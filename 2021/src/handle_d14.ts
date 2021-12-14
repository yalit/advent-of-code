interface Rule {
    value: string,
    toInsert: string
}

interface RuleList {
    [key: string]: Rule
}

interface Occurence {
    value: string, 
    occurences: number
}

interface OccurenceList {
    [key: string]: Occurence
}

interface Change {
    input: string,
    characterToInsert: string
}

function handleInput_1(lines: Array<string>, nbSteps: number = 1){
    let word: string = lines[0]

    let rules: RuleList = {}
    for (let i = 2; i < lines.length; i++) {
        const rule = getRule(lines[i])
        rules[rule.value] = rule
    }
    
    let a: number = 0
    let couplesOccurences: OccurenceList
    let characterOccurences: OccurenceList
    [couplesOccurences, characterOccurences] = getWordOccurences(word)

    while (a < nbSteps) {    
        [couplesOccurences, characterOccurences] = applyChanges(couplesOccurences, characterOccurences, rules)        
        a++
    }
    
    return getDeltaMaxAndMinCharacterOccurences(characterOccurences)
}

function handleInput_2(lines: Array<string>){
    return handleInput_1(lines, 40)
}

function getRule(line: string): Rule {
    const infos: Array<string> = line.split(' -> ')

    return {
        value: infos[0],
        toInsert: infos[1]
    }
}

function getWordOccurences(word: string): [OccurenceList, OccurenceList] {
    let occurenceList: OccurenceList = {}
    let characterOccurences: OccurenceList = {}
    const wSplit = word.split('')

    wSplit.forEach((c: string, k: number) => {

        if(!characterOccurences[c])characterOccurences[c] = {value: c, occurences: 0}
        characterOccurences[c].occurences++

        if (k >= wSplit.length - 1) return

        const input = wSplit.slice(k, k+2).join('')
        if (!occurenceList[input]) occurenceList[input] = {value: input, occurences: 0}
        occurenceList[input].occurences++
    })

    return [occurenceList, characterOccurences]
}

function applyChanges(couplesOccurences: OccurenceList, characterOccurences: OccurenceList, rules: RuleList): [OccurenceList, OccurenceList] {
    let newCouplesOccurences: OccurenceList = {}
    let newCharacterOccurences: OccurenceList = {...characterOccurences} 

    Object.keys(couplesOccurences).forEach((input: string) => {
        const [nc1, nc2, change]: [string, string, Change] = getNewCouples(input, rules) 
        const nbAdditions = couplesOccurences[input].occurences

        if (!newCouplesOccurences[nc1]) newCouplesOccurences[nc1] = {value: nc1, occurences: 0}
        newCouplesOccurences[nc1].occurences += nbAdditions
        if (!newCouplesOccurences[nc2]) newCouplesOccurences[nc2] = {value: nc2, occurences: 0}
        newCouplesOccurences[nc2].occurences += nbAdditions

        if (!newCharacterOccurences[change.characterToInsert]) newCharacterOccurences[change.characterToInsert] = {value: change.characterToInsert, occurences: 0}
        newCharacterOccurences[change.characterToInsert].occurences += nbAdditions
    })

    return [newCouplesOccurences, newCharacterOccurences]
}

function getNewCouples(input: string, rules: RuleList): [string, string, Change]{
    //Assumption that there is a rule for any of the possible character couples
    const iSplit = input.split('')
    const characterToInsert = rules[input].toInsert
    return[iSplit[0] + characterToInsert, characterToInsert + iSplit[1], {input, characterToInsert}]
}

function getDeltaMaxAndMinCharacterOccurences(characterOccurences: OccurenceList): number {
    const max: number = Object.values(characterOccurences).reduce((maxValue: number, occurence: Occurence) => (occurence.occurences > maxValue) ? occurence.occurences : maxValue, 0)
    const min = Object.values(characterOccurences).reduce((minValue: number, occurence: Occurence) => (occurence.occurences < minValue) ? occurence.occurences : minValue, max)

    return max - min
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines, 10), handleInput_2(lines)]
}