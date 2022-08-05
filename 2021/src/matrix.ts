import internal = require("stream");

export type Matrix = Array<Array<string>>
export type borderSide = 'top' | 'bottom' | 'left' | 'right'

type matrixMapCallbackFunction = (value: string, x: number, y : number, matrix: Matrix) => string

// apply a callback function to each of the element of the matrix
export function matrixMap(matrix: Matrix, fn: matrixMapCallbackFunction): Matrix {
    const newMatrix = matrix.map((line: Array<string>, matrixY: number) => {
        return line.map((elem: string, matrixX: number) => {
            return fn(elem, matrixX, matrixY, matrix)
        })
    })

    return newMatrix
}


export function getMatrixBorders(matrix: Matrix, borders: Array<borderSide> = ['top', 'bottom', 'left', 'right']): Array<string> {
    let borderValues: Array<string> = []

    const borderDataFunctions = {
        'top': (matrix: Matrix) => matrix[0],
        'bottom': (matrix: Matrix) => matrix[matrix.length - 1],
        'left': (matrix: Matrix) => matrix.map((line: Array<string>) => line[0]),
        'right': (matrix: Matrix) => matrix.map((line: Array<string>) => line[line.length - 1])
    }

    borders.forEach((border: borderSide) => {
        borderValues = borderValues.concat(borderDataFunctions[border](matrix))
    })

    return borderValues
}