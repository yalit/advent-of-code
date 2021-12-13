const dir = {
    'v': pos => ({x: pos.x, y: pos.y-1}),
    '>': pos => ({x: pos.x+1, y: pos.y}),
    '^': pos => ({x: pos.x, y: pos.y+1}),
    '<': pos => ({x: pos.x-1, y: pos.y})
}

function handleInput_1(lines){
    const directions = lines[0].split('')
    let currentPos = {x: 0, y:0}
    let visitedHouses = [getPositionIndex(currentPos)]
    
    directions.forEach(d => {
        currentPos = dir[d](currentPos)
        if (! visitedHouses.includes(getPositionIndex(currentPos))) visitedHouses.push(getPositionIndex(currentPos))
    });

    return visitedHouses.length
} 

function handleInput_2(lines){
    const directions = lines[0].split('')
    let currentPos = {0: {x: 0, y:0}, 1: {x: 0, y:0}}
    let visitedHouses = {0: [getPositionIndex(currentPos[0])], 1: []}
    
    directions.forEach((d, turn) => {
        let who = turn % 2

        currentPos[who] = dir[d](currentPos[who])
        if (! (visitedHouses[0].includes(getPositionIndex(currentPos[who])) || visitedHouses[1].includes(getPositionIndex(currentPos[who])))) {
            visitedHouses[who].push(getPositionIndex(currentPos[who]))
        }
    });

    return visitedHouses[0].length + visitedHouses[1].length
}

function getPositionIndex(position) {
    return (position.x * 10000) + position.y
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}