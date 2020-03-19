import unittest
from user import User


class TestUser(unittest.TestCase):

    grouped_post = {
        1: [
            {
                "userId": 1,
                "id": 1,
                "title": "title 1",
            },
            {
                "userId": 1,
                "id": 2,
                "title": "title 2",
            },
        ],
    }

    users_data = [
      {
        "id": 1,
        "username": "User1",
        "address": {
          "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
          }
        },
      },
      {
        "id": 2,
        "username": "User2",
        "address": {
          "geo": {
            "lat": "-38.0000",
            "lng": "81.0000"
          }
        },
      },
      {
        "id": 3,
        "username": "User3",
        "address": {
            "geo": {
                "lat": "-3.0000",
                "lng": "8.0000"
            }
          },
       }
    ]

    def test_get_closest_user(self):
        user_object = User(self.users_data[0])
        result = user_object.get_closest_user(self.users_data)
        self.assertEqual(result.get("id"), 2)

    def test_get_total_posts(self):
        user_object = User(self.users_data[0])
        result = user_object.get_total_posts(self.grouped_post)
        self.assertEqual(result, 2)

    def test_distance(self):
        user_object = User(self.users_data[0])
        result = user_object.get_distance(-43.9509, -34.4618)
        expected_value = 8897.75
        # 0.05 accuracy algorithm

        self.assertTrue((expected_value-expected_value*0.0005) < result < (expected_value+expected_value*0.0005))

        user_object.geo_lat = 0
        user_object.geo_lng = 100

        result = user_object.get_distance(0, 100)

        self.assertEqual(round(result), 0)

    def test_get_user_geo_lat(self):
        result = User.get_user_geo_lat(self.users_data[0])
        self.assertEqual(result, -37.3159)

    def test_get_user_geo_lng(self):
        result = User.get_user_geo_lng(self.users_data[0])
        self.assertEqual(result, 81.1496)
