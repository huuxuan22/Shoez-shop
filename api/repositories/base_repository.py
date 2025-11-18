from typing import Generic, TypeVar, List, Optional, Dict, Any, Sequence
from bson import ObjectId
from pymongo import ReturnDocument
from pymongo.errors import PyMongoError
from contextlib import asynccontextmanager
import uuid

ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType]):
    """Base class for data repositories using MongoDB."""

    def __init__(self, db, collection_name: str):
        self.db = db
        self.collection = db[collection_name]
        self.collection_name = collection_name

    async def __aenter__(self):
        return self

    async def update_one(self, filter_dict: dict, update_dict: dict):
        return await self.collection.update_one(filter_dict, update_dict)

    async def __aexit__(self, exc_type, exc, tb):
        # nếu cần cleanup, handle ở đây
        pass

    def _convert_id(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """Convert _id to string for JSON serialization"""
        if not document:
            return document
            
        # Convert _id to id
        if '_id' in document:
            document['id'] = str(document['_id'])
            del document['_id']
        
        # Convert all ObjectId fields to string recursively
        self._convert_objectids(document)
        return document
    
    def _convert_objectids(self, obj: Any) -> Any:
        """Recursively convert ObjectId to string in nested structures"""
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, dict):
            for key, value in obj.items():
                obj[key] = self._convert_objectids(value)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                obj[i] = self._convert_objectids(item)
        return obj

    async def delete_many_and_return(self, ids: List[str], id_key: str = "_id") -> List[ModelType]:
        """
        Xóa nhiều document theo danh sách ID và trả về các object đã xóa.
        """
        if not ids:
            return []

        # Chuyển string ID sang ObjectId nếu cần
        if id_key == "_id":
            object_ids = [ObjectId(i) for i in ids if ObjectId.is_valid(i)]
            filter_query = {id_key: {"$in": object_ids}}
        else:
            filter_query = {id_key: {"$in": ids}}

        # Lấy danh sách document trước khi xóa
        cursor = self.collection.find(filter_query)
        documents_to_delete = await cursor.to_list(length=len(ids))
        documents_to_delete = [self._convert_id(doc) for doc in documents_to_delete]

        # Xóa
        await self.collection.delete_many(filter_query)

        return documents_to_delete

    async def create(self, attributes: Dict[str, Any]) -> ModelType:
        """
        Creates the model instance.

        :param attributes: The attributes to create the model with.
        :return: The created model instance.
        """
        try:
            # Add timestamps if not provided
            if 'created_at' not in attributes:
                attributes['created_at'] = attributes['updated_at'] = self._get_current_timestamp()

            result = await self.collection.insert_one(attributes)
            created_doc = await self.collection.find_one({"_id": result.inserted_id})
            return self._convert_id(created_doc)
        except PyMongoError as e:
            raise Exception(f"Failed to create document: {str(e)}")

    async def find_one(self, query):
        return await self.collection.find_one(query)

    async def create_all(self, attributes_list: List[Dict[str, Any]]) -> List[ModelType]:
        """
        Creates multiple model instances.

        :param attributes_list: A list of dictionaries containing attributes for each model instance.
        :return: A list of the created model instances.
        """
        try:
            # Add timestamps to each document
            for attributes in attributes_list:
                if 'created_at' not in attributes:
                    attributes['created_at'] = attributes['updated_at'] = self._get_current_timestamp()

            result = await self.collection.insert_many(attributes_list)

            # Fetch all created documents
            created_ids = result.inserted_ids
            cursor = self.collection.find({"_id": {"$in": created_ids}})
            documents = await cursor.to_list(length=len(created_ids))

            return [self._convert_id(doc) for doc in documents]
        except PyMongoError as e:
            raise Exception(f"Failed to create multiple documents: {str(e)}")

    async def create_if_not_exist(
            self,
            filters: Dict[str, Any],
            create_data: Optional[Dict[str, Any]] = None,
    ) -> ModelType:
        """
        Create a model instance only if it doesn't already exist.

        :param filters: Fields and values to check existence.
        :param create_data: Data used to create the instance (optional, defaults to `filters`).
        :return: The existing or newly created model instance.
        """
        create_data = create_data or filters

        # Check if document exists
        existing = await self.collection.find_one(filters)
        if existing:
            return self._convert_id(existing)

        # Create new document
        return await self.create(create_data)

    async def update(
            self,
            entity_id: str,
            data: Dict[str, Any],
            id_key: str = "_id"
    ) -> Optional[ModelType]:
        """
        Update a document by ID.

        :param entity_id: The document ID
        :param data: The data to update
        :param id_key: The ID field name (default: "_id")
        :return: The updated document or None if not found
        """
        try:
            # Add updated_at timestamp
            data['updated_at'] = self._get_current_timestamp()

            # Convert string ID to ObjectId if needed
            if id_key == "_id" and not isinstance(entity_id, ObjectId):
                if not ObjectId.is_valid(entity_id):
                    return None
                entity_id = ObjectId(entity_id)

            updated_doc = await self.collection.find_one_and_update(
                {id_key: entity_id},
                {"$set": data},
                return_document=ReturnDocument.AFTER
            )

            return self._convert_id(updated_doc) if updated_doc else None
        except PyMongoError as e:
            raise Exception(f"Failed to update document: {str(e)}")

    async def update_all(self, filter_query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        """
        Update multiple documents.

        :param filter_query: The filter query
        :param update_data: The data to update
        :return: Number of modified documents
        """
        try:
            update_data['updated_at'] = self._get_current_timestamp()

            result = await self.collection.update_many(
                filter_query,
                {"$set": update_data}
            )
            return result.modified_count
        except PyMongoError as e:
            raise Exception(f"Failed to update multiple documents: {str(e)}")

    async def get_by_ids(
            self,
            ids: List[Any],
            id_key: str = "_id"
    ) -> List[ModelType]:
        """
        Returns the records matching the ids in the provided list.

        :param ids: List of ids to match.
        :param id_key: The field name to filter by.
        :return: The matching records.
        """
        if not ids:
            return []

        try:
            # Convert string IDs to ObjectId if needed
            if id_key == "_id":
                object_ids = []
                for id_val in ids:
                    if ObjectId.is_valid(id_val):
                        object_ids.append(ObjectId(id_val))
                filter_query = {"_id": {"$in": object_ids}}
            else:
                filter_query = {id_key: {"$in": ids}}

            cursor = self.collection.find(filter_query)
            documents = await cursor.to_list(length=1000)
            return [self._convert_id(doc) for doc in documents]
        except PyMongoError as e:
            raise Exception(f"Failed to get documents by IDs: {str(e)}")

    async def get_all(
            self,
            skip: int = 0,
            limit: int = 100,
            filter_query: Optional[Dict[str, Any]] = None,
            query: Optional[Dict[str, Any]] = None,
            sort: Optional[List[tuple]] = None,
            projection: Optional[Dict[str, Any]] = None
    ) -> List[ModelType]:
        """
        Returns a list of documents with optional sorting and projection.

        :param skip: The number of records to skip.
        :param limit: The number of records to return.
        :param filter_query: Additional filter query (preferred).
        :param query: Alias for filter_query (for backward compatibility).
        :param sort: List of tuples for sorting, e.g., [("field", 1)] for ascending, [("field", -1)] for descending.
        :param projection: Dictionary specifying which fields to include/exclude, e.g., {"field1": 1, "field2": 0}.
        :return: A list of documents.
        """
        try:
            # Support both filter_query and query for backward compatibility
            query_dict = filter_query or query or {}
            cursor = self.collection.find(query_dict, projection=projection)
            
            if sort:
                cursor = cursor.sort(sort)
            
            if skip > 0:
                cursor = cursor.skip(skip)
            
            cursor = cursor.limit(limit)
            documents = await cursor.to_list(length=limit)
            return [self._convert_id(doc) for doc in documents]
        except PyMongoError as e:
            raise Exception(f"Failed to get all documents: {str(e)}")

    async def get_by(
            self,
            field: str,
            value: Any,
            unique: bool = False
    ) -> Optional[ModelType] | List[ModelType]:
        """
        Returns documents matching the field and value.

        :param field: The field to match.
        :param value: The value to match.
        :param unique: Whether to return only one document.
        :return: The document(s) found.
        """
        try:
            if unique:
                document = await self.collection.find_one({field: value})
                return self._convert_id(document) if document else None
            else:
                cursor = self.collection.find({field: value})
                documents = await cursor.to_list(length=1000)
                return [self._convert_id(doc) for doc in documents]
        except PyMongoError as e:
            raise Exception(f"Failed to get documents by field: {str(e)}")

    async def get_by_id(
            self,
            value: Any,
            id_key: str = "_id"
    ) -> Optional[ModelType]:
        """
        Returns the document by ID.

        :param value: The ID value.
        :param id_key: The ID field name.
        :return: The document or None if not found.
        """
        try:
            # Convert string ID to ObjectId if needed
            if id_key == "_id" and not isinstance(value, ObjectId):
                if not ObjectId.is_valid(value):
                    return None
                value = ObjectId(value)

            document = await self.collection.find_one({id_key: value})
            return self._convert_id(document) if document else None
        except PyMongoError as e:
            raise Exception(f"Failed to get document by ID: {str(e)}")

    async def get_by_multi_fields(
            self,
            conditions: Dict[str, Any]
    ) -> Optional[ModelType]:
        """
        Returns documents matching multiple fields.

        :param conditions: Dictionary of field-value pairs.
        :return: The document found.
        """
        try:
            document = await self.collection.find_one(conditions)
            return self._convert_id(document) if document else None
        except PyMongoError as e:
            raise Exception(f"Failed to get documents by multiple fields: {str(e)}")

    async def delete(self, entity_id: str, id_key: str = "_id") -> bool:
        """
        Deletes the document by ID.

        :param entity_id: The document ID.
        :param id_key: The ID field name.
        :return: True if deleted, False otherwise.
        """
        try:
            if id_key == "_id" and not isinstance(entity_id, ObjectId):
                if not ObjectId.is_valid(entity_id):
                    return False
                entity_id = ObjectId(entity_id)

            result = await self.collection.delete_one({id_key: entity_id})
            return result.deleted_count > 0
        except PyMongoError as e:
            raise Exception(f"Failed to delete document: {str(e)}")

    async def delete_by_field(self, field: str, value: Any) -> int:
        """
        Deletes documents that match a specific field.

        :param field: The field name.
        :param value: The field value.
        :return: Number of deleted documents.
        """
        try:
            result = await self.collection.delete_many({field: value})
            return result.deleted_count
        except PyMongoError as e:
            raise Exception(f"Failed to delete documents by field: {str(e)}")

    async def delete_by_conditions(self, conditions: Dict[str, Any]) -> int:
        """
        Deletes documents that match the given conditions.

        :param conditions: A dictionary of field-value pairs.
        :return: The number of documents deleted.
        """
        try:
            result = await self.collection.delete_many(conditions)
            return result.deleted_count
        except PyMongoError as e:
            raise Exception(f"Failed to delete documents by conditions: {str(e)}")

    async def soft_delete_by_id(self, entity_id: str, id_key: str = "_id") -> bool:
        """
        Soft delete by setting is_deleted to True.

        :param entity_id: The document ID.
        :param id_key: The ID field name.
        :return: True if updated, False otherwise.
        """
        try:
            return await self.update(entity_id, {"is_deleted": True}, id_key) is not None
        except PyMongoError as e:
            raise Exception(f"Failed to soft delete document: {str(e)}")

    async def soft_delete_by_ids(self, ids: List[str], id_key: str = "_id") -> int:
        """
        Soft delete multiple documents by IDs.

        :param ids: List of document IDs.
        :param id_key: The ID field name.
        :return: Number of updated documents.
        """
        try:
            # Convert string IDs to ObjectId if needed
            if id_key == "_id":
                object_ids = []
                for id_val in ids:
                    if ObjectId.is_valid(id_val):
                        object_ids.append(ObjectId(id_val))
                filter_query = {"_id": {"$in": object_ids}}
            else:
                filter_query = {id_key: {"$in": ids}}

            result = await self.collection.update_many(
                filter_query,
                {
                    "$set": {
                        "is_deleted": True,
                        "updated_at": self._get_current_timestamp()
                    }
                }
            )
            return result.modified_count
        except PyMongoError as e:
            raise Exception(f"Failed to soft delete multiple documents: {str(e)}")

    async def exists_by_id(self, entity_id: str, id_key: str = "_id") -> bool:
        """
        Check if a document exists by ID.

        :param entity_id: The document ID.
        :param id_key: The ID field name.
        :return: True if exists, False otherwise.
        """
        try:
            if id_key == "_id" and not isinstance(entity_id, ObjectId):
                if not ObjectId.is_valid(entity_id):
                    return False
                entity_id = ObjectId(entity_id)

            document = await self.collection.find_one(
                {id_key: entity_id},
                projection={"_id": 1}
            )
            return document is not None
        except PyMongoError as e:
            raise Exception(f"Failed to check existence by ID: {str(e)}")

    async def exists_by_field(
            self,
            field: str,
            value: Any,
            additional_filters: Optional[Dict[str, Any]] = None,
            exclude_id: Optional[str] = None
    ) -> bool:
        """
        Check if a document exists by field value.

        :param field: The field name.
        :param value: The field value.
        :param additional_filters: Additional filter conditions.
        :param exclude_id: Exclude document with this ID.
        :return: True if exists, False otherwise.
        """
        try:
            query = {field: value}

            if additional_filters:
                query.update(additional_filters)

            if exclude_id:
                if not ObjectId.is_valid(exclude_id):
                    return False
                query["_id"] = {"$ne": ObjectId(exclude_id)}

            document = await self.collection.find_one(query, projection={"_id": 1})
            return document is not None
        except PyMongoError as e:
            raise Exception(f"Failed to check existence by field: {str(e)}")

    async def count(self, filter_query: Optional[Dict[str, Any]] = None) -> int:
        """
        Count documents.

        :param filter_query: Filter query.
        :return: Number of documents.
        """
        try:
            query = filter_query or {}
            return await self.collection.count_documents(query)
        except PyMongoError as e:
            raise Exception(f"Failed to count documents: {str(e)}")

    async def count_if(self, conditions: Dict[str, Any]) -> int:
        """
        Count documents with conditions.

        :param conditions: Filter conditions.
        :return: Number of documents.
        """
        return await self.count(conditions)

    def _get_current_timestamp(self):
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow()

    @asynccontextmanager
    async def transactional(self):
        """
        Context manager for transactions (MongoDB 4.0+).
        Note: MongoDB transactions require replica set.
        """
        async with await self.db.client.start_session() as session:
            try:
                async with session.start_transaction():
                    yield session
            except PyMongoError as e:
                await session.abort_transaction()
                raise e