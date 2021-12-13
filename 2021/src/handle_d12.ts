function arrayHas(arr, node) {
    if (!node) return false

    let found = false
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].name === node.name) found = true
    }

    return found
}
class Node {
    name: string
    size: string
    neighbors: Array<Node> = []

    constructor(name: string) {
        this.name = name
        this.size = (name.match(/^[a-z$]*$/)) ? 'small' : 'big'
    }

    isSmall = function() {
        return this.size === 'small'
    }

    isBig = function() {
        return this.size === 'big'
    }

    isStart = function() {
        return this.name === 'start'
    }

    isEnd = function() {
        return this.name === 'end'
    }

    addNeighbor = function(node: Node) { 
        this.neighbors.push(node)
    }
}

let allPaths: Array<Array<Node>>

function handleInput_1(lines: Array<string>){
    let tree: Map<string, Node> = new Map()
    
    lines.forEach(line => {
        const [from, to] = line.split('-')
        let fromNode: Node = (tree.has(from)) ? tree.get(from) : new Node(from)
        let toNode: Node = (tree.has(to)) ? tree.get(to) : new Node(to)

        fromNode.addNeighbor(toNode)
        toNode.addNeighbor(fromNode)

        if (!tree.has(from)) tree.set(from, fromNode)
        if (!tree.has(to)) tree.set(to, toNode)
    });

    allPaths = []
    depthFirst(tree.get('start'))

    return allPaths.length
}

function handleInput_2(lines: Array<string>){
    let tree: Map<string, Node> = new Map()
    
    lines.forEach(line => {
        const [from, to] = line.split('-')
        let fromNode: Node = (tree.has(from)) ? tree.get(from) : new Node(from)
        let toNode: Node = (tree.has(to)) ? tree.get(to) : new Node(to)

        fromNode.addNeighbor(toNode)
        toNode.addNeighbor(fromNode)

        if (!tree.has(from)) tree.set(from, fromNode)
        if (!tree.has(to)) tree.set(to, toNode)
    });

    allPaths = []
    depthFirstTwice(tree.get('start'))

    return allPaths.length
}

function depthFirst(node: Node, currentPath: Array<Node> = []) {
    if (node.isSmall() && arrayHas(currentPath, node)) return

    currentPath.push(node)

    if (node.isEnd()) {    
        allPaths.push(currentPath)
        return
    }

    node.neighbors.forEach(neighbor => {
       return depthFirst(neighbor, [...currentPath])
    })
}

function depthFirstTwice(node: Node, currentPath: Array<Node> = [], alreadyTwiceInSmallCave = false) {
    if (node.isSmall() && arrayHas(currentPath, node)) {
        if (node.isEnd() || node.isStart()) return
        if (alreadyTwiceInSmallCave) return
        else alreadyTwiceInSmallCave = true
    }

    currentPath.push(node)

    if (node.isEnd()) {    
        allPaths.push(currentPath)
        return
    }

    node.neighbors.forEach(neighbor => {
       return depthFirstTwice(neighbor, [...currentPath], alreadyTwiceInSmallCave)
    })
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}