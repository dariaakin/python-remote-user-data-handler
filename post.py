class Post:
    def __init__(self, post_dictionary):
        # Collecting information from post_dictionary
        self.user_id = post_dictionary.get("userId")
        self.id = post_dictionary.get("id")
        self.title = post_dictionary.get("title")
        self.body = post_dictionary.get("body")

    # Collecting repeated titles
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

        return repeated
