import unittest
from main import Application


class TestApplication(unittest.TestCase):
    def test_download_data(self):
        result = Application.download_data(Application.POSTS_URL)
        self.assertIsInstance(result, list)

