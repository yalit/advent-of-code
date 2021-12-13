function handleInput_1(lines: Array<string>){
    let x: number = 0, y: number = 0

    const actions = {
        forward: (dist: number) => x += dist,
        down: (dist: number) => y += dist,
        up: (dist: number) => y -= dist
    }

    lines.forEach(element => {
        const [action, dist] = element.split(" ")
        actions[action](Number(dist))
    });

    return x * y
}

function handleInput_2(lines: Array<string>){
    let x: number = 0, y: number = 0, aim: number = 0

    const actions = {
        forward: (dist: number) => {
            x += dist
            y += (aim * dist)
        },
        down: (dist: number) => aim += dist,
        up: (dist: number) => aim -= dist
    }

    lines.forEach(element => {
        const [action, dist] = element.split(" ")
        actions[action](Number(dist))
    });

    return x * y
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}