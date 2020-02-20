from time import time
from enum import Enum

from Select_Search import SelectSearch

import pandas as pd

import sys
import os

from board import Gameboard
from searches.A_Star_Search import AStarSearch
from searches.Iterative_Depth_Search import IterativeDepthSearch
from searches.Breadth_Search import BreadthSearch
from searches.Depth_Search import DepthSearch

WALL = {'#'}
PLAYER = {'@', '+'}
GOAL = {'.', '+', '*'}
BOX = {'$', '*'}


class SearchType(Enum):
    A_Star_Search = 4
    Iterative_Depth_Search = 3
    Breadth_Search = 1
    Depth_Search = 2


def load_map(filename):
    """
    @param filename: A file containing an ascii sokoban puzzle.
    @return: a Board obj representing the map

    Constructs a sokoban board object and returns it.

    Map specifications
        1st line contains the # of lines.
            @ : player on ground
            + : player on goal
            # : wall
            $ : box off goal
            * : box on goal
            . : empty goal
    """
    gameboard = Gameboard()

    with open(filename, 'r') as f:
        read_data = f.read()
        lines = read_data.split('\n')
        gameboard.num_lines = len(lines)

        for y, line in enumerate(lines):
            line = line.replace('\n', '')
            if line:
                for x, char in enumerate(line):
                    if char in WALL:
                        gameboard.add_wall(x, y)
                    if char in GOAL:
                        gameboard.add_goal(x, y)
                    if char in BOX:
                        gameboard.add_box(x, y)
                    if char in PLAYER:
                        gameboard.add_player(x, y)
    return gameboard


def main():
    path = './screens//screen.{}'.format(sys.argv[1])  # First arg
    gb = load_map(path)
    arg2 = sys.argv[2]
    arg2 = int(arg2)
    if arg2 == SearchType.A_Star_Search.value:
        s = AStarSearch()
    elif arg2 == SearchType.Iterative_Depth_Search.value:
        s = IterativeDepthSearch()
    elif arg2 == SearchType.Breadth_Search.value:
        s = BreadthSearch()
    elif arg2 == SearchType.Depth_Search.value:
        s = DepthSearch()
    else:
        print('Choose a number from 1 to 5')
        s = None
    ss = SelectSearch(s)
    print(gb)
    start = time()
    report, game = ss.do_the_search(gb)
    end = time()
    if game is not None:
        print('Steps to result: {0}'.format(game.moves))
    else:
        print('Solution not found')
    print('Node: {0}'.format(report.get('node')))
    print('Repeat: {0}'.format(report.get('repeat')))
    print('Fringe: {0}'.format(report.get('fringe')))
    print('Deadlock: {0}'.format(report.get('deadlock')))
    print('O tempo total foi: {0} segundos'.format(end - start))


def main_2():
    df_report = pd.DataFrame(columns=['SearchType', 'Screen', 'Node', 'Repeat', 'Fringe', 'Deadlock', 'Time', 'Answer'])
    search_type_string = ''
    for i in range(10):  # Each map
        for search_type in range(1, 5):
            path = './screens//screen.{}'.format(i)  # First arg
            gb = load_map(path)
            if search_type == SearchType.A_Star_Search.value:
                s = AStarSearch()
                search_type_string = SearchType.A_Star_Search
            elif search_type == SearchType.Iterative_Depth_Search.value:
                s = IterativeDepthSearch()
                search_type_string = SearchType.Iterative_Depth_Search
            elif search_type == SearchType.Breadth_Search.value:
                s = BreadthSearch()
                search_type_string = SearchType.Breadth_Search
            elif search_type == SearchType.Depth_Search.value:
                s = DepthSearch()
                search_type_string = SearchType.Depth_Search
            else:
                print('Choose a number from 1 to 5')
                s = None
            ss = SelectSearch(s)
            start = time()
            report, game = ss.do_the_search(gb)
            end = time()
            if game is not None:
                df_report.loc[len(df_report)] = ([search_type_string, i, report.get('node'), report.get('repeat'),
                                                  report.get('fringe'), report.get('deadlock'), end - start,
                                                  game.moves])
            else:
                df_report.loc[len(df_report)] = ([search_type_string, i, report.get('node'), report.get('repeat'),
                                                  report.get('fringe'), report.get('deadlock'), end - start,
                                                  'solution not found'])
    df_report.to_csv('C://Users//felip//Desktop//report_sokoban.csv')


if __name__ == "__main__":
    main_2()
