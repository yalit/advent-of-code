import _ from "lodash"

function handleInput_1(lines: Array<string>){
    let grid = new Uint8Array(1000 * 1000);
    
    const actions: {[key: string]: (ind: number) => number} = {
        'toggle': (ind: number) => grid[ind] = grid[ind] === 0 ? 1 : 0,
        'turn on': (ind: number) => grid[ind] = 1,
        'turn off': (ind: number) => grid[ind] = 0
    }

    lines.forEach(line => {
        let d: InputData = getInputData(line)

        for (let i = d.from.x; i <= d.to.x; i++) {
            for (let j = d.from.y; j <= d.to.y; j++) {
                let ind = getIndex(i, j)
                actions[d.action](ind)
            }
        }
    });
    
    return grid.reduce((total, light) => light === 0 ? total : ++total, 0)
} 

function handleInput_2(lines: Array<string>){
    return 0
}

function getIndex(x: number, y: number) {
    return (x * 1000) + y
} 

interface Coord {
    x: number,
    y: number
}

function getPos(x: number, y: number): Coord {
    return {x, y}
}

interface InputData {
    action: string,
    from: Coord,
    to: Coord
}

function getInputData(line: string): InputData {
    const parsed = line.match(/^(toggle|turn on|turn off).(\d+),(\d+).*(\d+),(\d+)$/)
    
    return {
        action: parsed[1],
        from: getPos(Math.min(Number(parsed[2]),Number(parsed[4])), Math.min(Number(parsed[3]),Number(parsed[5]))),
        to: getPos(Math.max(Number(parsed[2]),Number(parsed[4])), Math.max(Number(parsed[3]),Number(parsed[5])))
    }
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}