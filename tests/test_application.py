import unittest
from main import Application


class TestApplication(unittest.TestCase):
    # Checking if download_data returns a list
    def test_download_data(self):
        result = Application.download_data(Application.POSTS_URL)
        self.assertIsInstance(result, list)

