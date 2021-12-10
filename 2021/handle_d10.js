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

function handleInput_1(lines){
    return lines.reduce((errors, line) => {
        const error = findCorruptorOrIncomplete(line.split(''))
        if (!Array.isArray(error)) return errors + errorCost[error]
        return errors
    }, 0)
}

function handleInput_2(lines){
    const incomplete = lines.map(line => findCorruptorOrIncomplete(line)).filter(l => Array.isArray(findCorruptorOrIncomplete(l)))
    
    console.log(incomplete)

    const incompleteCosts =  incomplete
        .map(incomplete => {
            return incomplete.reverse().reduce((score, c) => (score * 5) + incompleteCost[toClose[c]], 0)
        })
        .sort((a, b) => a-b)
        
    return incompleteCosts[Math.floor(incomplete.length / 2)]
}

function findCorruptorOrIncomplete(line) {
    let opened = []

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

    return opened
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}