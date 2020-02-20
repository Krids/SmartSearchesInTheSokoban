import Search
from copy import deepcopy


class AStarPriorityCostQueue(object):

    def __init__(self):
        self.queue = []
        self.roster = {}

    def push(self, h_cost, real_cost, item):
        total_coast = (h_cost + real_cost)
        if hash(item) in self.roster:
            print(item)
            print('ERROR')
            raise Exception('Repeat item being added to priority queue')

        self.roster[hash(item)] = total_coast

        add_it = True
        for index, (h_cost, real_cost, node) in enumerate(self.queue):
            if total_coast <= h_cost:
                self.queue.insert(index, (total_coast, real_cost, item))
                add_it = False
                break
        if add_it:
            self.queue.append((total_coast, real_cost, item))

    def pop(self, index=0):
        h_cost, real_cost, item = self.queue.pop(index)
        del self.roster[hash(item)]

        assert len(self.queue) == len(self.roster.keys())

        return h_cost, real_cost, item

    def update_cost(self, h_cost, real_cost, item):
        total_cost = (h_cost + real_cost)
        if total_cost < self.roster[hash(item)]:
            for index, (element_total_cost, element_h_cost, element) in enumerate(self.queue):
                if hash(item) == hash(element):
                    self.queue[index] = (total_cost, real_cost, item)
                    self.roster[hash(item)] = total_cost

    def __contains__(self, item):
        return hash(item) in self.roster.keys()

    def __nonzero__(self):
        return len(self.queue) > 0 and len(self.roster.keys()) > 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


class AStarSearch(Search.Search):

    def __init__(self):
        super().__init__()

    def do_search(self, gameboard):
        print('A* Search')

        """
        @param board: a Board object
        @param print_steps: flag to print intermediate steps

        @return (records, board)
            records: a dictionary keeping track of necessary statistics
            board: a copy of the board at the finished state.
                Contains an array of all moves performed.

        Performs an A* search to solve the Sokoban puzzle.
        """
        records = {
            'node': 0,
            'repeat': 0,
            'fringe': 0,
            'deadlock': 0,
            'explored': set()
        }

        if gameboard.finished():  # check if initial state is complete
            return records, gameboard

        board_queue = AStarPriorityCostQueue()  # initialize queue
        board_queue.push(0, gameboard.manhattan(), gameboard)
        records['node'] += 1

        while True:

            records['fringe'] = len(board_queue)
            if not board_queue:  # fail if no options left
                print(records)
                raise Exception('Solution not found.')

            total_cost, real_cost, node_board = board_queue.pop()  # grab the top of the queue

            if node_board.finished():  # return if solved
                return records, node_board
            records['explored'].add(hash(node_board))  # log board

            for direction, cost in node_board.moves_available():

                child_board = deepcopy(node_board).move(direction)  # copy & move
                records['node'] += 1

                if not child_board.deadlock():
                    if hash(child_board) not in records['explored']:  # if not explored
                        if child_board not in board_queue:  # if not in queue
                            board_queue.push(real_cost + cost, child_board.manhattan(), child_board)
                        else:  # check if cost can be made lower
                            board_queue.update_cost((cost + real_cost), child_board.manhattan(), child_board)
                            records['repeat'] += 1
                    else:  # log repeat if already explored
                        records['repeat'] += 1
                else:
                    records['deadlock'] += 1
