import unittest
from post import Post


class TestPost(unittest.TestCase):

    list_titles = ['test title 1', 'test title 2', 'test title 3']

    def test_get_repeated_titles(self):
        result = Post.get_repeated_titles(self.list_titles)
        self.assertEqual(result, [])
        self.list_titles.append('test title 3')
        result = Post.get_repeated_titles(self.list_titles)
        self.assertEqual(result, ['test title 3'])
        self.list_titles.append('test title 3')
        result = Post.get_repeated_titles(self.list_titles)
        self.assertEqual(result, ['test title 3'])

