import Search
from copy import deepcopy
from time import time


class DepthSearch(Search.Search):

    def __init__(self):
        super().__init__()

    def do_search(self, gameboard, print_steps=None):
        print('Depth Search')
        start = time()
        """
        @param gameboard: a Gameboard object
        @param print_steps: flag to print intermediate steps

        @return (records, board)
            records: a dictionary keeping track of necessary statistics
            board: a copy of the board at the finished state.
                Contains an array of all moves performed.

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

        unfolded = [gameboard]  # initialize queue

        while True:
            if print_steps:
                print("{}\t{}".format(records['repeat'], len(records['explored'])))

            if not unfolded:  # if empty queue, fail
                print(records)
                raise Exception('Solution not found.')

            if time() - start >= 10800:  # Time limited for 3 hours
                return records, None

            node_board = unfolded.pop(0)
            records['explored'].add(hash(node_board))
            records['fringe'] = len(unfolded)

            if node_board.finished():  # if finished, return
                return records, node_board

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
