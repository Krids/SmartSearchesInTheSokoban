from enum import Enum
from abc import ABC, abstractmethod


class SearchType(Enum):
    A_Star_Search = 1
    Bidirectional_Search = 2
    Breadth_Search = 3
    Depth_Search = 4
    Mountain_Climb_Search = 5


class Search(ABC):

    @abstractmethod
    def do_search(self, gameboard):
        pass
