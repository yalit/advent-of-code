function handleInput_1(lines){
    const sizes = getSizes(lines)

    return sizes.reduce((acc, s) => acc + getAreaSmallest(s) + getBoxArea(s), 0)
} 

function handleInput_2(lines){
    const sizes = getSizes(lines)

    return sizes.reduce((acc, s) => acc + getRibbonBowSize(s) + getRibbonWrapSize(s), 0)
}

function getSizes(lines) {
    return lines.map(d => d.split('x').map(e => Number(e)).sort((a,b) => a-b))
}

function getBoxArea(s) {
    return 2 * ( (s[0]*s[1]) + (s[0]*s[2]) + (s[2]*s[1]) )
}

function getAreaSmallest(s) {
    return (s[0]*s[1])
}

function getRibbonWrapSize(s) {
    return 2 * (s[0] + s[1])
}

function getRibbonBowSize(s) {
    return s[0]*s[1]*s[2]
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}