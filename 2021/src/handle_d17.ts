import {_} from 'lodash'

function sumN(n: number): number {
    return (n*(n+1))/2
}

type findType = 'min' | 'max'

function getNForD(d: number): number {
    let x = 1

    while (sumN(x) < d) {
        x++
    }

    
    return (sumN(x) === d) ? x : x - 1
}

function getRawNForD(d: number): number {
    return Math.sqrt(1+ (2 * d)) - 1
}

function getMaxDistanceY(y: number, lowY: number): number {
    return sumN(y) - lowY
}

function parseLine(line: string): Array<number> {
    const n = line.match(/([?-\d]+)/g)
    
    return n.map(c => Number(c))
}

function searchY(x: number, highY: number, lowY: number): number {
    let y = x - 1
    let nMinY: number = 0

    while (sumN(nMinY + 1) <= getMaxDistanceY(y, lowY)) {
        y++
        nMinY = getNForD(getMaxDistanceY(y, highY))
    }

    return y - 1
}

function handleInput_1(lines: Array<string>){
    const [aX, bX, aY, bY]: Array<number> = parseLine(lines[0])
    const minX = Math.min(aX, bX)
    const maxX = Math.max(aX, bX)
    const highY = Math.max(aY, bY)
    const lowY = Math.min(aY, bY)

    const x = Math.min(getNForD(minX) + 1, getNForD(maxX))
    
    return searchY(x, highY, lowY)
    //return _.range(15).map(n => sumN(n))
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}
