function parseString(s: string): number {
    const hexa = /(\\x)/g
    const doublequotes = /(\\\")/g
    const doubleback = /(\\\\)/g
    
    const hexaNb = s.match(hexa) ?? []
    const dbQuotesNb = s.match(doublequotes) ?? []
    const dbBackslashNb = s.match(doubleback) ?? []
    
    return dbQuotesNb.length + dbBackslashNb.length + (3 * hexaNb.length) + 2
}

function handleInput_1(lines: Array<string>){
    return lines.map(parseString).reduce((s: number, x:number) => s+x,0)
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}