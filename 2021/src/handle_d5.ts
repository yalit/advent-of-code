import _ from 'lodash';

/**
 * vertice : 
 * {from:{x: a, y: b}, to:{x: a, y: b}, direction: r | l | u | d | dld | drd | dlu | dru } (dld = diag. left down / r = right & u = up)
 */
interface Coord {
    x: number,
    y: number
}


interface Vertice {
    from: Coord,
    to: Coord,
    direction: string
}

let fullMap
let nbCrossOver

const actions = {
    l: (coord: Coord) => {return {x: coord.x - 1, y: coord.y}},
    r: (coord: Coord) => {return {x: coord.x + 1, y: coord.y}},
    u: (coord: Coord) => {return {x: coord.x, y: coord.y - 1}},
    d: (coord: Coord) => {return {x: coord.x, y: coord.y + 1}},
    dld: (coord: Coord) => {return {x: coord.x - 1, y: coord.y + 1}}, //x-1, y+1
    drd: (coord: Coord) => {return {x: coord.x + 1, y: coord.y + 1}}, //x+1, y+1
    dlu: (coord: Coord) => {return {x: coord.x - 1, y: coord.y - 1}}, //x-1, y-1
    dru: (coord: Coord) => {return {x: coord.x + 1, y: coord.y - 1}}, //x+1, y-1
}

function handleInput_1(lines: Array<string>, allVertices: boolean = false){
    fullMap = {}
    nbCrossOver = 0

    const vertices = getAllVerticesAndComputeMapSize(lines, allVertices)
    
    vertices.forEach(vertice => {
        drawVertice(vertice)
    });
    
    return nbCrossOver;
}

function handleInput_2(lines) {
    return handleInput_1(lines, true)
}

function getAllVerticesAndComputeMapSize(lines: Array<string>, allVertices: boolean = false): Array<Vertice> {
    let vertices = []

    const getCoordinates = (inputData: string): Coord => {
        const d: Array<number> = inputData.split(',').map(e => parseInt(e))
        let data = {x: d[0], y: d[1]}
        return data
    }

    lines.forEach(line => {
        const d = line.split(' -> ')
        const vertice: Vertice = {
            from: getCoordinates(d[0]),
            to: getCoordinates(d[1]),
            direction: getVerticeDirection(getCoordinates(d[0]), getCoordinates(d[1]))
        }

        if (allVertices || vertice.from.x === vertice.to.x || vertice.from.y === vertice.to.y) {
            drawVertice(vertice)
        }
    });
    return vertices
}

function drawVertice(vertice: Vertice): void {
    const handleIndex = (index) => {
        fullMap[index] = fullMap[index] ?  fullMap[index] + 1 : 1
        computeCrossover(index)
    }

    //init 
    let coord = vertice.from
    handleIndex(getIndex(coord))

    while (!coordinatesEquals(coord, vertice.to)) {
        coord = actions[vertice.direction](coord)
        handleIndex(getIndex(coord))
    }
}

function computeCrossover(index: number) {
    //compute crossOvers
    if (fullMap[index] === 2) {
        nbCrossOver += 1
    }
}

function getIndex(coord: Coord): number {
    return (coord.x * 10000) + coord.y
}

function coordinatesEquals(c1: Coord, c2: Coord): boolean {
    return c1.x == c2.x && c1.y == c2.y
}

function getVerticeDirection(from: Coord, to: Coord): string {
    let diagonal = ''
    let horizontal = ''
    let vertical = ''

    if (from.x > to.x) horizontal = 'l'
    if (from.x < to.x) horizontal = 'r'
    if (from.y < to.y) vertical = 'd'
    if (from.y > to.y) vertical = 'u'
    if (from.x !== to.x && from.y !== to.y) diagonal = 'd'

    return diagonal+horizontal+vertical
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}