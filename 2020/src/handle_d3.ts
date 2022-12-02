function getNbTreesFromFall(lines: Array<Array<string>>, rightStep: number, downStep: number): number {
    const getNextXPosition = (start: number): number => {
        return (start + rightStep) % lines[0].length
    }

    let level = 0
    let nbTrees = 0
    let xPosition = 0
    while (level < lines.length) {
        nbTrees += lines[level][xPosition] === '#' ? 1 : 0
        xPosition = getNextXPosition(xPosition)
        level += downStep
    }
    return nbTrees
}

function handleInput_1(lines: Array<Array<string>>){
    return getNbTreesFromFall(lines, 3, 1)
}

function handleInput_2(lines: Array<Array<string>>){
    const nbTrees = [[1,1], [3,1], [5,1], [7,1], [1,2]].map(([rightStep, downStep]:[number, number]) => getNbTreesFromFall(lines, rightStep, downStep))
    return nbTrees.reduce((acc: number, elem: number) => acc*elem, 1)
}


export function handleInput(lines: Array<string>) {
    const input = lines.map(l => l.split(''))
    return [handleInput_1(input), handleInput_2(input)]
}