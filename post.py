class Post:
    def __init__(self, post_dictionary):
        self.user_id = post_dictionary.get("userId")
        self.id = post_dictionary.get("id")
        self.title = post_dictionary.get("title")
        self.body = post_dictionary.get("body")

    @staticmethod
    def get_repeated_titles(titles):
        checked = []
        repeated = []

        for title in titles:
            if title in checked:
                if title not in repeated:
                    repeated.append(title)
            else:
                checked.append(title)

        if not repeated:
            print("There is no common titles")
        else:
            print(repeated)

        return repeated
