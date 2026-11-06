
import requests
import json
from pathlib import Path
from datetime import datetime

if __package__:
    from .s3_upload import upload_to_s3
else:
    from s3_upload import upload_to_s3

API_URL = "https://jsonplaceholder.typicode.com/posts"

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def fetch_api_data():
    """Fetch sample posts from the public API."""

    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()

        posts = response.json()

        print(f"Successfully fetched {len(posts)} posts.")

        return posts

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return None


def save_data(posts):
    """Save API data locally as a JSON file."""

    DATA_DIR.mkdir(exist_ok=True)

    filename = f"posts-{datetime.now():%Y%m%d-%H%M%S}.json"
    file_path = DATA_DIR / filename

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)

    print(f"Data saved to: {file_path}")

    return file_path


def main():
    posts = fetch_api_data()

    if posts is None:
        print("Workflow stopped: API data could not be fetched.")
        return

    file_path = save_data(posts)

    upload_success = upload_to_s3(file_path)

    if upload_success:
        print("Workflow completed successfully!")
    else:
        print("Workflow completed with an S3 upload failure.")


if __name__ == "__main__":
    main()

