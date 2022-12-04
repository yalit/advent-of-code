import { arraySum } from "./libraries/array"
import { Coordinate, countValuesInMatrix, createMatrix, getNeighbors, isInside, Matrix, Point, updatePointsMatrix } from "./libraries/matrix"

type Seat = '.' | 'L' | '#'

function handleInput_1(lines: Array<Array<Seat>>){
    let matrix: Matrix<Seat> = createMatrix(lines) 
    let nbChanges: number
    while (nbChanges === undefined || nbChanges !== 0) {
        nbChanges = 0
        matrix = updatePointsMatrix(matrix, (p: Point<Seat>, m: Matrix<Seat>) => {
            const occupiedNeighbors: number = getNeighbors(p, m, '#').length
            let newValue: Seat = p.value;
            if (p.value === '#' && occupiedNeighbors >= 4) {
                newValue = 'L'
                nbChanges++
            }
            if (p.value === 'L' && occupiedNeighbors === 0) {
                newValue = '#'
                nbChanges++
            }
            
            return {
                ...p,
                value: newValue
            }
        })
    }

    return countValuesInMatrix(matrix, '#')
}

function handleInput_2(lines: Array<Array<Seat>>){
    let matrix: Matrix<Seat> = createMatrix(lines) 
    let nbChanges: number
    while (nbChanges === undefined || nbChanges !== 0) {
        nbChanges = 0
        matrix = updatePointsMatrix(matrix, (p: Point<Seat>, m: Matrix<Seat>) => {
            // 8 directions
            const directions = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
            const findFirstSeat = (tp: Point<Seat>, tm: Matrix<Seat>, direction: Array<number>): Point<Seat> => {
                let foundPoint: Point<Seat>
                let outside: boolean = false
                let i = 1;
                while (foundPoint === undefined && !outside) {
                    const newX = tp.coordinate.x + (i*direction[0])
                    const newY = tp.coordinate.y + (i*direction[1])
                    if (!isInside(tm, {x: newX, y: newY})) {
                        outside = true;
                        continue
                    }

                    if (tm[newX][newY].value !== '.') {
                        foundPoint = tm[tp.coordinate.x + (i*direction[0])][tp.coordinate.y + (i*direction[1])]
                    }
                    i++
                }
                return foundPoint ?? null
            }

            const nbSeatsAround: number = directions.map(dir => findFirstSeat(p, m, dir)).filter((p: Point<Seat>) => p?.value === '#').length
            
            let newValue: Seat = p.value;
            if (p.value === '#' && nbSeatsAround >= 5) {
                newValue = 'L'
                nbChanges++
            }
            if (p.value === 'L' && nbSeatsAround === 0) {
                newValue = '#'
                nbChanges++
            }
            
            return {
                ...p,
                value: newValue
            }

        })
    }

    return countValuesInMatrix(matrix, '#')
}


export function handleInput(lines: Array<string>) {
    const data = lines.map(l => l.split('') as Array<Seat>)
    return [handleInput_1(data), handleInput_2(data)]
}