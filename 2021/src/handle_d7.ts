import { _ } from 'lodash'

function handleInput_1(lines: Array<string>){
    const numbers: Array<number> = lines[0].split(',').map(a => Number(a)).sort((a,b) => a-b)    
    
    const ground:number = getMedian(numbers)

    return getSimpleCostNumbers(numbers, ground)
}

function handleInput_2(lines: Array<string>){
    const numbers: Array<number> = lines[0].split(',').map(a => Number(a)).sort((a,b) => a-b)

    //use of mass center
    const ground: number = getCenterOfMass(numbers)

    return getAccumulativeCostNnumber(numbers, ground)
}

interface Masses {
    [key: number]: number
}

function getPointsMasses(numbers: Array<number>): Masses {
    const masses: Masses = {}
    numbers.forEach((d: number) => {
        masses[d] = masses[d] ? masses[d]+1 : 1
    })

    return masses //number of points at a position x
}

function getMedian(numbers: Array<number>): number {
    return numbers[Math.round(numbers.length/2)]
}

function getCenterOfMass(numbers: Array<number>): number {
    const masses: Masses = getPointsMasses(numbers)
    const ponderedMass = Object.keys(masses).reduce((a,x) => a + (Number(x) * masses[x]), 0)

    return Math.floor(ponderedMass/numbers.length)
}

function getSimpleCostNumbers(numbers: Array<number>, ground: number): number {
    numbers = numbers.map(n => Math.abs(ground - n))
    return _.sum(numbers)
}

function getAccumulativeCostNnumber(numbers: Array<number>, ground: number): number {
    numbers = numbers.map(n => getNSum(Math.abs(ground - n)))
    return _.sum(numbers)
}

function getNSum(n: number): number {
    return _.sum(_.range(1,n+1))
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}