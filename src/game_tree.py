from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]

def sample_tree() -> GameTree:
    """Expected result: 5"""
    return [
        [5, 6],
        [2, 9],
    ]

def medium_tree() -> GameTree:
    """Expected result: 6"""
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[6, 4], [8, 6]],
    ]

def ordered_tree_for_pruning() -> GameTree:
    """Expected result: 10"""
    return [
        [[10, 10], [10, 10]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]