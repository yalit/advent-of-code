type Person = {
    name: string,
    gainLosses: {[k: string]: number}
}

function parseLinesToPersons(lines: Array<string>): {[k: string]: Person} {
    const matcher = /(\w+).would.(gain|lose).(\d+) happiness units by sitting next to (\w+)/
    let persons: {[k: string]: Person} = {}

    lines.forEach(line => {
        const m = line.match(matcher)
        let type = m[2]
        let amount = parseInt(m[3])
        const benefactor = m[1]
        const contributor = m[4]

        if (benefactor in persons) {
            persons[benefactor].gainLosses[contributor] = amount * ((type === 'gain')? 1 : -1)
        } else {
            let gainLosses = {}
            gainLosses[contributor] = amount * ((type === 'gain')? 1 : -1)
            persons[benefactor] = { name: benefactor, gainLosses}
        }
    })
        
    return persons
}

function getSumofHappiness(a: Array<string>, persons: {[k: string]: Person}): number {
    return a.reduce((s, p, k) => {
        const left = persons[p].gainLosses[a[(k-1 < 0) ? a.length + k-1 : k-1]]
        const right = persons[p].gainLosses[a[(k+1) % a.length]]
        return s + left + right
    }, 0)
}

function allPermutations(array) {
    function p(array, temp) {
        var i, x;
        if (!array.length) {
            result.push(temp);
        }
        for (i = 0; i < array.length; i++) {
            x = array.splice(i, 1)[0];
            p(array, temp.concat(x));
            array.splice(i, 0, x);
        }
    }

    var result = [];
    p(array, []);
    return result;
}

function handleInput_1(lines: Array<string>){
    const persons = parseLinesToPersons(lines)
    return Math.max(...allPermutations(Object.keys(persons)).map(p => getSumofHappiness(p, persons)))
}

function handleInput_2(lines: Array<string>){
    const persons = parseLinesToPersons(lines)

    // add me
    let me: Person = {name: 'me', gainLosses: {}}
    Object.keys(persons).forEach(p => {
        me.gainLosses[p] = 0
        persons[p].gainLosses['me'] = 0
    })
    persons['me'] = me
    const permutations = allPermutations(Object.keys(persons))
    
    let max = 0

    permutations.forEach(p => {
        let maxtemp = getSumofHappiness(p, persons)
        max = Math.max(max, maxtemp)
    })

    return max
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}