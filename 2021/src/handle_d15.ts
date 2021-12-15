interface Coord {
    x: number,
    y: number
}

function index(coord: Coord): string {
    return JSON.stringify(coord)
}

interface Cost {
    cost: number,
    to: Coord
}

interface Graph {
    neighbors: {[key: string]: Array<Cost>}
}

interface QElement {
    coord: Coord,
    priority: number
}

class PriorityQueue {
    items: Array<QElement> = []

    put = function(coord: Coord, priority: number) {
        const qElement = {coord, priority}
        
        let added = false
        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].priority > priority) {
                this.items.splice(i, 0, qElement)
                added = true
                break
            }
        }

        if (!added) {
            this.items.push(qElement)
        }
        
    }

    get = function(): Coord {
        return this.items.shift().coord
    }

    empty = function(): boolean {
        return this.items.length === 0
    }
}

function getAllNeighbors(coord: Coord, width: number, height: number): Array<Coord> {
    let neighbors: Array<Coord> = []
    if (coord.x - 1 >= 0) neighbors.push({x: coord.x - 1, y: coord.y})
    if (coord.x + 1 < width) neighbors.push({x: coord.x + 1, y: coord.y})
    if (coord.y - 1 >= 0) neighbors.push({x: coord.x, y: coord.y - 1})
    if (coord.y + 1 < height) neighbors.push({x: coord.x, y: coord.y + 1})

    return neighbors
}

function heuristic(a: Coord, b: Coord): number {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y)
}

function parse(lines: Array<string>): [Graph, number, number] {
    let tree: Graph = {neighbors: {}}
    const width = lines[0] ? lines[0].length : 0
    const height = lines.length

    for (let y=0; y < lines.length; y++) {
        const tLine = lines[y].split('').map(c => Number(c))
        for (let x = 0; x < tLine.length; x++) {
            const currentCoord: Coord =  {x, y}

            tree.neighbors[index(currentCoord)] = []
            getAllNeighbors(currentCoord, width, height).forEach((coord: Coord) => {
                tree.neighbors[index(currentCoord)].push({to: coord, cost: Number(lines[coord.y][coord.x])})
            })
        }
    }

    return [tree, width, height]
}

function handleInput_1(lines: Array<string>){
    let [tree, width, height]: [Graph, number, number] = parse(lines)    
    const max = width*height*10*10
    const startCoord: Coord = {x: 0, y:0}
    const endCoord: Coord = {x:width-1, y:height-1}
    const start:string =  index(startCoord)
    const end: string = index(endCoord)
    
    let toVisit: PriorityQueue = new PriorityQueue()
    toVisit.put({x: 0, y:0}, 0)

    let came_from: {[key: string]: Coord} = {}
    came_from[start] = undefined

    let cost_so_far: {[key: string]: number} = {}
    cost_so_far[start] = 0

    let currentCoord: Coord
    while (!toVisit.empty()) {
        currentCoord = toVisit.get()
        

        if (index(currentCoord) === end) {
            break
        }

        const currentIndex = index(currentCoord)
        tree.neighbors[currentIndex].forEach((cost: Cost)=> {
            const new_cost = cost_so_far[currentIndex] + cost.cost
            
            if (!Object.keys(cost_so_far).includes(index(cost.to)) || new_cost < cost_so_far[index(cost.to)]){
                cost_so_far[index(cost.to)] = new_cost
                toVisit.put(cost.to, new_cost)
                came_from[index(cost.to)] = currentCoord
            }
        })        
    }
    
    return cost_so_far[end]
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return handleInput_1(lines)
}