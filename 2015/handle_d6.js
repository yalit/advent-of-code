import _ from "lodash"

function handleInput_1(lines){
    let grid = new Uint8Array(1000 * 1000);
    
    const actions = {
        'toggle': ind => grid[ind] = grid[ind] === 0 ? 1 : 0,
        'turn on': ind => grid[ind] = 1,
        'turn off': ind => grid[ind] = 0
    }

    lines.forEach(line => {
        let d = getInputData(line)

        for (let i = d.from.x; i <= d.to.x; i++) {
            for (let j = d.from.y; j <= d.to.y; j++) {
                let ind = getIndex(i, j)
                actions[d.action](ind)
            }
        }
    });
    
    return grid.reduce((total, light) => light === 0 ? total : ++total, 0)
} 

function handleInput_2(lines){
    return 0
}

function getIndex(x, y) {
    return (x*1000) + y
} 

function getPos(x, y) {
    return {x, y}
}

function getInputData(line) {
    const parsed = line.match(/^(toggle|turn on|turn off).(\d+),(\d+).*(\d+),(\d+)$/)
    
    return {
        action: parsed[1],
        from: getPos(Math.min(parsed[2],parsed[4]), Math.min(parsed[3],parsed[5])),
        to: getPos(Math.max(parsed[2],parsed[4]), Math.max(parsed[3],parsed[5]))
    }
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}