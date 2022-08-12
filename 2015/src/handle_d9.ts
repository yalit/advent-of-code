type Node = {
    name: string,
    vertices: Array<Vertice>
}

class Vertice {
    node1: Node
    node2: Node
    weight: number

    constructor(node1: Node, node2: Node, weight: number ) {
        this.node1 = node1
        this.node2 = node2
        this.weight = weight
    }

    getOtherNode(node: Node): Node {
        return (this.node1 === node) ? this.node2 : this.node1
    }
}

type VerticeData = {
    from: string,
    to: string,
    weight:number
}

function extractAllVerticeData(lines: Array<string>): Array<VerticeData> {
    return lines.map(line => extractData(line))
}
function extractData(line: string): VerticeData {
    let match = line.match(/(\w+).to.(\w+).=.(\d+)/)
    
    return {from: match[1], to: match[2], weight: parseInt(match[3])}
}

class Graph {
    nodes: {[k:string]: Node} = {}
    vertices: Array<Vertice> = []

    constructor(verticesData: Array<VerticeData>) {
        verticesData.forEach(verticeData => {
            let node1 = this.getNode(verticeData.from)
            let node2 = this.getNode(verticeData.to)
            let vertice: Vertice = new Vertice(node1, node2, verticeData.weight)

            node1.vertices.push(vertice)
            node2.vertices.push(vertice)
            this.vertices.push(vertice)
        })
        console.log(this.nodes)
    }

    getNode(name: string) {
        if (!(name in this.nodes)) {
            let node = {name, vertices: []}
            this.nodes[name] = node
        }

        return this.nodes[name]
    }
}
let min: number = Infinity

function findMinimum(g: Graph, path: Array<Node> = [], currentPathWeight: number = 0): void {
    if (min <= currentPathWeight) {
        return
    }

    if (path.length ===  Object.keys(g.nodes).length) {
        min = Math.min(min, currentPathWeight)
        return
    }

    let lastNode = path[path.length-1]
    lastNode.vertices.forEach(vertice => {
        let nextNode = vertice.getOtherNode(lastNode)
        if (path.indexOf(nextNode) >= 0) {
            return
        }
      findMinimum(g, path.concat([nextNode]), currentPathWeight + vertice.weight)
    })
}

let max: number = 0

function findMaximum(g: Graph, path: Array<Node> = [], currentPathWeight: number = 0): void {
    if (path.length ===  Object.keys(g.nodes).length) {
        max = Math.max(max, currentPathWeight)
        return
    }

    let lastNode = path[path.length-1]
    lastNode.vertices.forEach(vertice => {
        let nextNode = vertice.getOtherNode(lastNode)
        if (path.indexOf(nextNode) >= 0) {
            return
        }
        findMaximum(g, path.concat([nextNode]), currentPathWeight + vertice.weight)
    })
}

function handleInput_1(lines: Array<string>){
    let graph = new Graph(extractAllVerticeData(lines))
    Object.keys(graph.nodes).forEach((name: string) => findMinimum(graph, [graph.getNode(name)], 0))
    return min
}

function handleInput_2(lines: Array<string>){
    let graph = new Graph(extractAllVerticeData(lines))
    Object.keys(graph.nodes).forEach((name: string) => findMaximum(graph, [graph.getNode(name)], 0))
    return max
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}