import Search
from copy import deepcopy
from time import time


class BreadthSearch(Search.Search):

    def __init__(self):
        super().__init__()

    def do_search(self, gameboard, print_steps=None):
        print('Breadth Search')
        start = time()
        """
            @param board: a Board object
            @param print_steps: flag to print intermediate steps

            @return (records, board)
                records: a dictionary keeping track of necessary statistics
                board: a copy of the board at the finished state.
                    Contains an array of all moves performed.

            Performs a breadth first search on the sokoban board. Follows the
                implementation on pg 83 of AIMA closely.
            """
        records = {
            'node': 0,
            'repeat': 0,
            'fringe': 0,
            'deadlock': 0,
            'explored': set([])
        }
        if print_steps:
            print('repeat\tseen')

        if gameboard.finished():  # check if initial state is complete
            return records, gameboard

        unfolded = [gameboard]  # initialize queue
        records['node'] += 1

        while True:
            if print_steps:
                print("{}\t{}".format(records['repeat'], len(records['explored'])))

            if not unfolded:  # fail if no options left
                print(records)
                raise Exception('Solution not found.')

            if time() - start >= 10800:  # Time limited for 3 hours
                return records, None

            node_board = unfolded.pop(0)  # move to next node in array
            records['explored'].add(hash(node_board))  # add hash to explored
            records['fringe'] = len(unfolded)  #

            for direction, cost in node_board.moves_available():
                # copy the board and perform the move
                child_board = deepcopy(node_board).move(direction)
                records['node'] += 1

                if not child_board.deadlock():
                    if hash(child_board) not in records['explored'] and child_board not in unfolded:
                        if child_board.finished():  # if the board is solved
                            return records, child_board
                        unfolded.append(child_board)  # else, add to the queue
                    else:  # child board is a repeat
                        records['repeat'] += 1
                else:
                    records['deadlock'] += 1
