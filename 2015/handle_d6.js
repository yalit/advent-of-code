import _ from "lodash"

function handleInput_1(lines){
    let grid = _.range(0,1000*1000).map(n => false)
    
    const actions = {
        'toggle': n => !n,
        'turn on': n => true,
        'turn off': n => false
    }

    lines.forEach(line => {
        let d = getInputData(line)

        for (let i = d.from.x; i <= d.to.x; i++) {
            for (let j = d.from.y; j <= d.to.y; j++) {
                let ind = getIndex(i, j)
                grid[ind] = actions[d.action](grid[ind])
            }
        }
    });
    
    return grid.filter(n => n).length
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