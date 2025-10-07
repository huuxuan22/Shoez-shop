import uuid
# from services.s3_client import s3, BUCKET_NAME

def upload_image_to_s3(file_bytes: bytes, category: str) -> str:
    unique_filename = f"{uuid.uuid4()}.jpg"
    s3_key = f"{category}/{unique_filename}"

    # s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=file_bytes)

    return s3_key  # Trả về key để lưu vào DB hoặc phản hồi
