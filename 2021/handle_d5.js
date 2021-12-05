import _ from 'lodash';

/**
 * vertice : 
 * {from:{x: a, y: b}, to:{x: a, y: b}}
 */
let mapSize = 0;
let map = [];

const actions = {
    left: pos => pos -= mapSize,
    right: pos => pos += mapSize,
    up: pos => pos -= 1,
    down: pos => pos += 1,
}

function handleInput_1(lines){
    const vertices = getAllVerticesAndComputeMapSize(lines) 
    map = _.range(0, mapSize*mapSize).map(n => 0)

    vertices.forEach(vertice => {
        drawVertice(vertice)
    });

    return map.filter(e => e > 1).length;
}

function drawVertice(vertice) {
    const direction = getVerticeDirection(vertice)
    const indexTo = getCoordinateIndex(vertice.to)
    
    //init 
    let index = getCoordinateIndex(vertice.from)
    map[index] += 1

    while (index !== indexTo) {
        index = actions[direction](index)
        map[index] += 1
    }
}

function getCoordinateIndex(coordinate) {
    return (coordinate.x * mapSize) + coordinate.y 
}

function getVerticeDirection(v) {
    if (v.from.x < v.to.x) return 'right'
    if (v.from.x > v.to.x) return 'left'
    if (v.from.y < v.to.y) return 'down'
    if (v.from.y > v.to.y) return 'up'

    return 'same'
}

function getAllVerticesAndComputeMapSize(lines, allVertices = false) {
    let vertices = []

    const getCoordinates = (inputData) => {
        const d = inputData.split(',').map(e => parseInt(e))
        if (d[0] > mapSize) mapSize = d[0] //define mapSize
        if (d[1] > mapSize) mapSize = d[1] //define mapSize
    
        return {x: d[0], y:d[1]}
    }

    lines.forEach(line => {
        const d = line.split(' -> ')
        const vertice = {
            from: getCoordinates(d[0]),
            to: getCoordinates(d[1])
        }
        if (allVertices || vertice.from.x === vertice.to.x || vertice.from.y === vertice.to.y) {
            vertices.push(vertice)
        }
    });
    return vertices
}

export function handleInput(lines) {
    return [handleInput_1(lines)]
}