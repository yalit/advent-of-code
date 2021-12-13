import { writeFile } from 'fs'
import internal = require('stream')

function handleInput_1(lines: Array<string>, nbSteps: number): number{
    let [grid, folds] = processInput(lines)    

    let i = 0
    while (i < nbSteps) {
        const fold = folds[i]

        if (fold.type === 'y') grid = foldY(grid, fold.value)
        else if (fold.type === 'x') grid = foldX(grid, fold.value)

        i++
    } 
    return grid.length
}

function handleInput_2(lines: Array<string>): number{
    let [grid, folds] = processInput(lines)    

    let i = 0
    while (i < folds.length) {
        const fold = folds[i]

        if (fold.type === 'y') grid = foldY(grid, fold.value)
        else if (fold.type === 'x') grid = foldX(grid, fold.value)

        i++
    } 
    
    writeToOutputFile(grid)
    return grid.length
}

class Point {
    x: number
    y: number
    constructor(x: number, y: number) {
        this.x = x
        this.y = y
    }

    equals = function(point: Point) {
        return this.x === point.x && this.y === point.y
    }
}

interface Fold {
    type: string,
    value: number
}

function processInput(lines: Array<string>): [Array<Point>, Array<Fold>] {
    let grid: Array<Point> = []
    let folds: Array<Fold> = []

    let i = 0
    while (lines[i] !== ''){
        const [x, y] = lines[i].split(',').map(c => Number(c))
        grid.push(new Point(x,y))
        i++
    }

    for (let j = i+1; j < lines.length; j++) {
        const [,axis,n] = lines[j].match(/([x|y])=([\d]*)/)
        folds.push({
            type: axis, 
            value: Number(n)
        })
    }

    return [grid, folds]
}

function foldY(grid: Array<Point>, n: number): Array<Point> {
    let newGrid: Array<Point> = []

    grid.forEach(point => {
        if (point.y === n) return
        else if (point.y < n) {
            if (!hasPoint(newGrid, point)) newGrid.push(point)
            return
        }
        
        const newY = n - (point.y - n)
        if (newY < 0) return 

        const newPoint = new Point(point.x, newY)
        if (!hasPoint(newGrid, newPoint)) newGrid.push(newPoint)
    });

    return newGrid
}

function foldX(grid: Array<Point>, n: number): Array<Point> {
    let newGrid: Array<Point> = []

    grid.forEach(point => {
        if (point.x === n) return
        else if (point.x < n) {
            if (!hasPoint(newGrid, point)) newGrid.push(point)
            return
        }

        const newX = n - (point.x - n)
        if ( newX < 0) return 

        const newPoint = new Point(newX, point.y)
        if (!hasPoint(newGrid, newPoint)) newGrid.push(newPoint)
    });

    return newGrid
}

function hasPoint (grid: Array<Point>, point: Point): boolean {
    if (!point) return false

    let found = false
    for (let i = 0; i < grid.length; i++) {
        if (grid[i].equals(point)) found = true
    }

    return found
}

function writeToOutputFile(grid: Array<Point>): void {
    const content = grid.map(point => point.x+","+point.y).join('#/#')

    writeFile('../output/output_13_part2.txt', content, err => {
    if (err) {
        console.error(err)
        return
    }
    //file written successfully
    })
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines, 1), handleInput_2(lines)]
}