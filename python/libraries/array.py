from functools import reduce

import numpy as np

def inbound(r,c,h,w):
    return 0 <= r < h and 0 <= c < w

def product(arr):
    return reduce(lambda p, x: p * x, arr, 1)

# Creates windows of a given length from an array.
# Ex: ([1, 2, 3, 4], 2) = > ([[1, 2], [2, 3], [3, 4]])
def windows(arr, n):
    return [arr[x, x + n] for x in arr[:-n + 1]]

# transpose a row matrix into columns
def transpose(matrix):
    return list(map(list, zip(*matrix)))

def visualize(arr: list):
    if len(arr) == 0:
        print()
        return

    if np.isscalar(arr[0]):
        print(*arr)
        return

    for elem in arr:
        visualize(elem)
