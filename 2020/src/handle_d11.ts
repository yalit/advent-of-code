import { countValuesInMatrix, createMatrix, getNeighborsWithValue, isChanged, Matrix, Point, UpdatePointCallback, updatePointsMatrix } from "./libraries/matrix"

type Seat = '.' | 'L' | '#'

type UpdateSeatCallback = UpdatePointCallback<Seat>

function handleSeats(lines: Array<Array<Seat>>, updateCallback: UpdateSeatCallback): number{
    let matrix: Matrix<Seat> = createMatrix(lines)     
    let i = 0
    while (i === 0 || isChanged(matrix)) {
        matrix = updatePointsMatrix(matrix, updateCallback)
        i++
    }
    return countValuesInMatrix(matrix, '#')
}

function getUpdateSeatsCallback(radius: number, minOccupiedNeighbors: number): UpdateSeatCallback {
    return (p: Point<Seat>, m: Matrix<Seat>): Point<Seat> => {
        const occupiedNeighbors: number = getNeighborsWithValue(p, m, ['#', 'L'], radius).filter(p => p.value === '#').length
        let newValue: Seat = p.value;
        if (p.value === '#' && occupiedNeighbors >= minOccupiedNeighbors) {
            newValue = 'L'
        }
        if (p.value === 'L' && occupiedNeighbors === 0) {
            newValue = '#'
        }
        
        return {
            ...p,
            value: newValue,
            changed: p.value !== newValue
        }
    }
}

function handleInput_1(lines: Array<Array<Seat>>){
    return handleSeats(lines, getUpdateSeatsCallback(1, 4))
}

function handleInput_2(lines: Array<Array<Seat>>){
    return handleSeats(lines, getUpdateSeatsCallback(Math.max(lines.length, lines[0].length), 5))
}


export function handleInput(lines: Array<string>) {
    const data = lines.map(l => l.split('') as Array<Seat>)
    return [handleInput_1(data), handleInput_2(data)]
}