function handleInput_1(lines: Array<string>){
    return lines.map(l => (new Set(l.replaceAll(' ', '').split('')).size)).reduce((sum, n) => sum + n, 0)
}

function handleInput_2(lines: Array<string>){
    return lines.map(group => {
        return group
                .split(' ')
                .map(person => person.split(''))
                .reduce((intersect, p) => intersect.filter(n => p.includes(n)))
                .length
    }).reduce((sum, n) => sum + n, 0)
}


export function handleInput(lines: Array<string>) {
    const data = lines.join(' ').split('  ')
    return [handleInput_1(data), handleInput_2(data)]
}