from model import Role
from repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository[Role]):
    model = Role


