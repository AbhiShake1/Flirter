import webbrowser


class GoogleService:
    def __init__(self, search_for: str):
        self.search_for = search_for

    def search(self) -> None:
        # open web browser and search
        webbrowser.open("google.com/search?q=" + self.search_for)
