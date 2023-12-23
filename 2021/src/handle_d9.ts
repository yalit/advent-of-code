import { _ } from "lodash"

function handleInput_1(lines: Array<string>){
    const fullMap = new FullMap(lines)

    return _.sumBy(fullMap.fullMap.filter(n => n.isLowPoint()), l => l.getRiskLevel())
}

function handleInput_2(lines: Array<string>){
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

class FullMap {
    fullMap: Array<Point>
    width: number
    totalLength: number
    
    constructor(lines: Array<string>) {
        this.fullMap = lines.join('').split('').map((v, i) => new Point(i, v))
        this.width = lines[0].length
        this.totalLength = this.fullMap.length

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

    moves = {
        'left': (n: number) => (n % this.width) - 1 < 0 ? n : n - 1,
        'right': (n: number) => (n % this.width) + 1 >= this.width ? n : n + 1,
        'up': (n: number) => n < this.width ? n : n - this.width,
        'down': (n: number) => n + this.width >= this.totalLength ? n : n + this.width
    }

    getPointNeighbors = function(point) {
        let neighbors = []
        Object.keys(this.moves).forEach(k => {
            const move = this.moves[k]
            if (move(point.pos) === point.pos) return
            neighbors.push(this.fullMap[move(point.pos)])
        })
        return neighbors
    }

    getBasinRelatedNeighbor = function(point, initial = true, basinNeighbors = []) {
        if (! (point.isLowPoint() || !initial)) return basinNeighbors
        
        if (point.value === 9) return basinNeighbors

        if (this.arrayHasPoint(basinNeighbors, point)) return basinNeighbors

        basinNeighbors.push(point)
        this.getPointNeighbors(point).forEach(neighbor => {
            basinNeighbors = this.getBasinRelatedNeighbor(neighbor, false, basinNeighbors)   
        });

        return basinNeighbors
    }

    arrayHasPoint = (arr, point) => {
        return arr.reduce((has, p) => has ? has : point.pos === p.pos, false)
    }
}

class Point {
    pos: number
    value: number
    neighbors: Array<Point>
    basin: Array<Point>

    constructor(pos: number = null, value: string = null) {
        this.pos = pos;
        this.value = Number(value);
        this.neighbors = [];
        this.basin = []
    }
    
    addNeighbor = function(neighbor: Point): void {
        this.neighbors.push(neighbor)
    }

    addToBasin = function(point: Point): void {
        this.basin.push(point)
    }

    getRiskLevel = function(): number {
        return this.value + 1
    }

    isLowPoint = function(): boolean {
        if (this.neighbors.length === 0) return false

        if (this.neighbors.filter(n => this.value < n.value).length === this.neighbors.length) return true
        
        return false
    }
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}