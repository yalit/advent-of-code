import numpy as np

# export const transpose = (matrix) => {
#     let [row] = matrix
#     return row.map((_, column) => matrix.map(row => row[column]))
# }

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
