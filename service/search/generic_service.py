import webbrowser


class SearchService:
    def __init__(self, search_for: str):
        self.search_for: str = search_for

    def search_google(self) -> None:
        webbrowser.open("google.com/search?q=" + self.search_for)

    def search_youtube(self) -> None:
        webbrowser.open("youtube.com/results?search_query=" + self.search_for)
