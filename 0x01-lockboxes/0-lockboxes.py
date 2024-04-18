#!/usr/bin/python3
"""this function determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """this is a method that determines if all the boxes can be opened
    boxes is a list of lists"""
    total = {0}
    visited = set()
    while total:
        box_index = total.pop()
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                total.add(key)
    return len(visited) == len(boxes)
