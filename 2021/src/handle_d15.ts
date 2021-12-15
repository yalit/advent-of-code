interface Coord {
    x: number,
    y: number
}

interface Vertice {
    weight: number,
    to: Coord
}

class Node {
    vertices: Array<Vertice> = []

    addVertice = function(vertice: Vertice) {
        this.vertices.push(vertice)
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

function parse(lines: Array<string>): [Map<string, Node>, number, number] {
    let tree = new Map()
    const width = lines[0] ? lines[0].length : 0
    const height = lines.length

    for (let y=0; y < lines.length; y++) {
        const tLine = lines[y].split('').map(c => Number(c))
        for (let x = 0; x < tLine.length; x++) {
            let node = new Node()
            const currentCoord: Coord =  {x, y}
            getAllNeighbors(currentCoord, width, height).forEach((coord: Coord) => {
                node.addVertice({to: coord, weight: Number(lines[coord.y][coord.x])})
            })
            tree.set(index(currentCoord), node)
        }
    }

    return [tree, width, height]
}

function index(coord: Coord): string {
    return JSON.stringify(coord)
}

function handleInput_1(lines: Array<string>){
    let [tree, width, height]: [Map<string, Node>, number, number] = parse(lines)    
    const max = width*height*10*10
    const start:string =  index({x: 0, y:0})
    const end: string = index({x:width-1, y:height-1})

    let visited: Array<string> = []
    let distances: Map<string, number> = new Map()

    tree.forEach((node: Node, i: string) => distances.set(i, undefined))
    distances.set(start, 0)

    let currentIndex = start
    let endFound = false
    while(visited.length < tree.size && ! endFound) {
        console.log(tree.size, visited.length);
        
        //compute min size for all neighbors
        tree.get(currentIndex).vertices.forEach((v: Vertice) => {
            const weight: number = distances.get(currentIndex) + v.weight
            if (distances.get(index(v.to)) === undefined) distances.set(index(v.to), weight)
            else if (distances.get(index(v.to)) > weight) distances.set(index(v.to), distances.get(currentIndex) + v.weight)
        })

        //add currentIndex to the visited nodes
        visited.push(currentIndex)
        tree.delete(currentIndex)

        endFound = currentIndex === end

        //get Next index with smaller distance
        let smallestDistance = max
        Array.from(tree.keys()).forEach((k : string) => {
            if (distances.get(k) < smallestDistance) {
                smallestDistance = distances.get(k)
                currentIndex = k
            }
        })
    }

    return distances.get(end)
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return handleInput_1(lines)
}