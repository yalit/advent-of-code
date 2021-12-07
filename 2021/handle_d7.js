import { plotLine } from "./plot.js"
import _ from 'lodash'

function handleInput_1(lines){
    const numbers = lines[0].split(',').map(a => parseInt(a)).sort((a,b) => a-b)    
    const ground = getMedian(numbers)

    return getSimpleCostNumbers(numbers, ground)
}

function handleInput_2(lines){
    const numbers = lines[0].split(',').map(a => parseInt(a)).sort((a,b) => a-b)

    //Brute-Force
    /* const costsForEach = getCostsForEach(numbers)
    const cost = costsForEach.sort((a,b) => a.cost - b.cost)[0] */

    //use of mass center
    const ground = getCenterOfMass(numbers)

    return getAccumulativeCostNnumber(numbers, ground)
}

function getPointsMasses(numbers) {
    const masses = {}
    numbers.forEach(d => {
        masses[d] = masses[d] ? masses[d]+1 : 1
    })

    return masses //number of points at a position x
}

function getMedian(numbers) {
    return numbers[Math.round(numbers.length/2)]
}

function getCenterOfMass(numbers) {
    const masses = getPointsMasses(numbers)
    const ponderedMass = Object.keys(masses).reduce((a,x) => a +(x*masses[x]),0)
    console.log('pondered Mass : '+ponderedMass)

    return Math.floor(ponderedMass/numbers.length)
}

function getCostsForEach(numbers) {
    let costs = _.range(0, numbers.length)
    costs = costs.map(pos => {
        return {
            pos,
            cost: _.sum(numbers.map(n => getNSum(Math.abs(pos-n))))
        }
    })
    return costs
}

function getSimpleCostNumbers(numbers, ground) {
    numbers = numbers.map(n => Math.abs(ground - n))
    return _.sum(numbers)
}

function getAccumulativeCostNnumber(numbers, ground) {
    numbers = numbers.map(n => getNSum(Math.abs(ground - n)))
    return _.sum(numbers)
}

function getNSum(n) {
    return _.sum(_.range(1,n+1))
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}