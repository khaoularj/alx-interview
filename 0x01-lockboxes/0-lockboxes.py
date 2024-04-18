#!/usr/bin/python3
"""this function determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """this is a method that determines if all the boxes can be opened
    boxes is a list of lists"""
    def dfs(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                dfs(key)

    visited = set()
    dfs(0)
    return len(visited) == len(boxes)