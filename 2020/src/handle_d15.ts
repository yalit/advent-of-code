function getLastSpoken(line: string, nbTurns: number): number {
    let spoken: {[k: number]: [number?, number?]} = line.split(',').reduce((s: {}, a: string, idx: number) => {
        let ts = {...s}
        ts[a] = [idx + 1]
        return ts
    }, {})

    let turn = Object.keys(spoken).length + 1
    let lastSpoken = parseInt(line.slice(-1))
    
    while (turn <= nbTurns) {
        if (spoken[lastSpoken].length <= 1) { //not spoken before
            lastSpoken = 0
        } else { //spoken before
            lastSpoken = spoken[lastSpoken][1] - spoken[lastSpoken][0]
        }

        if (!(lastSpoken in spoken)) {
            spoken[lastSpoken] = []
        } else if (spoken[lastSpoken].length > 1) {
            spoken[lastSpoken] = [spoken[lastSpoken][1]]
        }
        spoken[lastSpoken].push(turn)
        turn++
    }

    return lastSpoken
}

function handleInput_1(lines: Array<string>){
    return getLastSpoken(lines[0], 2020)
}

function handleInput_2(lines: Array<string>){
    return getLastSpoken(lines[0], 30000000)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}