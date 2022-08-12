function lookAndSay(s: string): string {
    let i = 1
    let currentNumber: number = 1
    let current: string = s[0]
    let lookAndSayString: string = ''

    while (i < s.length) {
        let nextChar = s[i]
        if (current !== nextChar) {
            lookAndSayString += `${currentNumber}${current}`
            currentNumber = 1
            current = nextChar
        } else {
            currentNumber++
        }
        i++
    }
    lookAndSayString += `${currentNumber}${current}`

    return lookAndSayString
}

function algorithm(n: number, s: string): string {
    let i = 0
    while (i < n) {
        s = lookAndSay(s)
        i++
    }

    return s
}

function handleInput_1(s: string){
    return algorithm(40, s).length
}

function handleInput_2(s: string){
    return algorithm(50, s).length
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines[0]), handleInput_2(lines[0])]
}