function findDuoCompanion(base: number, target: number, elements: Array<number>): Array<number> {
    if (base + elements[0] === target) {
        return [base, elements[0]]
    }
    if (base + elements[0] > target || elements.length === 1) {
        return [base, 0]
    }

    const companion: Array<number> = findDuoCompanion(base, target, elements.slice(1)) 

    if (companion[1] !== 0) {
        return companion
    }

    return findDuoCompanion(elements[0], target, elements.slice(1))
}
function findTrioCompanion(base: number, target: number, elements: Array<number>): Array<number> {
    const duoCompanions = findDuoCompanion(elements[0], target - base, elements.slice(1))
    if (duoCompanions[1] !== 0) {
        return [base, ...duoCompanions]
    }
    if (elements.length === 2) {
        return [base, 0, 0]
    }

    const companions = findTrioCompanion(base, target, elements.slice(1))

    if (companions[1] !== 0) {
        return companions
    }

    return findTrioCompanion(elements[0], target, elements.slice(1))
}

function handleInput_1(lines: Array<number>){
    lines.sort((a: number, b: number) => a-b)
    return findDuoCompanion(lines[0], 2020, lines.slice(1)).reduce((acc: number, elem: number) => acc * elem, 1)
}

function handleInput_2(lines: Array<number>){
    lines.sort((a: number, b: number) => a-b)

    return findTrioCompanion(lines[0], 2020, lines.slice(1)).reduce((acc: number, elem: number) => acc * elem, 1)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines.map(l => parseInt(l, 10))), handleInput_2(lines.map(l => parseInt(l, 10)))]
}