# Python API to Amazon S3 Automation

A Python automation project that fetches data from a public REST API, saves the response as a JSON file, and uploads it to Amazon S3 using Boto3.

This project demonstrates Python scripting, REST API integration, AWS S3 storage, automated testing, and CI with GitHub Actions.

## Project Overview

The application retrieves sample posts from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/), saves the returned data locally, and uploads the generated JSON file to an Amazon S3 bucket.

## Screenshots & Diagrams

### Architecture
![Python API to S3 architecture](screenshots/python-api-s3-architecture.png.drawio.png)

### GitHub Actions CI
![GitHub Actions CI](screenshots/github-actions-ci.png)

### Successful Workflow Run
![Successful workflow](screenshots/successful-workflow.png)

### Automated Tests
![Automated tests](screenshots/automated-tests.png)

### S3 Objects
![S3 objects](screenshots/s3-objects.png)

## Architecture

1. **API Integration:** Fetches posts from JSONPlaceholder using Python Requests.
2. **Local Storage:** Saves API responses as timestamped JSON files.
3. **AWS S3 Upload:** Uploads generated files to Amazon S3 using Boto3.
4. **S3 Download:** Includes a script to download an object from S3.
5. **Data Verification:** Uses SHA-256 checksums to verify downloaded files against their originals.
6. **Automated Testing:** Tests application and upload functionality using Python `unittest` and mocks.
7. **Continuous Integration:** GitHub Actions automatically runs the test suite on pushes and pull requests to `main`.

## Technologies Used

- Python 3
- Requests
- Boto3
- Amazon S3
- AWS IAM
- JSON
- Git and GitHub
- GitHub Actions
- Python unittest and unittest.mock

## Project Structure

```text
python-api-s3-automation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── main.py
│   ├── s3_upload.py
│   └── s3_download.py
├── tests/
│   ├── test_main.py
│   └── test_s3_upload.py
├── requirements.txt
├── .gitignore
└── README.md
```

Generated JSON files and downloaded data are excluded from Git using `.gitignore`.

## Prerequisites

- Python 3
- An AWS account
- An existing Amazon S3 bucket
- AWS credentials configured through a supported Boto3 credential provider

## Setup

Clone the repository:

```bash
git clone https://github.com/UmarArshad3/python-api-s3-automation.git
cd python-api-s3-automation
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## AWS Configuration

The application uses Boto3 to communicate with Amazon S3.

Configure AWS credentials using a supported method, such as the AWS CLI:

```bash
aws configure
```

Current application configuration:

- **S3 bucket:** `python-api-s3-automation-umar-2026`
- **AWS region:** `eu-north-1`

These values are defined in `src/s3_upload.py`.

The AWS identity used by the application needs appropriate permissions for the configured bucket, including `s3:PutObject` and `s3:GetObject`.

Keep AWS access keys and secret credentials out of the source code and Git repository.

## Running the Application

Run the complete API-to-S3 workflow:

```bash
python src/main.py
```

The application:

1. Fetches 100 sample posts from the API.
2. Saves the response as a timestamped JSON file in `data/`.
3. Uploads the generated file to the configured S3 bucket.
4. Reports whether the workflow completed successfully.

## Downloading an S3 Object

The project also includes an S3 download script:

```bash
python src/s3_download.py
```

It downloads the configured S3 object into the local project data directory.

## Running Automated Tests

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

The tests cover:

- Successful API data retrieval
- API connection failure handling
- JSON file creation
- Successful S3 upload
- Missing local file handling
- S3 upload error handling

AWS and API calls are mocked in the unit tests, so the test suite does not require live AWS operations or API requests.

## Continuous Integration

GitHub Actions is configured to run automated tests when:

- Code is pushed to the `main` branch.
- A pull request targets the `main` branch.

The workflow installs the project dependencies and executes the Python unit tests on an Ubuntu runner.

## Security Considerations

- AWS credentials are not stored in the repository.
- Generated data files are excluded using `.gitignore`.
- S3 public access should remain blocked.
- AWS IAM permissions should follow the principle of least privilege.

## Project Learning Outcomes

This project demonstrates practical experience with:

- Consuming REST APIs using Python
- Processing and storing JSON data
- Automating AWS S3 uploads and downloads
- Managing AWS credentials and IAM permissions
- Verifying file integrity with SHA-256
- Writing automated unit tests with mocks
- Building a GitHub Actions CI pipeline

## Author

**Umar Arshad**

GitHub: [UmarArshad3](https://github.com/UmarArshad3)
