const algebraicSum = (n: number) => {
    let sum = 1
    for (let i = 1; i < n; i++) {
        sum += i
    }
    return sum
}
function handleInput_1(lines: Array<string>){
    const row = 2978
    const col = 3083

    const index = algebraicSum(row + col - 1) + col - 1
    let code = 20151125
    for (let i = 1; i < index; i++) {
        code = (code * 252533) % 33554393
    }
    return code
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}