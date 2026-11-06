
import boto3
from botocore.exceptions import ClientError
from pathlib import Path


BUCKET_NAME = "python-api-s3-automation-umar-2026"
REGION = "eu-north-1"
OBJECT_KEY = "posts-20261105-155543.json"

PROJECT_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = PROJECT_DIR / "data" / "downloads"


def download_from_s3():
    """Download a JSON file from Amazon S3."""

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    destination = DOWNLOAD_DIR / OBJECT_KEY

    s3_client = boto3.client("s3", region_name=REGION)

    try:
        s3_client.download_file(
            BUCKET_NAME,
            OBJECT_KEY,
            str(destination)
        )

        print(f"Successfully downloaded {OBJECT_KEY}.")
        print(f"Saved to: {destination}")
        return True

    except ClientError as error:
        print(f"S3 download failed: {error}")
        return False


if __name__ == "__main__":
    download_from_s3()

