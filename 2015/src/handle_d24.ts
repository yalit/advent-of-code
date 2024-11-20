const sum = (arr: Array<number>) => arr.reduce((a, b) => a + b)
const quantumEntanglement = (arr: Array<number>) => arr.reduce((a, b) => a * b, 1)

const k_combinations = (set: Array<number>, k: number) => {
    let i, j, combs, head, tailcombs

    if (k > set.length || k <= 0) {
        return []
    }

    if (k === set.length) {
        return [set]
    }

    if (k === 1) {
        combs = []
        for (i = 0; i < set.length; i++) {
            combs.push([set[i]])
        }
        return combs
    }

    combs = []
    for (i = 0; i < set.length - k + 1; i++) {
        head = set.slice(i, i + 1)
        tailcombs = k_combinations(set.slice(i + 1), k - 1)
        for (j = 0; j < tailcombs.length; j++) {
            combs.push(head.concat(tailcombs[j]))
        }
    }
    return combs
}

const getLowestQE = (lines: Array<string>, groups: number) => {
    const weights = lines.map(Number)
    const targetSum = sum(weights) / groups

    let found: Array<Array<number>> = []

    for (let i = 1; i < weights.length; i++) {
        const combs = k_combinations(weights, i)
        for (let comb of combs) {
            if (sum(comb) === targetSum) {
                found.push(comb)
            }
        }
        if (found.length > 0) {
            break
        }
    }
    found.sort((a,b) => quantumEntanglement(a) - quantumEntanglement(b))

    return quantumEntanglement(found[0])
}

function handleInput_1(lines: Array<string>){
    return getLowestQE(lines, 3)
}

function handleInput_2(lines: Array<string>){
    return getLowestQE(lines, 4)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}