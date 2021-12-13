import {_} from 'lodash'

const newBornDays: number = 8
const resetDays: number = 6

function handleInput_1(line: Array<string>, nbDays: number = 80){
    let population = setUpPopulation(line[0].split(','))
    
    let nbRemainingDays = nbDays
    while (nbRemainingDays > 0) {
        population = getNewPopulationAfterANight(population)
        nbRemainingDays--
    }

    return getPopulationSize(population)
}

/**
 * Population = {0: #nb lanternfish @0day}
 */
interface Population {
    [key: number]: number
}
function getZeroedPopulation(): Population {
    let elems: Population = {}
    _.range(0,newBornDays+1).forEach((n: number) => elems[n] = 0)

    return elems
}

function setUpPopulation(elements: Array<string>): Population {
    let elems: Population = getZeroedPopulation()

    elements.forEach((e: string) => elems[Number(e)] += 1)

    return elems
}

function getPopulationSize(population: Population) {
    return Object.values(population).reduce((s,n) => s + n, 0)
}

function getNewPopulationAfterANight(population: Population): Population {
    const newPopulation: Population = getZeroedPopulation()

    Object.keys(population).forEach(d =>  {
        const n: number = Number(d)
        if (n === 0){
            newPopulation[resetDays] = population[0]
            newPopulation[newBornDays] = population[0]
        } else {
            newPopulation[n-1] += population[n]
        }
    })

    return newPopulation
}

export function handleInput(line: Array<string>) {
    return [handleInput_1(line), handleInput_1(line, 256)]
}