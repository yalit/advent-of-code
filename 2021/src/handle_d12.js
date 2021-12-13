Array.prototype.has = function(node) {
    if (!node) return false

    let found = false
    for (let i = 0; i < this.length; i++) {
        if (this[i].name === node.name) found = true
    }

    return found
}
class Node {
    name
    size
    neighbors = []

    constructor(name) {
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

    addNeighbor = function(node) { 
        this.neighbors.push(node)
    }
}

let allPaths

function handleInput_1(lines){
    let tree = new Map()
    
    lines.forEach(line => {
        const [from, to] = line.split('-')
        let fromNode = (tree.has(from)) ? tree.get(from) : new Node(from)
        let toNode = (tree.has(to)) ? tree.get(to) : new Node(to)

        fromNode.addNeighbor(toNode)
        toNode.addNeighbor(fromNode)

        if (!tree.has(from)) tree.set(from, fromNode)
        if (!tree.has(to)) tree.set(to, toNode)
    });

    allPaths = []
    depthFirst(tree.get('start'))

    return allPaths.length//allPaths.map(path => path.map(n => n.name))
}

function handleInput_2(lines){
    let tree = new Map()
    
    lines.forEach(line => {
        const [from, to] = line.split('-')
        let fromNode = (tree.has(from)) ? tree.get(from) : new Node(from)
        let toNode = (tree.has(to)) ? tree.get(to) : new Node(to)

        fromNode.addNeighbor(toNode)
        toNode.addNeighbor(fromNode)

        if (!tree.has(from)) tree.set(from, fromNode)
        if (!tree.has(to)) tree.set(to, toNode)
    });

    allPaths = []
    depthFirstTwice(tree.get('start'))

    return allPaths.length//allPaths.map(path => path.map(n => n.name))
}

function depthFirst(node, currentPath = []) {
    if (node.isSmall() && currentPath.has(node)) return

    currentPath.push(node)

    if (node.isEnd()) {    
        allPaths.push(currentPath)
        return
    }

    node.neighbors.forEach(neighbor => {
       return depthFirst(neighbor, [...currentPath])
    })
}

function depthFirstTwice(node, currentPath = [], alreadyTwiceInSmallCave = false) {
    if (node.isSmall() && currentPath.has(node)) {
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

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}