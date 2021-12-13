import { writeFile } from 'fs'

function handleInput_1(lines, nbSteps){
    let [grid, folds] = processInput(lines)    

    let i = 0
    while (i < nbSteps) {
        const fold = folds[i]

        if (fold[0] === 'y') grid = foldY(grid, fold[1])
        else if (fold[0] === 'x') grid = foldX(grid, fold[1])

        i++
    } 
    return grid.length
}

function handleInput_2(lines){
    let [grid, folds] = processInput(lines)    

    let i = 0
    while (i < folds.length) {
        const fold = folds[i]

        if (fold[0] === 'y') grid = foldY(grid, fold[1])
        else if (fold[0] === 'x') grid = foldX(grid, fold[1])

        i++
    } 
    console.log(grid);
    writeToOutputFile(grid)
    return grid.length
}

class Point {
    constructor(x, y) {
        this.x = x
        this.y = y
    }

    equals = function(point) {
        return this.x === point.x && this.y === point.y
    }
}

function processInput(lines) {
    let grid = []
    let folds = []

    let i = 0
    while (lines[i] !== ''){
        const [x, y] = lines[i].split(',').map(c => Number(c))
        grid.push(new Point(x,y))
        i++
    }

    for (let j = i+1; j < lines.length; j++) {
        const [,axis,n] = lines[j].match(/([x|y])=([\d]*)/)
        folds.push([axis, n])
    }

    return [grid, folds]
}

function foldY(grid, n) {
    let newGrid = []

    grid.forEach(point => {
        if (point.y === n) return
        else if (point.y < n) {
            if (!newGrid.hasPoint(point)) newGrid.push(point)
            return
        }
        
        const newY = n - (point.y - n)
        if (newY < 0) return 

        const newPoint = new Point(point.x, newY)
        if (!newGrid.hasPoint(newPoint)) newGrid.push(newPoint)
    });

    return newGrid
}

function foldX(grid, n) {
    let newGrid = []

    grid.forEach(point => {
        if (point.x === n) return
        else if (point.x < n) {
            if (!newGrid.hasPoint(point)) newGrid.push(point)
            return
        }

        const newX = n - (point.x - n)
        if ( newX < 0) return 

        const newPoint = new Point(newX, point.y)
        if (!newGrid.hasPoint(newPoint)) newGrid.push(newPoint)
    });

    return newGrid
}

Array.prototype.hasPoint = function(point) {
    if (!point) return false

    let found = false
    for (let i = 0; i < this.length; i++) {
        if (this[i].equals(point)) found = true
    }

    return found
}

function writeToOutputFile(grid) {
    const content = grid.map(point => point.x+","+point.y).join('#/#')

    writeFile('output_13_part2.txt', content, err => {
    if (err) {
        console.error(err)
        return
    }
    //file written successfully
    })
}

export function handleInput(lines) {
    return [handleInput_1(lines, 1), handleInput_2(lines)]
}