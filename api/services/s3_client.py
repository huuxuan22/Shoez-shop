import boto3
from config.config import get_settings

settings = get_settings()

s3 = boto3.client('s3',
    endpoint_url=settings.minio_url,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
)

bucket_name = settings.bucket_name

# tổng kíc thước file của dự án
def calculate_prefix_size(bucket_name: str, prefix: str) -> str:
    total_size = 0
    continuation_token = None
    while continuation_token is None:
        list_kwargs = {
            'Bucket': bucket_name,
            'Prefix': prefix,
        }
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token
        response = s3.list_objects_v2(**list_kwargs)
        contents = response.get('Contents', [])

        for content in contents:
            total_size += content['Size']
        if response.get('IsTruncated'):
            continuation_token = response.get('NextContinuationToken')
        else:
            break
    return total_size

def get_all_object_by_object_key(bucket_name: str, object_key_prefix: str):
    response = s3.list_objects_v2(
        Bucket=bucket_name,
        Prefix=object_key_prefix
    )
    return [obj['Key'] for obj in response.get('Contents', [])]


