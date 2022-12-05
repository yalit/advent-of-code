import { Coordinate } from "./libraries/matrix"

// 0 = East / 90 = South / 180 = West / 270 = North
type Direction = 0 | 90 | 180 | 270 

const DirectionMapping: {[k in Direction]: Move} = {
    0 : 'E',
    90: 'S', 
    180: 'W',
    270: 'N'
}

type Move = 'N' | 'S'| 'E' | 'W' | 'L' | 'R' | 'F'

interface DirectionBoat {
    coordinate: Coordinate,
    direction: Direction
}

interface WaypointBoat {
    coordinate: Coordinate,
    waypoint: Coordinate
}

type DirectionMoveHandler = (boat: DirectionBoat, value: number) => DirectionBoat
type WaypointMoveHandler = (boat: WaypointBoat, value: number) => WaypointBoat

const handleBoatMoves: {[k in Move]: DirectionMoveHandler} = {
    'E' : (b: DirectionBoat, v: number) => {return {...b, coordinate: {...b.coordinate, y: b.coordinate.y + v}}},
    'S' : (b: DirectionBoat, v: number) => {return {...b, coordinate: {...b.coordinate, x: b.coordinate.x + v}}},
    'N' : (b: DirectionBoat, v: number) => {return {...b, coordinate: {...b.coordinate, x: b.coordinate.x - v}}},
    'W' : (b: DirectionBoat, v: number) => {return {...b, coordinate: {...b.coordinate, y: b.coordinate.y - v}}},
    'L' : (b: DirectionBoat, v: number) => {return {...b, direction: (360 + b.direction - v) % 360 as Direction}},
    'R' : (b: DirectionBoat, v: number) => {return {...b, direction: (360 + b.direction + v) % 360 as Direction}},
    'F' : (b: DirectionBoat, v: number) => handleBoatMoves[DirectionMapping[b.direction]](b, v)
}

const handleWaypointMoves: {[k in Move]: WaypointMoveHandler} = {
    'E' : (b: WaypointBoat, v: number) => {return {...b, waypoint: {...b.waypoint, x: b.waypoint.x + v}}},
    'S' : (b: WaypointBoat, v: number) => {return {...b, waypoint: {...b.waypoint, y: b.waypoint.y + v}}},
    'N' : (b: WaypointBoat, v: number) => {return {...b, waypoint: {...b.waypoint, y: b.waypoint.y - v}}},
    'W' : (b: WaypointBoat, v: number) => {return {...b, waypoint: {...b.waypoint, x: b.waypoint.x - v}}},
    'L' : (b: WaypointBoat, v: number) => {
        let waypoint: Coordinate
        if (v === 90) {
            waypoint = {x: b.coordinate.x + (b.waypoint.y - b.coordinate.y), y: b.coordinate.y - (b.waypoint.x - b.coordinate.x)}
        } 
        if (v === 180) {
            waypoint = {x: b.coordinate.x - (b.waypoint.x - b.coordinate.x), y: b.coordinate.y - (b.waypoint.y - b.coordinate.y)}
        }
        return {...b, waypoint}
    },
    'R' : (b: WaypointBoat, v: number) => {
        let waypoint: Coordinate
        if (v === 90) {
            waypoint = {x: b.coordinate.x - (b.waypoint.y - b.coordinate.y), y: b.coordinate.y + (b.waypoint.x - b.coordinate.x)}
        } 
        if (v === 180) {
            waypoint = {x: b.coordinate.x - (b.waypoint.x - b.coordinate.x), y: b.coordinate.y - (b.waypoint.y - b.coordinate.y)}
        }
        return {...b, waypoint}
    },
    'F' : (b: WaypointBoat, v: number) => {
        const moveX = v * (b.waypoint.x - b.coordinate.x)
        const moveY = v * (b.waypoint.y - b.coordinate.y)
        return {
            ...b, 
            coordinate: {x: b.coordinate.x + moveX,y: b.coordinate.y + moveY},
            waypoint: {x: b.waypoint.x + moveX,y: b.waypoint.y + moveY}
        }
    }
}

function handleInput_1(lines: Array<string>){
    let boat: DirectionBoat = {coordinate: {x: 0, y: 0}, direction: 0}

    lines.forEach(l => {
        boat = handleBoatMoves[l.slice(0,1)](boat, parseInt(l.slice(1)))
    })
    return Math.abs(boat.coordinate.x) + Math.abs(boat.coordinate.y)
}

function handleInput_2(lines: Array<string>){
    let boat: WaypointBoat = {coordinate: {x: 0, y: 0}, waypoint: {x: 10, y: -1}}

    const parseInput = (line: string): {move: Move, value: number} => {
        let move = line.slice(0,1) as Move
        let value = parseInt(line.slice(1))

        if (['L', 'R'].includes(move) && value >= 270) {
            move = move === 'L' ? 'R' : 'L'
            value = 90
        }
        return {move, value}
    }

    lines.forEach(l => {
        const {move, value} = parseInput(l)
        boat = handleWaypointMoves[move](boat, value)
        console.log(l, boat)
    })
    return Math.abs(boat.coordinate.x) + Math.abs(boat.coordinate.y)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}