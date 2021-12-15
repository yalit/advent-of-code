const aStar = require('a-star')

interface Node {
    x: number, 
    y: number, 
    v: number
}
type Grid = Array<Array<Node>>

function solve(grid: Grid): number {
    let width = grid[0].length
    let height = grid.length

    const end = grid[height-1][width-1]

    function getAllNeighbors(n: Node): Array<Node> {
        let neighbors: Array<Node> = []
        if (n.x - 1 >= 0) neighbors.push(grid[n.y][n.x - 1])
        if (n.x + 1 < width) neighbors.push(grid[n.y][n.x + 1])
        if (n.y - 1 >= 0) neighbors.push(grid[n.y - 1][n.x])
        if (n.y + 1 < height) neighbors.push(grid[n.y + 1][n.x])
    
        return neighbors
    }

    const path = aStar({
        start: grid[0][0], 
        isEnd: (n: Node) => n.x === width -1 && n.y === height -1,
        neighbor: (n: Node) => getAllNeighbors(n),
        distance: (a: Node, b: Node) => b.v,
        heuristic: (n: Node) => Math.abs(width - 1 - n.x) + Math.abs(height - 1 - n.y), //distance euclidienne
        hash: (n: Node) => `${n.x},${n.y}`
    })
    console.log(path);
    
    return path.cost
}

function getGrid(lines: Array<string>): Grid {
    return lines.map((line: string, y: number) => line.split('').map((c: string , x: number) => {return {x, y, v: Number(c)}}))
}

function handleInput_1(lines: Array<string>){
    let grid: Grid = getGrid(lines)
    return solve(grid)
}

function handleInput_2(lines: Array<string>){
    let grid: Grid = getGrid(lines)
    
    function addOne(n : number): number {
        if (n + 1 === 10) return 1
        return n + 1
    }

    function addOneToRow(row: Array<Node>, ): Array<Node> {
        return row.map((n: Node) => Object.assign({}, {y: n.y, x: n.x + row.length, v: addOne(n.v)}))
    }

    function addOneToGrid(grid: Grid): Grid {
        return grid.map(row => row.map((n: Node) => Object.assign({}, {x: n.x, y: n.y + grid.length, v: addOne(n.v)})))
    }

    // width
    grid = grid.map((row: Array<Node>, i: number) => {
        let newRow = [...row]
        for (let i = 1; i < 5; i++){
            newRow = addOneToRow(newRow)
            row = row.concat(newRow)
        }           
        return row 
    })    
    
    // height
    let newGrid: Grid = grid
    for (let i = 1; i < 5; i++) {
        newGrid = addOneToGrid(newGrid)
        grid = grid.concat(newGrid)
    }      

    return solve(grid)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}