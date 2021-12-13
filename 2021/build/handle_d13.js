"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handleInput = void 0;
const fs_1 = require("fs");
function handleInput_1(lines, nbSteps) {
    let [grid, folds] = processInput(lines);
    let i = 0;
    while (i < nbSteps) {
        const fold = folds[i];
        if (fold.type === 'y')
            grid = foldY(grid, fold.value);
        else if (fold.type === 'x')
            grid = foldX(grid, fold.value);
        i++;
    }
    return grid.length;
}
function handleInput_2(lines) {
    let [grid, folds] = processInput(lines);
    let i = 0;
    while (i < folds.length) {
        const fold = folds[i];
        if (fold.type === 'y')
            grid = foldY(grid, fold.value);
        else if (fold.type === 'x')
            grid = foldX(grid, fold.value);
        i++;
    }
    writeToOutputFile(grid);
    return grid.length;
}
class Point {
    constructor(x, y) {
        this.equals = function (point) {
            return this.x === point.x && this.y === point.y;
        };
        this.x = x;
        this.y = y;
    }
}
function processInput(lines) {
    let grid = [];
    let folds = [];
    let i = 0;
    while (lines[i] !== '') {
        const [x, y] = lines[i].split(',').map(c => Number(c));
        grid.push(new Point(x, y));
        i++;
    }
    for (let j = i + 1; j < lines.length; j++) {
        const [, axis, n] = lines[j].match(/([x|y])=([\d]*)/);
        folds.push({
            type: axis,
            value: Number(n)
        });
    }
    return [grid, folds];
}
function foldY(grid, n) {
    let newGrid = [];
    grid.forEach(point => {
        if (point.y === n)
            return;
        else if (point.y < n) {
            if (!hasPoint(newGrid, point))
                newGrid.push(point);
            return;
        }
        const newY = n - (point.y - n);
        if (newY < 0)
            return;
        const newPoint = new Point(point.x, newY);
        if (!hasPoint(newGrid, newPoint))
            newGrid.push(newPoint);
    });
    return newGrid;
}
function foldX(grid, n) {
    let newGrid = [];
    grid.forEach(point => {
        if (point.x === n)
            return;
        else if (point.x < n) {
            if (!hasPoint(newGrid, point))
                newGrid.push(point);
            return;
        }
        const newX = n - (point.x - n);
        if (newX < 0)
            return;
        const newPoint = new Point(newX, point.y);
        if (!hasPoint(newGrid, newPoint))
            newGrid.push(newPoint);
    });
    return newGrid;
}
function hasPoint(grid, point) {
    if (!point)
        return false;
    let found = false;
    for (let i = 0; i < grid.length; i++) {
        if (grid[i].equals(point))
            found = true;
    }
    return found;
}
function writeToOutputFile(grid) {
    const content = grid.map(point => point.x + "," + point.y).join('#/#');
    (0, fs_1.writeFile)('../output/output_13_part2.txt', content, err => {
        if (err) {
            console.error(err);
            return;
        }
        //file written successfully
    });
}
function handleInput(lines) {
    return [handleInput_1(lines, 1), handleInput_2(lines)];
}
exports.handleInput = handleInput;
