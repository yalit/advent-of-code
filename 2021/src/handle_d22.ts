type Bounds = {min: number, max: number}
type Action = 'on' | 'off'

const intersectPlane = (b1: Bounds, b2: Bounds): boolean => {
    return (b1.min === b2.min) 
        || (b1.max === b2.max) 
        || (b2.min <= b1.min && b2. max >= b1.min)
        || (b2.min > b1. min && b2.max < b1.max)
        || (b2.max > b1.max && b2.min < b1.max)
}

class Cube {
    X: Bounds
    Y: Bounds
    Z: Bounds

    constructor(bounds: Array<Bounds> = null) {
        if (bounds){
            this.X = bounds[0]
            this.Y = bounds[1]
            this.Z = bounds[2]
        }
    }

    nbCubes = () => {
        return (this.X.max - this.X.min + 1) * (this.Y.max - this.Y.min + 1) * (this.Z.max - this.Z.min + 1)
    }

    intersect = (cube: Cube): boolean => {
        return intersectPlane(cube.X, this.X) && intersectPlane(cube.Y,this.Y) && intersectPlane(cube.Z, this.Z)
    }

    inside = (cube: Cube): boolean => {
        return this.X.min >= cube.X.min && this.X.max <= cube.X.max && this.Y.min >= cube.Y.min && this.Y.max <= cube.Y.max && this.Z.min >= cube.Z.min && this.X.max <= cube.Z.max
    }

    getOuterBlocks = (cube: Cube): Array<Cube> => {
        let cubes: Array<Cube> = []

        const getBounds = (base: Bounds, compare: Bounds): Array<Bounds> => {
            let bounds: Array<Bounds> = []

            if (!intersectPlane(base, compare)) {
                return []
            }
            
            if (compare.min >= base.min && compare.min <= base.max) {
                bounds.push({min: base.min, max: compare.min - 1})
                bounds.push({min: compare.min, max: base.max})
            }

            if (compare.max >= base.min && compare.max <= base.max) {
                bounds.push({min: compare.max + 1, max: base.max})
                bounds.push({min: base.min, max: compare.max})
            }

            return bounds
        }

        let boundX = getBounds(this.X, cube.X)
        let boundY = getBounds(this.Y, cube.Y)
        let boundZ = getBounds(this.Z, cube.Z)

        boundX.forEach((x: Bounds) => {
            cubes.push(new Cube([x, this.Y, this.Z]))
        })

        boundY.forEach((y: Bounds) => {
            cubes.push(new Cube([this.X, y, this.Z]))
        })

        boundZ.forEach((z: Bounds) => {
            cubes.push(new Cube([this.X, this.Y, z]))
        })

        return cubes
    }
}

function parseInitLine(line: string): [Action, Array<Bounds>] {
    const lSplit = line.split(' ')
    const matches = lSplit[1].split(',')
    
    const bounds = matches.map(m => {
        const s = m.split("=")[1].split('..')
        return {min: (+s[0] < -50) ? -50 : +s[0], max: (+s[1] > 50) ? 50 : +s[1]}
    })

    return [lSplit[0] as Action, bounds]
}

function parseRebootLine(line: string): [Action, Cube] {
    const lSplit = line.split(' ')
    const matches = lSplit[1].split(',')
    
    const bounds: Array<Bounds> = matches.map(m => {
        const s = m.split("=")[1].split('..')
        return {min: +s[0], max: +s[1]}
    })

    return [lSplit[0] as Action, new Cube(bounds)]
}

function handleInput_1(lines: Array<string>){
    let reactor = {}

    lines.forEach(line => {
        const [action, [X, Y, Z]] = parseInitLine(line)
        
        for (let x = X.min; x <= X.max; x++) {
            for (let y = Y.min; y <= Y.max; y++) {
                for (let z = Z.min; z <= Z.max; z++) {
                    const index = x + "-" + y + "-" + z
                    if (action === 'on') {
                        reactor[index] = true
                    } else {
                        reactor[index] = false
                    }
                }
            }
        }
    })
    return Object.values(reactor).filter(v => v).length
}

function handleInput_2(lines: Array<string>){
    let reactorCubesOn: Array<Cube> = []

    lines.forEach(line => {
        const [action, cube] = parseRebootLine(line)
        let noIntersect = []
        reactorCubesOn.forEach((cubeOn: Cube) => {
            if (!cubeOn.intersect(cube)) {
                noIntersect.push(cubeOn)
                return
            }

            if (cubeOn.inside(cube)) {
                return
            } 

            const outerBlocks = cubeOn.getOuterBlocks(cube)
            if (outerBlocks.length > 0) {
                noIntersect.concat(outerBlocks)
            }
        })
        
        if (action === 'on') noIntersect.push(cube)
        reactorCubesOn = [...noIntersect]
    })

    return reactorCubesOn.reduce((s: number, c: Cube) =>  s + c.nbCubes() , 0)
}


export function handleInput(lines: Array<string>) {
    console.log("Started Part 1 : "+ new Date());
    const part1 = handleInput_1(lines)
    console.log("Ended Part 1 : "+ new Date());
    console.log("Result part 1 : ", part1);
    
    console.log("Started Part 2 : "+ new Date());
    const part2 = handleInput_2(lines)
    console.log("Started Part 2 : "+ new Date());
    console.log("Result part 2 : ", part2);
}