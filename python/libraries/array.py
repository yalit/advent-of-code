from functools import reduce

import numpy as np

def inbound(r,c,h,w, min_h = 0, min_w = 0):
    return min_h <= r < h and min_w <= c < w

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
    for r in arr:
        if np.isscalar(r):
            print(r)
        else:
            print("".join(r))
