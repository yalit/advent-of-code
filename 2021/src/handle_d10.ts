const errorCost = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

const incompleteCost = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

const open = ['[','{','<','(']
const close = {']': '[', '}': '{', '>': '<', ')': '('}
const toClose = {'[': ']', '{': '}', '<': '>', '(': ')'}
const closeKeys = Object.keys(close)

function handleInput_1(lines: Array<string>){
    return lines.reduce((errors, line) => {
        const error = findCorruptor(line.split(''))
        if (error !== null) return errors + errorCost[error]
        return errors
    }, 0)
}

function handleInput_2(lines: Array<string>){
    const incomplete = lines.map(line => findIncomplete(line.split(''))).filter(l => findIncomplete(l).length > 0)

    const incompleteCosts = incomplete
        .map(incomplete => {
            return incomplete.reverse().reduce((score, c) => (score * 5) + incompleteCost[toClose[c]], 0)
        })
        .sort((a, b) => a-b)
        
    return incompleteCosts[Math.floor(incomplete.length / 2)]
}

function findCorruptor(line: Array<string>): string | null {
    let opened: Array<string> = []
    for (let i = 0; i < line.length; i++) {
        let c = line[i]
        if (open.includes(c)){
            opened.push(c)
            continue
        }

        if (closeKeys.includes(c) && close[c] !== opened.pop()) {
            return c
        }
    }

    return null
}

function findIncomplete(line: Array<string>): Array<string> {
    let opened = []

    for (let i = 0; i < line.length; i++) {
        let c = line[i]
        if (open.includes(c)){
            opened.push(c)
            continue
        }

        if (closeKeys.includes(c) && close[c] !== opened.pop()) {
            return []
        }
    }

    return opened
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}