class Point {
    constructor(x, y) {
        this.x = x
        this.y = y
    }

    equals = function(point) {
        return this.x === point.x && this.y === point.y
    }
}

class Grid{
    points

    hasPoint = function(point) {
        return points.filter(p === p.equals(point)).length !== 0
    }

    addPoint = function(point) {
        if (!this.hasPoint(point)) {
            points.push(point)
        }
    }

    get columns() {
        let columns = {}
        this.points.forEach(point => {
            if (!columns[point.y]) columns[point.y] = []
            columns[point.y].push(point)
        });
        
        return Object.keys(columns).sort((a,b) => a-b).map(k => columns[k])
    }

    get column(n) {
        return this.columns[n]
    }

    get rows() {

    }

    get row(n) {
        return this.columns()[n]
    }

}