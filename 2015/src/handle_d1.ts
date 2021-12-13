function handleInput_1(lines: Array<string>){
    return lines[0].split('').reduce((a,n) => {
        if (n === '(') return a+1
        if (n === ')') return a-1
    },0)
} 

function handleInput_2(lines: Array<string>){
    const dir = lines[0].split('')
    let position = 0
    let floor = 0
    
    while (floor !== -1) {
        if (dir[position] === '(') floor += 1
        if (dir[position] === ')') floor -=1
        position++
    }

    return position
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}