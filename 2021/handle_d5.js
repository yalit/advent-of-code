function handleInput_1(lines){
    let increase = 0
    lines.forEach((element, k) => {
        increase += k!==0 && element > lines[k-1]
    });
    return increase
}

function handleInput_2(lines){
    let measurements = []

    measurements = lines.reduce((acc, elem, k) =>  {
        if (k > lines.length-3) return acc
        acc.push(sumMeasures(lines.slice(k, k+3)))
        return acc
    }, [])

    return handleInput_1(measurements)
}

function sumMeasures(measures){
    return measures.reduce((acc, measure) => acc + measure, 0)
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}