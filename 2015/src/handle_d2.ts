function handleInput_1(lines: Array<string>){
    const sizes: Array<Array<number>> = getSizes(lines)

    return sizes.reduce((acc, s) => acc + getAreaSmallest(s) + getBoxArea(s), 0)
} 

function handleInput_2(lines: Array<string>){
    const sizes: Array<Array<number>> = getSizes(lines)

    return sizes.reduce((acc, s) => acc + getRibbonBowSize(s) + getRibbonWrapSize(s), 0)
}

function getSizes(lines: Array<string>) {
    return lines.map(d => d.split('x').map(e => Number(e)).sort((a,b) => a-b))
}

function getBoxArea(s: Array<number>) {
    return 2 * ( (s[0]*s[1]) + (s[0]*s[2]) + (s[2]*s[1]) )
}

function getAreaSmallest(s: Array<number>) {
    return (s[0]*s[1])
}

function getRibbonWrapSize(s: Array<number>) {
    return 2 * (s[0] + s[1])
}

function getRibbonBowSize(s: Array<number>) {
    return s[0]*s[1]*s[2]
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}