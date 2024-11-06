import { isText } from "./libraries/types"

const findClosingParentheses = (line: string, index: number): number => {
    let counter = 1
    while (counter > 0) {
        index++
        if (line[index] == '(') {
            counter++
        } else if (line[index] == ')') {
            counter--
        }
    }
    return index
}

const getOperationResult = (left: number, right: number, operator: string) => {
    if (operator == '+') {
        return left + right
    } else {
        return left * right
    }
}

const getResult = (input: string): number => {
    let result = 0
    let i = 0
    let operator = '+'

    while (i < input.length) {
        const char = input[i]
        if (char == ' ') {
            i++
            continue
        }

        if (char == '(') {
            const closingIndex = findClosingParentheses(input, i)
            result = getOperationResult(result, getResult(input.substring(i + 1, closingIndex)), operator)
            i = closingIndex + 1
            continue
        }
        if (char == '+' || char == '*') {
            operator = char
        } else {
            result = getOperationResult(result, parseInt(char), operator)
        }
        i++
    }
    return result
}

const getResult_2 = (input: string): number => {
    let values = [0]
    let i = 0
    let operator = '+'

    while (i < input.length) {
        const char = input[i]
        if (char == ' ') {
            i++
            continue
        }

        if (char == '(') {
            const closingIndex = findClosingParentheses(input, i)
            const intermediateResult = getResult_2(input.substring(i + 1, closingIndex))
            if (operator == '+') {
                values[values.length - 1] += intermediateResult
            } else {
                values.push(intermediateResult)
            }
            i = closingIndex + 1
            continue
        }
        if (char == '+' || char == '*') {
            operator = char
        } else {
            if (operator == '+') {
                values[values.length - 1] += parseInt(char)
            } else {
                values.push(parseInt(char))
            }
        }
        i++
    }

    return values.reduce((acc, val) => acc * val, 1)
}

function handleInput_1(lines: Array<string>){
    let sum = 0

    lines.forEach(line => {
        sum += getResult(line)
    })
    return sum
}

function handleInput_2(lines: Array<string>){
    let sum = 0
    lines.forEach(line => {
        sum += getResult_2(line)
    })
    return sum
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}