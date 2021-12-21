import { threadId } from "worker_threads"

type Side = 'left' | 'right' | 'top'
class Pair {
    level: number
    parent: Pair | null
    left: number | Pair = null
    right: number | Pair = null
    hasLevel4pairs = () => this.level === 4
    side: Side = null

    constructor(level: number = 0, parent: Pair = null) {
        this.level = level
        this.parent = parent
    }

    display = function(d: string = '') {
        if (Number.isInteger(this.left) && Number.isInteger(this.right)){
            return '[' + (this.level === 4 ? 'l' + String(this.level) + ': ' : '') + String(this.left) + ',' + String(this.right) + ']'
        } else if (Number.isInteger(this.left)) {
            return '[' + (this.level === 4 ? 'l' + String(this.level) + ': ' : '') + String(this.left) + ',' + this.right.display(d) + ']'
        } else if (Number.isInteger(this.right)) {
            return '[' + (this.level === 4 ? 'l' + String(this.level) + ': ' : '') + this.left.display(d) + ',' + String(this.right) + ']'
        } else {
            return '[' + (this.level === 4 ? 'l' + String(this.level) + ': ' : '') + this.left.display(d) + ',' + this.right.display(d) + ']'
        }
    }

    setLevel(level: number) {
        this.level = level
        if (this.left instanceof Pair) {
            this.left.setLevel(this.level + 1)
        }
        if (this.right instanceof Pair) {
            this.right.setLevel(this.level + 1)
        }
    }

    setLeftPair = function(pair: Pair) {
        this.left = pair
        pair.side = 'left'
        pair.parent = this
        this.left.setLevel(this.level + 1)
    }

    setRightPair = function(pair: Pair) {
        this.right = pair
        pair.side = 'right'
        pair.parent = this
        this.right.setLevel(this.level + 1)
    }

    addToLeftFirstRegular = function (value: number, side: string) {
        if (side === 'right' && Number.isInteger(this.left)) {
            this.left += value
        }
        else if (side === 'right') {
            this.left.addToLeftFirstRegular(value, 'top')
        }
        else if (side === 'left' && this.parent !== null) {
            this.parent.addToLeftFirstRegular(value, this.side)
        }
        else if (side === 'top' && Number.isInteger(this.right)) {
            this.right += value
        }
        else if (side === 'top') {
            this.right.addToLeftFirstRegular(value, 'top')
        }
    }   

    addToRightFirstRegular = function (value: number, side: string) {
        if (side === 'left' && Number.isInteger(this.right)) {
            this.right += value
        }
        else if (side === 'left') {
            this.right.addToRightFirstRegular(value, 'top')
        }
        else if (side === 'right' && this.parent !== null) {
            this.parent.addToRightFirstRegular(value, this.side)
        }
        else if (side === 'top' && Number.isInteger(this.left)) {
            this.left += value
        }
        else if (side === 'top') {
            this.left.addToRightFirstRegular(value, 'top')
        }
    }   

    explode = function(): boolean {
        if (Number.isInteger(this.left) && Number.isInteger(this.right)) {
            if (this.hasLevel4pairs()) {
                this.doExplode()
                return true
            } else {
                return false
            }
        } else {
            if (this.left instanceof Pair) {
                const exploded = this.left.explode()
                if (exploded) {
                    return true
                }
            }
            if (this.right instanceof Pair) {
                const exploded = this.right.explode()
                if (exploded) {
                    return true
                }
            }
            return false
        }
    }

    doExplode = function() {
        this.parent.addToLeftFirstRegular(this.left, this.side)
        this.parent.addToRightFirstRegular(this.right, this.side)
        if (this.side === 'left') this.parent.left = 0
        if (this.side === 'right') this.parent.right = 0
    }

    split = function(): boolean {
        if (Number.isInteger(this.left) && this.left > 9) {
            let pair = new Pair(this.level + 1, this)
            pair.left = Math.floor(this.left / 2)
            pair.right = Math.ceil(this.left / 2)
            this.setLeftPair(pair)
            return true
        }
        if (Number.isInteger(this.right) && this.right > 9) {
            let pair = new Pair(this.level + 1, this)
            pair.left = Math.floor(this.right / 2)
            pair.right = Math.ceil(this.right / 2)
            this.setRightPair(pair)
            return true
        }
        if (this.left instanceof Pair) {
            if (this.left.split()) {
                return true
            }
        }
        if (this.right instanceof Pair) {
            if (this.right.split()) {
                return true
            }
        }
        return false
    }

    reduce = function(): boolean {
        let hasChanged = this.explode()
        if (hasChanged) {
            console.log("Exploded : " + this.display())
            return true
        }

        hasChanged = this.split()
        if (hasChanged) {
            console.log("Splitted : " + this.display())
            return true
        }

        return false
    }

    getMagnitude = function(): number {
        let leftMagnitude: number
        if (Number.isInteger(this.left)) {
            leftMagnitude = 3 * this.left
        } else {
            leftMagnitude = 3 * this.left.getMagnitude()
        }

        let rightMagnitude: number
        if (Number.isInteger(this.right)) {
            rightMagnitude = 2 * this.right
        } else {
            rightMagnitude = 2 * this.right.getMagnitude()
        }

        return leftMagnitude + rightMagnitude
    }
}

function parseLine(line: string): Pair {
    let currentPair: Pair = null
    let side = 'left'
    let i = 0

    while(i < line.length){
        switch(line.slice(i,i+1)){
            case '[':
                let pair = new Pair(currentPair === null ? 0 : currentPair.level + 1 , currentPair)
                currentPair = pair
                side = 'left'
                break
            case ']':
                if (currentPair.parent === null) {
                    break;
                }
                if (line.slice(i+1,i+2) === ',') {
                    currentPair.parent.left = currentPair
                    currentPair.side = 'left'
                } else {
                    currentPair.parent.right = currentPair
                    currentPair.side = 'right'
                }
                currentPair = currentPair.parent
                break
            case ',':
                side = 'right'
                break
            default: //Number
                let value = Number(line.slice(i,i+1))
                if(line.slice(i+1,i+2).match(/\d/) !== null) {
                    value = Number(line.slice(i,i+2))
                    i++
                }
                if (side === 'left') currentPair.left = value
                else currentPair.right = value
                break
        }
        i++
    }

    return currentPair
}

function handleInput_1(lines: Array<string>){
    let pairs: Array<Pair> = lines.map(l => parseLine(l))

    while (pairs.length > 1) {
        let newPair = new Pair()
        newPair.setLeftPair(pairs[0])
        newPair.setRightPair(pairs[1])
        console.log(newPair.display())
        let hasBeenReduced = newPair.reduce()
        while (hasBeenReduced) {
            hasBeenReduced = newPair.reduce()
        }
        console.log("####################");
        console.log("New Reduce");
        console.log("####################");
        pairs = [newPair].concat(pairs.slice(2))
    }

    console.log(pairs[0].display())

    return pairs[0].getMagnitude()
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}