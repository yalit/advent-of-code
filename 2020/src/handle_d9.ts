function isValid(preamble: Array<number>, value: number): boolean {
    const checkSum = (l: Array<number>, v: number, a: number, b: number): boolean =>{
        if (a >= l.length) {
            return false
        }
        if (b >= l.length) {
            return checkSum(l, v, a+1, a+2)
        }
        if (l[a] + l[b] === v) {
            return true
        }
        if (l[a] + l[b] > v) {
            return checkSum(l, v, a+1, a+2)
        }
        return checkSum(l, v, a, b+1)
    }

    let l = [...preamble]
    l.sort((a,b) => a-b)
    return checkSum(l, value, 0, 1)
}

function handleInput_1(lines: Array<number>){
    const preambleLength = 25

    let i = 0
    let isValueValid = isValid(lines.slice(i,i+preambleLength), lines[i+preambleLength])
    while (isValueValid) {
        i++
        isValueValid = isValid(lines.slice(i,i+preambleLength), lines[i+preambleLength])
    }

    return lines[i+preambleLength]
}

function handleInput_2(lines: Array<number>){
    const targetValue = handleInput_1(lines)

    const sum = (l: Array<number>) : number => {
        return l.reduce((acc: number, n: number) => acc + n, 0)
    }

    let a = 0
    let b = 1
    let result = 0
    while (a < lines.length) {
        if (b >= lines.length) {
            a += 1
            b = a + 1
        } else if (sum(lines.slice(a, b)) === targetValue) {
            result = Math.min(...lines.slice(a, b)) + Math.max(...lines.slice(a, b))
            a = lines.length
        } else if (sum(lines.slice(a, b)) > targetValue) {
            a += 1
            b = a + 1
        }
        b +=1
    } 
    return result
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines.map(x => parseInt(x))), handleInput_2(lines.map(x => parseInt(x)))]
}