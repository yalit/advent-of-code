import _ from 'lodash';

/**
 * vertice : 
 * {from:{x: a, y: b}, to:{x: a, y: b}, direction: r | l | u | d | dld | drd | dlu | dru } (dld = diag. left down / r = right & u = up)
 */
let mapSize
let fullMap
let nbCrossOver

const actions = {
    l: coord => {return {x: coord.x - 1, y: coord.y}},
    r: coord => {return {x: coord.x + 1, y: coord.y}},
    u: coord => {return {x: coord.x, y: coord.y - 1}},
    d: coord => {return {x: coord.x, y: coord.y + 1}},
    dld: coord => {return {x: coord.x - 1, y: coord.y + 1}}, //x-1, y+1
    drd: coord => {return {x: coord.x + 1, y: coord.y + 1}}, //x+1, y+1
    dlu: coord => {return {x: coord.x - 1, y: coord.y - 1}}, //x-1, y-1
    dru: coord => {return {x: coord.x + 1, y: coord.y - 1}}, //x+1, y-1
}

function handleInput_1(lines, allVertices = false){
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

function getAllVerticesAndComputeMapSize(lines, allVertices = false) {
    let vertices = []

    const getCoordinates = (inputData) => {
        const d = inputData.split(',').map(e => parseInt(e))
        let data = {x: d[0], y:d[1]}
        return data
    }

    lines.forEach(line => {
        const d = line.split(' -> ')
        const vertice = {
            from: getCoordinates(d[0]),
            to: getCoordinates(d[1])
        }
        vertice.direction = getVerticeDirection(vertice)
        if (allVertices || vertice.from.x === vertice.to.x || vertice.from.y === vertice.to.y) {
            drawVertice(vertice)
        }
    });
    return vertices
}

function drawVertice(vertice) {
    const handleIndex = (index) => {
        if (! Object.keys(fullMap).includes(index)) fullMap[index] = 0
    
        fullMap[index] += 1
        computeCrossover(index)
    }

    //init 
    let coord = vertice.from
    handleIndex(getIndex(coord))

    while (!coordinatesEquals(coord, vertice.to)) {
        coord = actions[vertice.direction](coord)

        handleIndex(getIndex(coord))
        console.log(fullMap);
    }
}

function computeCrossover(index) {
    //compute crossOvers
    if (fullMap[index] === 2) {
        nbCrossOver += 1
    }
}

function getIndex(coord) {
    return (coord.x * 10000) + coord.y
}

function coordinatesEquals(v1, v2) {
    return v1.x == v2.x && v1.y == v2.y
}

function getVerticeDirection(v) {
    let diagonal = ''
    let horizontal = ''
    let vertical = ''
    if (v.from.x < v.to.x) horizontal = 'r'
    if (v.from.x > v.to.x) horizontal = 'l'
    if (v.from.y < v.to.y) vertical = 'd'
    if (v.from.y > v.to.y) vertical = 'u'
    if (v.from.x !== v.to.x && v.from.y !== v.to.y) diagonal = 'd'

    return diagonal+horizontal+vertical
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}