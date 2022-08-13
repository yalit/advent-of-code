type Aunt = {
    id: number
    children?: number,
    cats?: number,
    samoyeds?: number 
    pomeranians?: number,
    akitas?: number,
    vizslas?: number,
    goldfish?: number,
    trees?: number,
    cars?: number,
    perfumes?: number
}

const auntInputs = {
    children: 3,
    cats: 7,
    samoyeds: 2,
    pomeranians: 3,
    akitas: 0,
    vizslas: 0,
    goldfish: 5,
    trees: 3,
    cars: 2,
    perfumes: 1
}

function parseAuntDefinition(line: string): Aunt {
    let m = line.match(/Sue.(?<id>\d+):(?<characteristics>.*)/)
    let aunt: Aunt = {id: parseInt(m.groups.id)}

    m.groups.characteristics.split(',').forEach(s => {
        const datas = s.trim().split(':')
        aunt[datas[0]] = parseInt(datas[1].trim())
    })

    return aunt
}

function handleInput_1(lines: Array<string>){
    const aunts = lines.map(parseAuntDefinition)

    let finalAunt = aunts.filter((aunt: Aunt) =>  {
        return Object.keys(auntInputs).reduce((isMatching, input) => {
            return isMatching && ((input in aunt) ? aunt[input] === auntInputs[input] : true)
        }, true)
    })

    return finalAunt[0].id
}

function handleInput_2(lines: Array<string>){
    const aunts = lines.map(parseAuntDefinition)

    let finalAunt = aunts.filter((aunt: Aunt) =>  {
        return Object.keys(auntInputs).reduce((isMatching, input) => {
            let tempIsMatching: boolean = true

            if (!(input in aunt)) {
                return isMatching
            }
            
            if (input === 'cats' || input === 'trees') {
                return isMatching && aunt[input] > auntInputs[input]
            }

            if (input === 'pomeranians' || input === 'goldfish') {
                return isMatching && aunt[input] < auntInputs[input]
            }

            return isMatching && aunt[input] === auntInputs[input]
        }, true)
    })

    return finalAunt[0].id
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}