import wikipedia.wikipedia as wiki


class WikipediaService:
    def __init__(self, search_for: str):
        self.search_for = search_for

    def search(self) -> str:
        result = wiki.summary(self.search_for, sentences=2)  # first 2 sentences only
        return result
