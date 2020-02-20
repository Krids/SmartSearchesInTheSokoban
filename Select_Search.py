from searches.Depth_Search import DepthSearch


class SelectSearch:

    def __init__(self, search):
        self.search = search if search is not None else DepthSearch()

    def do_the_search(self, gameboard):
        return self.search.do_search(gameboard)
