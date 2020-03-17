from math import sin, cos, sqrt, atan2, radians


class User:

    total_posts = None
    closest_user = None
    closest_user_distance = None

    def __init__(self, user_dictionary):
        self.id = user_dictionary.get("id")
        self.username = user_dictionary.get("username")
        self.geo_lat = self.get_user_geo_lat(user_dictionary)
        self.geo_lng = self.get_user_geo_lng(user_dictionary)

    def get_total_posts(self, grouped_posts):
        user_id = self.id
        users_posts = grouped_posts.get(user_id)
        total_posts = len(users_posts)

        self.total_posts = total_posts

        return total_posts

    def get_closest_user(self, users_data):
        closest_user_distance = None
        closest_user = None

        for other_user in users_data:
            if other_user.get("id") == self.id:
                continue

            distance = self.get_distance(User.get_user_geo_lat(other_user), User.get_user_geo_lng(other_user))

            if closest_user_distance is None or distance < closest_user_distance:
                closest_user_distance = distance
                closest_user = other_user

        self.closest_user_distance = closest_user_distance
        self.closest_user = closest_user

        return closest_user

    def print_information(self):
        distance_text = ' and close to ' + self.closest_user.get("username") + ' by ' + str(round(self.closest_user_distance)) + ' km'

        if self.total_posts == 0:
            print(self.username + ' has no posts' + distance_text)
        elif self.total_posts == 1:
            print(self.username + ' has ' + str(1) + ' post' + distance_text)
        else:
            print(self.username + ' has ' + str(self.total_posts) + ' posts' + distance_text)

    def get_distance(self, lat2, lng2):
        r = 6373.0
        lat = radians(self.geo_lat)
        lng = radians(self.geo_lng)
        lat2 = radians(lat2)
        lng2 = radians(lng2)

        a = sin((lat2 - lat) / 2) ** 2 + cos(lat) * cos(lat2) * sin((lng2 - lng) / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = r * c
        return distance

    @staticmethod
    def get_user_geo_lat(user_dictionary):
        return float(user_dictionary.get("address").get("geo").get("lat"))

    @staticmethod
    def get_user_geo_lng(user_dictionary):
        return float(user_dictionary.get("address").get("geo").get("lng"))

