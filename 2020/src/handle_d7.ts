interface ContentBag {
    nb: number,
    name: string
}
interface Rule {
    contain: {[k: string]: ContentBag},
    inside: Array<string>
}

interface Rules {
    [k: string] : Rule
}

const insideRegexp = /^(?<nb>[0-9]+).(?<name>[\w\s]+).?$/

function addContainer(rules: Rules, container: string, inside: Array<string>): Rules {
    if (!(container in rules)) {
        rules[container] = {contain: {}, inside: []}
    }

    inside.forEach(elem => {
        const v = elem.match(insideRegexp)
        if (v === null) {
            return
        }
        const insideName = parseInt(v.groups.nb) === 1 ? v.groups.name.trim() : v.groups.name.trim().slice(0,-1)
        if (!(insideName in rules[container].contain)) {
            rules[container].contain[insideName] = {nb: parseInt(v.groups.nb), name: insideName}
        }

        if (! (insideName in rules)) {
            rules[insideName] = {contain: {}, inside: []}
        }
        if (!rules[insideName].inside.includes(container)){
            rules[insideName].inside.push(container)
        }
    })

    return {...rules}
}


function getRules(lines: Array<string>): Rules {
    let rules = {}

    lines.forEach(l => {
        let [container, inside] = l.split(' contain ')
        container = container.slice(-1) === 's' ? container.slice(0,-1) : container
        rules = addContainer(rules, container, inside.split(', '))
    })

    return rules
}

function findContainerBags(bag: string, rules: Rules, bags: Array<string>): Array<string> {
    let updatedBags = [...bags]
    rules[bag].inside.forEach(container => {
        if (!bags.includes(container)) {
            updatedBags = findContainerBags(container, rules, [...updatedBags, container])
        }
    })

    return updatedBags
}

function findContainingBags(bag: string, rules: Rules, containingBags: Array<string>): number {
    let nbBags = 0
    Object.keys(rules[bag].contain).forEach(key => {
        const inside = rules[bag].contain[key]

        if(!containingBags.includes(inside.name)){
            nbBags += inside.nb +(inside.nb * findContainingBags(inside.name, rules, [...containingBags, inside.name]))
        }
    })

    return nbBags
}

function handleInput_1(lines: Array<string>){
    const rules: Rules = getRules(lines)    
    return new Set(findContainerBags('shiny gold bag', rules, [])).size
}

function handleInput_2(lines: Array<string>){
    const rules: Rules = getRules(lines)

    return findContainingBags('shiny gold bag', rules, [])
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}