import json
import urllib.request
from typing import Final
from user import User
from post import Post


class Application:
    POSTS_URL: Final = "https://jsonplaceholder.typicode.com/posts"
    USERS_URL: Final = "https://jsonplaceholder.typicode.com/users"

    @staticmethod
    def handle_remote_data():
        # Downloading posts data
        posts_data = Application.download_data(Application.POSTS_URL)
        # Downloading users data
        users_data = Application.download_data(Application.USERS_URL)

        grouped_posts = {}
        titles_list = []

        for post in posts_data:
            # Creating a Post class instance by post dictionary
            post_object = Post(post)

            # Grouping posts by user
            current_user_id = post_object.user_id

            # Creating posts dictionary where user id is a key and containing information in a list
            if current_user_id not in grouped_posts:
                grouped_posts[current_user_id] = list()

            # Adding new users to grouped_posts
            grouped_posts[current_user_id].append(post_object)

            # Collecting all titles
            titles_list.append(post_object.title)

        for user in users_data:
            # Creating a User class instance by user dictionary
            user_object = User(user)

            # Collecting user's total posts
            user_object.get_total_posts(grouped_posts)
            # Finding closest user and distance between users
            user_object.get_closest_user(users_data)
            # Printing collected information
            user_object.print_information()

        # Collecting repeated titles
        repeat_titles = Post.get_repeated_titles(titles_list)

        # Printing information about repeat titles
        if len(repeat_titles) == 0:
            print("There is no common title")
        else:
            print(repeat_titles)

    @staticmethod
    def download_data(url):
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            return data


Application.handle_remote_data()
