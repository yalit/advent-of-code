function handleInput_1(lines: Array<string>){
    let gamma: number
    let epsilon: number

    let mapped = []
    lines.forEach((line, k) => {
        if (k ===0 ){
            mapped = line.split('').map(d => [d])
            return
        }

        line.split('').forEach((element, k) => {
            mapped[k].push(element)
        });
    });

    gamma = parseInt(mapped.map(elems => findMostCommonBit(elems)).join(''), 2)
    epsilon = parseInt(mapped.map(elems => findLeastCommonBit(elems)).join(''), 2)

    return gamma * epsilon
}


function handleInput_2(lines: Array<string>){
    let oxygen: Array<string> = lines, co2: Array<string> = lines
    let n: number = 0

    while (oxygen.length > 1 && n < lines[0].length){
        let bits = getNthBitsFromElements(oxygen, n)
        oxygen = rating(oxygen, n, findMostCommonBit(bits))
        n++
    }
    let oxygenLevel: number = parseInt(oxygen[0], 2)

    n = 0
    while (co2.length > 1 && n < lines[0].length){
        let bits = getNthBitsFromElements(co2, n)
        co2 = rating(co2, n, findLeastCommonBit(bits))
        n++
    }
    let co2Level = parseInt(co2[0], 2)

    return oxygenLevel * co2Level
}

function rating(elements: Array<string>, bitPosition: number, value: string): Array<string>{
    return elements.filter(elem => elem.split('')[bitPosition] === value)
}


function getNthBitsFromElements(elements: Array<string>, n: number): Array<string>{
    return elements.map(elem => elem.split('')[n])
}

function findMostCommonBit(elements: Array<string>): '1' | '0' {
    let common = 0
    elements.forEach(element => {
        if (element === '0') common -=1
        else if (element === '1') common +=1
    });

    return (common >= 0) ? '1' : '0'
}

function findLeastCommonBit(elements: Array<string>): '1' | '0' {
    let common = 0
    elements.forEach(element => {
        if (element === '0') common +=1
        else if (element === '1') common -=1
    });

    return (common > 0) ? '1' : '0'
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}