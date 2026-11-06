
import unittest
from unittest.mock import patch, Mock
from pathlib import Path
import tempfile
import json

from src.main import fetch_api_data, save_data


class TestAPIWorkflow(unittest.TestCase):

    @patch("src.main.requests.get")
    def test_fetch_api_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {"id": 1, "title": "Test post"}
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_api_data()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        mock_get.assert_called_once()

    @patch("src.main.requests.get")
    def test_fetch_api_data_failure(self, mock_get):
        mock_get.side_effect = Exception("Unexpected error")

        # The production function catches RequestException,
        # so test a realistic requests exception.
        import requests
        mock_get.side_effect = requests.exceptions.ConnectionError(
            "Connection failed"
        )

        result = fetch_api_data()

        self.assertIsNone(result)

    def test_save_data_creates_json_file(self):
        sample_posts = [
            {"id": 1, "title": "Test post"}
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("src.main.DATA_DIR", Path(temp_dir)):
                file_path = save_data(sample_posts)

                self.assertTrue(file_path.exists())

                with file_path.open("r", encoding="utf-8") as file:
                    saved_data = json.load(file)

                self.assertEqual(saved_data, sample_posts)


if __name__ == "__main__":
    unittest.main()

