from copy import deepcopy
from time import time
import Search


class IterativeDepthSearch(Search.Search):

    def __init__(self):
        super().__init__()

    def depth_search_limited(self, gameboard, limit, print_steps=None, nexts=None):
        """
        @param gameboard: a Gameboard object
        @param limit: the max depth
        @param print_steps: flag to print intermediate steps
        @param nexts: a list of Gameboard objects

        @return (records, board, nexts)
            records: a dictionary keeping track of necessary statistics
            board: a copy of the board at the finished state.
                Contains an array of all moves performed.
            nexts: the max depth leafs for the next search

        Performs a depth first search on the sokoban board.
        Doesn't add duplicate nodes to the stack so as to prevent looping.
        """

        records = {
            'node': 0,
            'repeat': 0,
            'fringe': 0,
            'deadlock': 0,
            'explored': set()
        }

        if print_steps:
            print('repeat\tseen')

        if gameboard.finished():  # check if initial state is complete
            return records, gameboard

        if nexts is None:
            unfolded = [gameboard]  # initialize queue
            nexts = []
        else:
            unfolded = []
            unfolded.extend(nexts)
            nexts = []

        while True:
            if print_steps:
                print("{}\t{}".format(records['repeat'], len(records['explored'])))

            if not unfolded:  # if empty queue, fail
                # print(records)
                return records, None, nexts

            node_board = unfolded.pop(0)
            records['explored'].add(hash(node_board))
            records['fringe'] = len(unfolded)

            if node_board.finished():  # if finished, return
                return records, node_board, nexts

            if len(node_board.moves) < limit:

                choices = node_board.moves_available()
                if not choices:  # if no options
                    unfolded.pop(0)
                else:  # regular
                    for direction, cost in choices:
                        records['node'] += 1
                        child_board = deepcopy(node_board).move(direction)

                        if not child_board.deadlock():
                            if hash(child_board) not in records['explored'] and child_board not in unfolded:
                                unfolded.insert(0, child_board)
                            else:
                                records['repeat'] += 1
                        else:
                            records['deadlock'] += 1
            else:
                nexts.insert(0, node_board)

    def do_search(self, gameboard, print_steps=False):
        print('Iterative Depth Search')
        start = time()
        depth = 1
        records = {
            'node': 0,
            'repeat': 0,
            'fringe': 0,
            'deadlock': 0,
            'explored': set()
        }
        nexts = None
        while time() - start <= 10800:  # Time limited in 3 hours
            records, node, nexts = self.depth_search_limited(gameboard, depth, print_steps, nexts)

            if node is not None:
                return records, node

            depth += 1
        return records, None
