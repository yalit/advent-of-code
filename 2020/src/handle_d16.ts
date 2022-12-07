import { arraySum, intersection, removeElement, transpose } from "./libraries/array"

interface TicketRange {
    minLow: number,
    maxLow: number,
    minHigh: number,
    maxHigh: number
}

interface TicketRanges {
    [k: string] : TicketRange
}

const getInputData = (lines: Array<string>): {ticketRules: TicketRanges, yourTicket: Array<number>, nearbyTickets: Array<Array<number>>} => {
    let ticketRules: TicketRanges = {}
    let yourTicket: Array<number> = []
    let nearbyTickets: Array<Array<number>> = []

    let currentTreatment = 'ranges'
    lines.forEach(l => {
        if (l === '') {
            return
        }
        if (l.startsWith('your')) {
            currentTreatment = 'your'
            return
        }
        if (l.startsWith('nearby')) {
            currentTreatment = 'nearby'
            return
        }
        if (currentTreatment === 'ranges') {
            const input = l.match(/^(?<ranges>[\w\s]+):.(?<minLow>\d+)-(?<maxLow>\d+).or.(?<minHigh>\d+)-(?<maxHigh>\d+)$/)
            
            ticketRules[input.groups.ranges] = {
                minLow: parseInt(input.groups.minLow),
                maxLow: parseInt(input.groups.maxLow),
                minHigh: parseInt(input.groups.minHigh),
                maxHigh: parseInt(input.groups.maxHigh)
            }
            return
        }
        if (currentTreatment === 'your') {
            yourTicket = l.split(',').map(n => parseInt(n))
            return
        }
        if (currentTreatment === 'nearby') {
            nearbyTickets.push(l.split(',').map(n => parseInt(n)))
        }
    })

    return {ticketRules, yourTicket, nearbyTickets}
}

const isInRange = (range: TicketRange, n: number): boolean => {
    return (n >= range.minLow && n <= range.maxLow) || (n >= range.minHigh && n <= range.maxHigh)
}

const getInvalidValues = (ticketRules: TicketRanges, values: Array<number>): {valid: boolean, invalidValues: Array<number>} =>  {
    let invalidValues = []

    values.forEach(n => {
        if (Object.values(ticketRules).map(rule => !isInRange(rule, n)).every(Boolean)) {
            invalidValues.push(n)
        }
    })

    return {valid: invalidValues.length === 0 ,invalidValues}
}

const getValidRanges = (ticketRanges: TicketRanges, value: number): Array<string> => {
    return Object.keys(ticketRanges).filter(k => isInRange(ticketRanges[k], value))
}

function handleInput_1(lines: Array<string>){
    let {ticketRules, nearbyTickets} = getInputData(lines)
    return nearbyTickets
        .map((ticket: Array<number>) => {
            const {valid, invalidValues} = getInvalidValues(ticketRules, ticket)
            return invalidValues
        })
        .reduce((s: number, invalidValues: Array<number>) => {
            return s + arraySum(invalidValues)
        },0)
    
}

function handleInput_2(lines: Array<string>){
    let {ticketRules, yourTicket, nearbyTickets} = getInputData(lines)
    const validNearbyTickets = nearbyTickets
            .filter(t => getInvalidValues(ticketRules, t).valid)
    
    const transposedNearbyTickets = transpose(validNearbyTickets)
    
    //map all valid rules per column in tickets
    let mappedColumns = {}
    transposedNearbyTickets.forEach((col: Array<number>, k: number) => {
        mappedColumns[k] = col.reduce((validRanges: Array<string>, n: number, idx: number) => {
            if (idx === 0) {
                return getValidRanges(ticketRules, n)
            }
            return intersection(validRanges, getValidRanges(ticketRules, n) )
        }, [])
    })
    
    const haveColumnsUniqueRules = (columns) => Object.values(columns).filter((c: Array<string>) => c.length > 1).length === 0

    //match the rules to the column
    let matched = []
    while (!haveColumnsUniqueRules(mappedColumns)) {
        //get the column keys not yet matched sorted based on the length of their mapped rules (always one with a single rule)
        const sortedColumnsKeys = Object.keys(mappedColumns)
                .sort((a, b) => mappedColumns[a].length - mappedColumns[b].length)
                .filter(k => mappedColumns[k].length > 1 || !matched.includes(mappedColumns[k][0]))

        const currentRule = mappedColumns[sortedColumnsKeys[0]][0] //this one is single and not matched

        //remove the rule from all other mapped rules in the columns
        sortedColumnsKeys.forEach((k, idx) => {
            if (mappedColumns[k].length > 1) {
                mappedColumns[k] = removeElement(mappedColumns[k], currentRule)
            }
        })
        matched.push(currentRule)
    }

    //keep only the departure columns and multiply the values from your ticket
    return Object.keys(mappedColumns).filter(k => mappedColumns[k][0].startsWith('departure')).map(n => yourTicket[parseInt(n)]).reduce((m,n) => m * n,1)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}