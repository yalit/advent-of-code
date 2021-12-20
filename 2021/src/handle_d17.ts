import {_} from 'lodash'

function parseLine(line: string): Array<number> {
    const n = line.match(/([?-\d]+)/g)
    
    return n.map(c => Number(c))
}

type Coord = {x: number, y: number}
type Target = {topleft: Coord, bottomright: Coord}

function getTarget(line: string): Target {
    const inputs = parseLine(line)

    const left = Math.min(inputs[0], inputs[1])
    const right = Math.max(inputs[0], inputs[1])
    const top = Math.max(inputs[2], inputs[3])
    const bottom = Math.min(inputs[2], inputs[3])

    return {topleft: {x: left, y: top}, bottomright: {x: right, y: bottom}}
}

function isXinTarget(coord: Coord, target: Target ): boolean {
    return coord.x <= target.bottomright.x && coord.x >= target.topleft.x
}

function isYinTarget(coord: Coord, target: Target): boolean {
    return coord.y <= target.topleft.y && coord.y >= target.bottomright.y
}

function isCoordInTarget(coord: Coord, target: Target) {
    return isXinTarget(coord, target) && isYinTarget(coord, target)
}

function getAllCoordsForXAndY(x: number, y: number, target: Target): Array<Coord> {
    let coords = []
    let coord = {x: 0, y: 0}
    let stepNumber = 0
    while (coord.x <= target.bottomright.x && coord.y >= target.bottomright.y) {
        let addX = x - stepNumber <= 0 ? 0 : x - stepNumber
        let addY = y - stepNumber
        coord = {x: coord.x + addX, y: coord.y + addY}
        
        if (isCoordInTarget(coord, target)) coords.push(coord)
        
        stepNumber++
    }

    return coords
}

function handleInput_1(lines: Array<string>){ 
    const target = getTarget(lines[0])
    return _.sum(_.range(Math.abs(target.bottomright.y))) //always arriving at 0, so the biggest step that can be done is Math.abs(lowest step - 1)
}

function handleInput_2(lines: Array<string>){
    const target = getTarget(lines[0])
    
    let y = target.bottomright.y
    let nbTrajectories = 0
    let coords: Array<Coord>
    for (let y = target.bottomright.y; y <= Math.abs(target.bottomright.y); y++){
        for (let x = 0; x <= target.bottomright.x; x++) {
            coords = getAllCoordsForXAndY(x,y,target)
            if (coords.length > 0) nbTrajectories++
        }
    }

    return nbTrajectories
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}
