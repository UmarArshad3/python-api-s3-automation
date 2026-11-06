import boto3
from botocore.exceptions import ClientError
from pathlib import Path


BUCKET_NAME = "python-api-s3-automation-umar-2026"
REGION = "eu-north-1"


def upload_to_s3(file_path):
    """Upload a JSON file to Amazon S3."""

    file_path = Path(file_path)

    if not file_path.is_file():
        print(f"File not found: {file_path}")
        return False

    s3_client = boto3.client("s3", region_name=REGION)

    try:
        s3_client.upload_file(
            str(file_path),
            BUCKET_NAME,
            file_path.name
        )

        print(f"Successfully uploaded {file_path.name} to S3.")
        return True

    except ClientError as error:
        print(f"S3 upload failed: {error}")
        return False

