
import unittest
from unittest.mock import patch, Mock
from botocore.exceptions import ClientError
from pathlib import Path
import tempfile

from src.s3_upload import upload_to_s3


class TestS3Upload(unittest.TestCase):

    @patch("src.s3_upload.boto3.client")
    def test_upload_success(self, mock_boto_client):
        mock_s3 = Mock()
        mock_boto_client.return_value = mock_s3

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.json"
            file_path.write_text('{"id": 1}', encoding="utf-8")

            result = upload_to_s3(file_path)

            self.assertTrue(result)

            mock_s3.upload_file.assert_called_once_with(
                str(file_path),
                "python-api-s3-automation-umar-2026",
                "test.json"
            )

    @patch("src.s3_upload.boto3.client")
    def test_upload_file_not_found(self, mock_boto_client):
        result = upload_to_s3("missing-file.json")

        self.assertFalse(result)
        mock_boto_client.assert_not_called()

    @patch("src.s3_upload.boto3.client")
    def test_upload_client_error(self, mock_boto_client):
        mock_s3 = Mock()

        mock_s3.upload_file.side_effect = ClientError(
            {
                "Error": {
                    "Code": "AccessDenied",
                    "Message": "Access denied"
                }
            },
            "PutObject"
        )

        mock_boto_client.return_value = mock_s3

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.json"
            file_path.write_text('{"id": 1}', encoding="utf-8")

            result = upload_to_s3(file_path)

            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

