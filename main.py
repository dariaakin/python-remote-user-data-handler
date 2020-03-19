import json
import urllib.request
from typing import Final
from user import User
from post import Post

POSTS_URL: Final = "https://jsonplaceholder.typicode.com/posts"
USERS_URL: Final = "https://jsonplaceholder.typicode.com/users"


def handle_remote_data():
    posts_data = download_data(POSTS_URL)
    users_data = download_data(USERS_URL)
    print(type(users_data))

    grouped_posts = {}
    titles_list = []

    for post in posts_data:
        post_object = Post(post)

        # grouping posts by user
        current_user_id = post_object.user_id

        if current_user_id not in grouped_posts:
            grouped_posts[current_user_id] = list()

        grouped_posts[current_user_id].append(post_object)

        # collecting all titles
        current_title = post_object.title
        titles_list.append(current_title)

    for user in users_data:
        user_object = User(user)

        user_object.get_total_posts(grouped_posts)
        user_object.get_closest_user(users_data)
        user_object.print_information()

    repeat_titles = Post.get_repeated_titles(titles_list)
    if len(repeat_titles) == 0:
        print("There is no common title")
    else:
        print(repeat_titles)


def download_data(url):
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        return data


handle_remote_data()
