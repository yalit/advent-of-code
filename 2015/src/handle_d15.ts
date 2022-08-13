type Ingredient = {
    name: string,
    capacity: number,
    durability: number,
    flavor: number,
    texture: number,
    calories: number
}

function parseLine(line: string): Ingredient {
    const m = line.match(/^(?<name>\w+): capacity (?<capacity>-?\d+), durability (?<durability>-?\d+), flavor (?<flavor>-?\d+), texture (?<texture>-?\d+), calories (?<calories>-?\d+)$/)
    
    return {
        name: m.groups.name,
        capacity: parseInt(m.groups.capacity),
        durability: parseInt(m.groups.durability),
        flavor: parseInt(m.groups.flavor),
        texture: parseInt(m.groups.texture),
        calories: parseInt(m.groups.calories),
    }
}

function getCookieScore(pct: Array<number>, ingredients: Array<Ingredient>, withCalories: boolean = false): number {
    let characteristics = ['capacity', 'durability', 'flavor', 'texture']

    let score = characteristics.reduce((strength, c) => {
        const charStrength = ingredients.reduce((temp, ingredient, index) => temp + ingredient[c] * pct[index] ,0)
        return strength * ((charStrength < 0) ? 0 : charStrength)
    }, 1)

    if (withCalories){
        const scoreCalories = ingredients.reduce((temp, ingredient, index) => temp + ingredient['calories'] * pct[index] ,0)
        score *= (scoreCalories === 500) ? 1 : 0
    }

    return score
}

function getMaxScore(lines: Array<string>, withCalories: boolean = false): number {
    const ingredients = lines.map(parseLine)
    const n = 2

    let max = -1
    let mpct: Array<number>
    for (let a = 0; a <= 100; a++) {
        for (let b = 0; b <= 100 - a; b++) {
            for (let c = 0; c <= 100 - a -b; c++) {
                
                const tempStrength = getCookieScore([a, b, c, 100-a-b-c], ingredients, withCalories)
                if (tempStrength > max ){
                    mpct = [a, b, c, 100-a-b-c]
                }
                max = Math.max(max, tempStrength)
            }
        }
    }
    console.log(mpct);
    
    return max
}

function handleInput_1(lines: Array<string>){
    return getMaxScore(lines)
}

function handleInput_2(lines: Array<string>){
    return getMaxScore(lines, true)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}