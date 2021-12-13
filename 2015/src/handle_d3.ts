const dir: {[key: string]: (coord: Coord) => Coord} = {
    'v': (pos: Coord) => ({x: pos.x, y: pos.y-1}),
    '>': (pos: Coord) => ({x: pos.x+1, y: pos.y}),
    '^': (pos: Coord) => ({x: pos.x, y: pos.y+1}),
    '<': (pos: Coord) => ({x: pos.x-1, y: pos.y})
}

interface Coord {
    x: number,
    y: number
}

function handleInput_1(lines: Array<string>){
    const directions: Array<string> = lines[0].split('')
    let currentPos: Coord = {x: 0, y:0}
    let visitedHouses = [getPositionIndex(currentPos)]
    
    directions.forEach(d => {
        currentPos = dir[d](currentPos)
        if (! visitedHouses.includes(getPositionIndex(currentPos))) visitedHouses.push(getPositionIndex(currentPos))
    });

    return visitedHouses.length
} 

function handleInput_2(lines: Array<string>){
    const directions: Array<string> = lines[0].split('')
    let currentPos: {[key: number]: Coord} = {0: {x: 0, y:0}, 1: {x: 0, y:0}}
    let visitedHouses: {[key: number]: Array<number>} = {0: [getPositionIndex(currentPos[0])], 1: []}
    
    directions.forEach((d, turn) => {
        let who = turn % 2

        currentPos[who] = dir[d](currentPos[who])
        if (! (visitedHouses[0].includes(getPositionIndex(currentPos[who])) || visitedHouses[1].includes(getPositionIndex(currentPos[who])))) {
            visitedHouses[who].push(getPositionIndex(currentPos[who]))
        }
    });

    return visitedHouses[0].length + visitedHouses[1].length
}

function getPositionIndex(position: Coord) {
    return (position.x * 10000) + position.y
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}