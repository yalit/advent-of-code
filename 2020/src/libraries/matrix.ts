import _ from 'lodash'

export interface Coordinate {
    x: number,
    y: number
}

export interface Point<T> {
    coordinate: Coordinate,
    value: T,
    changed: boolean
}

export interface MatrixColumn<T> {
    [k: number]: Point<T>
}

export interface Matrix<T>  {
    [k: number]: MatrixColumn<T>,
    width: number,
    height: number
}

export type UpdatePointCallback<T> = (point: Point<T>, matrix: Matrix<T>) => Point<T>

export function createMatrix<T>(lines: Array<Array<T>>): Matrix<T> {
    const width = lines[0].length
    const height = lines.length
    let matrix: Matrix<T> = {width, height}
    lines.forEach((line: Array<T>, y: number) => {
        line.forEach((elem: T, x: number) => {
            if (!(x in matrix)){
                matrix[x] = {}
            }
            matrix[x][y] = {
                coordinate: {x, y},
                value: elem,
                changed: false
            }
        })
    })

    return matrix
}

export function isInside<T>(matrix: Matrix<T>, coordinate: Coordinate): boolean {
    return coordinate.x >=0 && coordinate.x < matrix.width && coordinate.y >= 0 && coordinate.y < matrix.height 
}

export function isChanged<T>(matrix: Matrix<T>): boolean {
    let nbChanged: number = 0

    Object.keys(matrix).forEach((x: string): void => {
        Object.keys(matrix[x]).forEach((y: string) => {
            nbChanged += matrix[x][y].changed ? 1 : 0
        })
    })

    return nbChanged > 0
}

export function getNeighbors<T>(point: Point<T>, matrix: Matrix<T>, value: T, radius: number = 1): Array<Point<T>> {
    const directions = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
    const findFirstSeat = (tp: Point<T>, tm: Matrix<T>, direction: Array<number>): Point<T> => {
        let foundPoint: Point<T>
        let outside: boolean = false
        let i = 1;
        while (foundPoint === undefined && !outside && i <= radius) {
            const newX = tp.coordinate.x + (i*direction[0])
            const newY = tp.coordinate.y + (i*direction[1])
            if (!isInside(tm, {x: newX, y: newY})) {
                outside = true;
                continue
            }

            if (tm[newX][newY].value === value) {
                foundPoint = tm[tp.coordinate.x + (i*direction[0])][tp.coordinate.y + (i*direction[1])]
            }
            i++
        }
        return foundPoint ?? null
    }

    return directions.map((dir) => findFirstSeat(point, matrix, dir)).filter(p => p !== null)
}

export function updatePointsMatrix<T>(matrix: Matrix<T>, callback: UpdatePointCallback<T>): Matrix<T> {
    let newMatrix: Matrix<T> = {width: matrix.width, height: matrix.height}
    Object.keys(matrix).forEach((x: string): void => {
        Object.keys(matrix[x]).forEach((y: string) => {
            if (!(x in newMatrix)) {
                newMatrix[x] = {}
            }
            newMatrix[x][y] = callback(matrix[x][y], matrix)
        })
    })

    return newMatrix
}

export function countValuesInMatrix<T>(matrix: Matrix<T>, value: T): number {
    let nbValues: number = 0

    Object.keys(matrix).forEach((x: string): void => {
        Object.keys(matrix[x]).forEach((y: string) => {
            nbValues += matrix[x][y].value === value ? 1 : 0
        })
    })

    return nbValues
}
