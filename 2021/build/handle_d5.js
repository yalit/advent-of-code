"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
let fullMap;
let nbCrossOver;
const actions = {
    l: (coord) => { return { x: coord.x - 1, y: coord.y }; },
    r: (coord) => { return { x: coord.x + 1, y: coord.y }; },
    u: (coord) => { return { x: coord.x, y: coord.y - 1 }; },
    d: (coord) => { return { x: coord.x, y: coord.y + 1 }; },
    dld: (coord) => { return { x: coord.x - 1, y: coord.y + 1 }; },
    drd: (coord) => { return { x: coord.x + 1, y: coord.y + 1 }; },
    dlu: (coord) => { return { x: coord.x - 1, y: coord.y - 1 }; },
    dru: (coord) => { return { x: coord.x + 1, y: coord.y - 1 }; }, //x+1, y-1
};
function handleInput_1(lines, allVertices = false) {
    fullMap = {};
    nbCrossOver = 0;
    const vertices = getAllVerticesAndComputeMapSize(lines, allVertices);
    vertices.forEach(vertice => {
        drawVertice(vertice);
    });
    return nbCrossOver;
}
function handleInput_2(lines) {
    return handleInput_1(lines, true);
}
function getAllVerticesAndComputeMapSize(lines, allVertices = false) {
    let vertices = [];
    const getCoordinates = (inputData) => {
        const d = inputData.split(',').map(e => parseInt(e));
        let data = { x: d[0], y: d[1] };
        return data;
    };
    lines.forEach(line => {
        const d = line.split(' -> ');
        const vertice = {
            from: getCoordinates(d[0]),
            to: getCoordinates(d[1]),
            direction: getVerticeDirection(getCoordinates(d[0]), getCoordinates(d[1]))
        };
        if (allVertices || vertice.from.x === vertice.to.x || vertice.from.y === vertice.to.y) {
            drawVertice(vertice);
        }
    });
    return vertices;
}
function drawVertice(vertice) {
    const handleIndex = (index) => {
        fullMap[index] = fullMap[index] ? fullMap[index] + 1 : 1;
        computeCrossover(index);
    };
    //init 
    let coord = vertice.from;
    handleIndex(getIndex(coord));
    while (!coordinatesEquals(coord, vertice.to)) {
        coord = actions[vertice.direction](coord);
        handleIndex(getIndex(coord));
    }
}
function computeCrossover(index) {
    //compute crossOvers
    if (fullMap[index] === 2) {
        nbCrossOver += 1;
    }
}
function getIndex(coord) {
    return (coord.x * 10000) + coord.y;
}
function coordinatesEquals(c1, c2) {
    return c1.x == c2.x && c1.y == c2.y;
}
function getVerticeDirection(from, to) {
    let diagonal = '';
    let horizontal = '';
    let vertical = '';
    if (from.x > to.x)
        horizontal = 'l';
    if (from.x < to.x)
        horizontal = 'r';
    if (from.y < to.y)
        vertical = 'd';
    if (from.y > to.y)
        vertical = 'u';
    if (from.x !== to.x && from.y !== to.y)
        diagonal = 'd';
    return diagonal + horizontal + vertical;
}
function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)];
}
exports.handleInput = handleInput;
