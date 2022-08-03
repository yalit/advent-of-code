import { count } from "console"

type Position = {
    x: number,
    y: number
}

type Positions = {
    'east': Array<Position>,
    'south': Array<Position>
}

type Direction = 'east' | 'south'
type Matrix = Array<Array<string>>

const directionSigns = {
    'east': '>',
    'south': 'v'
}

let width = 0
let height = 0
let matrix: Matrix
let moved: Positions = {'east': [], 'south': []}
let positions: Positions = {'east': [], 'south': []}
let newPositions: Positions = {'east': [], 'south': []}

function handleInput_1(lines: Array<string>): number {
    setMatrixAndSetBoardSizes(lines)
    
    let steps = 1
    
    movePositionOneDirection('east')
    movePositionOneDirection('south')

    while (moved.east.length + moved.south.length > 0) {
        steps+=1
        console.log("Steps : " + steps)
        
        positions = newPositions
        moved = {'east': [], 'south': []}
        newPositions = {'east': [], 'south': []}
        movePositionOneDirection('east')
        movePositionOneDirection('south')
    }

    return steps
}

function handleInput_2(lines: Array<string>): number {
    return 0
}

//return the number of elements that could move
function movePositionOneDirection(direction: Direction): void
{     
    //get the new positions
    positions[direction].forEach((position: Position) => {
        const nextPosition = getNextPos(position, direction)
        if (isPositionReachable(nextPosition)) {
            moved[direction].push(position)
            newPositions[direction].push(nextPosition)
        } else {
            newPositions[direction].push(position)
        }
    });

    //update the matrix
    moved[direction].forEach((position: Position) => {
        matrix[position.y][position.x] = '.'
        const nextPosition = getNextPos(position, direction)
        matrix[nextPosition.y][nextPosition.x] = directionSigns[direction]
    })
}

function setMatrixAndSetBoardSizes(lines: Array<string>): void {
    matrix = lines.map(line => line.split(''));
    height = matrix.length
    width = matrix[0].length

    for (let y = 0; y < matrix.length; y++) {
        for (let x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] === '>') {
                positions.east.push({'x': x, 'y': y})
            } if (matrix[y][x] === 'v') {
                positions.south.push({'x': x, 'y': y})
            }
        }
    }
}

function getNextPos(position: Position, direction: Direction): Position {
    return {
        'x': (direction === 'east') ? (position.x + 1) % width : position.x,
        'y': (direction === 'south') ? (position.y + 1) % height : position.y,
    }
}

function isPositionReachable(position: Position): boolean {
    return matrix[position.y][position.x] === '.'
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}