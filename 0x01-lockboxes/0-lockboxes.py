#!/usr/bin/python3
"""this function determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """this is a method that determines if all the boxes can be opened
    boxes is a list of lists"""
    def explore(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                explore(key)

    visited = set()
    explore(0)
    return len(visited) == len(boxes)
