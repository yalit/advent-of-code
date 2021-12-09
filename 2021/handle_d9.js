import _ from "lodash"

function handleInput_1(lines){
    const fullMap = new FullMap(lines)

    return _.sumBy(fullMap.fullMap.filter(n => n.isLowPoint()), l => l.getRiskLevel())
}

function handleInput_2(lines){
    const fullMap = new FullMap(lines)
    
    const basins = fullMap.fullMap
        .filter(n => n.isLowPoint())
        .map(n => n.basin)
        .sort((a, b) => b.length - a.length)
        .slice(0,3)
        .reduce((a,basin) => a * basin.length, 1)
    ;

    return basins
}

function FullMap(lines) {
    this.fullMap = lines.join('').split('').map((v, i) => new Point(i, v))
    this.width = lines[0].length
    this.totalLength = this.fullMap.length

    this.moves = {
        'left': n => (n % this.width) - 1 < 0 ? n : n - 1,
        'right': n => (n % this.width) + 1 >= this.width ? n : n + 1,
        'up': n => n < this.width ? n : n - this.width,
        'down': n => n + this.width >= this.totalLength ? n : n + this.width
    }

    this.getPointNeighbors = function(point) {
        let neighbors = []
        Object.values(this.moves).forEach(move => {
            if (move(point.pos) === point.pos) return
            neighbors.push(this.fullMap[move(point.pos)])
        })
        return neighbors
    }

    this.getBasinRelatedNeighbor = function(point, initial = true, basinNeighbors = []) {
        if (! (point.isLowPoint() || !initial)) return basinNeighbors
        
        if (point.value === 9) return basinNeighbors

        if (this.arrayHasPoint(basinNeighbors, point)) return basinNeighbors

        basinNeighbors.push(point)
        this.getPointNeighbors(point).forEach(neighbor => {
            basinNeighbors = this.getBasinRelatedNeighbor(neighbor, false, basinNeighbors)   
        });

        return basinNeighbors
    }

    this.arrayHasPoint = (arr, point) => {
        return arr.reduce((has, p) => has ? has : point.pos === p.pos, false)
    }
    
    //instantiate neighbors
    this.fullMap.map(p => {
        this.getPointNeighbors(p).forEach(n => {
            if (p.pos !== n.pos) p.addNeighbor(n)
        })
        return p
    })

    //instantiate basins
    this.fullMap.map(p => {
        this.getBasinRelatedNeighbor(p).forEach(b => {
            p.addToBasin(b)
        })
    })
}

function Point(pos = null, value = null) {
    this.pos = pos;
    this.value = Number(value);
    this.neighbors = [];
    this.basin = []
    
    this.addNeighbor = function(neighbor) {
        this.neighbors.push(neighbor)
    }

    this.addToBasin = function(point) {
        this.basin.push(point)
    }

    this.getRiskLevel = function() {
        return this.value + 1
    }

    this.isLowPoint = function() {
        if (this.neighbors === []) return false

        if (this.neighbors.filter(n => this.value < n.value).length === this.neighbors.length) return true
        
        return false
    }
}


export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}