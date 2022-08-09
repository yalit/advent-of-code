import _ from "lodash"

type Actions =  {
    'toggle':  (value: number) => number,
    'turn on':  (value: number) => number
    'turn off':  (value: number) => number
}

function handleInput_1(lines: Array<string>){    
    const actions: Actions = {
        'toggle': (value: number) => value === 0 ? 1 : 0,
        'turn on': (value: number) => 1,
        'turn off': (value: number) => 0
    }

    return handle(lines, actions)
} 

function handleInput_2(lines: Array<string>){    
    const actions: Actions = {
        'toggle': (value: number) => value + 2,
        'turn on': (value: number) => value + 1,
        'turn off': (value: number) => (value > 0) ? value - 1 : 0
    }

    return handle(lines, actions)
}

function handle(lines: Array<string>, actions: Actions): number {
    let grid = new Uint8Array(1000 * 1000);

    lines.forEach(line => {
        let d: InputData = getInputData(line)
        
        for (let i = d.from.x; i <= d.to.x; i++) {
            for (let j = d.from.y; j <= d.to.y; j++) {
                let ind = getIndex(i, j)
                grid[ind] = actions[d.action](grid[ind])
            }
        }
    });
    
    return grid.reduce((total, light) => {
        return total+light
    }, 0)
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
    const parsed = line.match(/^(toggle|turn on|turn off).(\d+),(\d+).through.(\d{1,3}),(\d+)$/)

    return {
        action: parsed[1],
        from: getPos(Math.min(Number(parsed[2]),Number(parsed[4])), Math.min(Number(parsed[3]),Number(parsed[5]))),
        to: getPos(Math.max(Number(parsed[2]),Number(parsed[4])), Math.max(Number(parsed[3]),Number(parsed[5])))
    }
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}