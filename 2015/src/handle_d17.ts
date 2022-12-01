let allCombinations = []

function getAllCombinations(liters: number, containers: Array<number>, combination: Array<number>) {
    if (liters === 0) {
        if (allCombinations.indexOf(combination.join('-')) === -1) {
            allCombinations.push(combination.join('-'))
        }
        return
    }

    if (containers.length === 0) {
        return   
    }

    for (let i = 0; i < containers.length; i++) {
        let newContainers = containers.slice(i+1)
        if (liters < containers[i]) {
            getAllCombinations(liters, newContainers, combination)
        } else {
            let newCombination = [...combination]
            newCombination.push(containers[i])
            getAllCombinations(liters-containers[i], newContainers, newCombination)
        }
    }
}

function handleInput_1(lines: Array<string>){
    const containers = lines.map(line => parseInt(line)).sort((a,b) => b-a)
    getAllCombinations(150,containers,[])
    console.log(allCombinations);
    
    return allCombinations.length
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}