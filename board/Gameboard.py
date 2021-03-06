from enum import Enum

from board.Position import Position

DIRECTION = {
    'u': Position(0, -1),
    'd': Position(0, 1),
    'r': Position(1, 0),
    'l': Position(-1, 0)
}


class Gameboard(object):
    """
    Keeps track of all elements of a board:
        walls, goals, boxes, the player and moves

    - moves_available: returns which moves are possible for the player
        in it's current position
    - move: moves the player in the specified direction and adjusts
        other elements accordingly
    - hash: only depends on the placement of boxes and the player.
    """

    def __init__(self):
        """ Contructor """
        self.num_lines = 0
        self.size = ()
        self.walls = set()  # all the walls
        self.goals = set()  # all the goals
        self.boxes = set()  # all the boxes w/ their states
        self.player = None  # the player with their state
        self.moves = []  # array of moves made

    def move(self, direction):
        """
        @param direction: a direction in the set [u,r,d,l]
            (assumes this is a valid movement)

        Adjusts the board object given a movement.
        """
        pos1 = self.player + DIRECTION[direction]
        pos2 = self.player + DIRECTION[direction].multiply(2)

        if pos1 in self.boxes:  # move box if in path
            self.boxes.remove(pos1)
            self.boxes.add(pos2)

        self.player = pos1  # reset player position
        self.moves.append(direction)  # log the move

        return self

    def manhattan(self):
        """
        A naive heuristic. Returns the sum of the shortest distance between the
        player with an unplaced box and the distances between each box and their
        nearest goals
        """
        unplaced_boxes = self.boxes.difference(self.goals)
        unfilled_goals = self.goals.difference(self.boxes)
        if not unplaced_boxes:
            return 0

        player_dist = min([self.player.manhattan_distance(box) for box in unplaced_boxes])

        box_distances = sum([min([box.manhattan_distance(goal) for goal in unfilled_goals]) for box in unplaced_boxes])

        return player_dist + box_distances

    def finished(self):
        """
        Return  True: if all boxes are on goals.
                False: Otherwise
        """
        if not self.goals.difference(self.boxes):  # if no overlap
            return True
        return False

    def moves_available(self):
        """
        @return array (move, cost)
            move: available moves in [u,r,d,l]
            cost:   2 if pushing a box,
                    1 otherwise

        Checks that moves that involve pushing a block are possible given the
        placement of walls.
        """
        theoretical_moves = ['u', 'r', 'd', 'l']
        possible_moves = []

        for direction in theoretical_moves:
            # position the player would be in
            new_pos = self.player + DIRECTION[direction]
            # position the box the player pushes would be
            next_pos = self.player + DIRECTION[direction].multiply(2)

            if new_pos in self.walls:  # blocked by walls
                continue
            elif new_pos in self.boxes:  # pushing a box
                if next_pos in self.walls.union(self.boxes):  # into a wall/box
                    continue
                possible_moves.append((direction, 1))
            else:  # regular movement
                possible_moves.append((direction, 1))

        return possible_moves

    def add_player(self, x, y):
        """ sets the player """
        self.player = Position(x, y)

    def add_box(self, x, y):
        """ adds a box """
        self.boxes.add(Position(x, y))

    def add_goal(self, x, y):
        """ adds a goal """
        self.goals.add(Position(x, y))

    def add_wall(self, x, y):
        """ adds a wall to the board """
        self.walls.add(Position(x, y))

    def deadlock(self):
        for box in self.boxes:
            if box not in self.goals:
                if box + Position(0, -1) in self.walls and box + Position(-1, 0) in self.walls:
                    return True
                if box + Position(0, 1) in self.walls and box + Position(-1, 0) in self.walls:
                    return True
                if box + Position(0, -1) in self.walls and box + Position(1, 0) in self.walls:
                    return True
                if box + Position(0, 1) in self.walls and box + Position(1, 0) in self.walls:
                    return True
        return False

    def __hash__(self):
        """ hashes the board object """
        return hash((
            hash(frozenset(self.boxes)),
            hash(self.player)
        ))

    def __str__(self):
        """
        Returns a string representation like the input files
        """
        str_board = []
        for y in range(self.num_lines):
            str_board.append([' '] * 20)  # 20 is an abitrary width

        for wall in self.walls:  # walls
            str_board[wall.y][wall.x] = '#'

        for box in self.boxes.difference(self.goals):  # boxes - goals
            str_board[box.y][box.x] = '$'

        for box in self.goals.union(self.boxes):  # boxes & goals
            if box in self.goals and box in self.boxes:
                str_board[box.y][box.x] = '*'

        for goal in self.goals.difference(self.boxes):  # goals - boxes
            str_board[goal.y][goal.x] = '.'

        if self.player not in self.goals:  # player on goal
            str_board[self.player.y][self.player.x] = '@'

        else:  # player off goal
            str_board[self.player.y][self.player.x] = '+'

        return '\n'.join([''.join(line) for line in str_board])
