function handleInput_1(lines: Array<number>){
    lines.sort((a, b) => a-b)

    let diff = {1: 0, 2: 0, 3: 1}
    let previous = 0
    lines.forEach(l => {
        diff[l-previous] += 1
        previous = l
    })
    console.log(diff)
    return diff[1] * diff[3]
}

function handleInput_2(adapters: Array<number>){
    adapters.push(0)
    adapters.sort((a, b) => a-b)
    adapters.push(adapters[adapters.length -1] + 3)
    let tree = {}
    adapters.forEach(a => {
        let j = []
        for (let i = 1; i <= 3; i++) {
            if (adapters.includes(a + i)) {
                j.push(a+i)
            }
            tree[a] = [...j]
        }
    })
    let visited = {}
    const dfc = (t, v) => {
        if (v in visited) {
            return visited[v]
        } else if (t[v].length > 0) {
            visited[v] = t[v].reduce((s, tv) => s + dfc(t, tv) ,0)
            return visited[v]
        } else {
            return 1
        }
    }      

    return dfc(tree, 0)
}


export function handleInput(lines: Array<string>) {
    const data = lines.map(x => parseInt(x))
    return [handleInput_1(data), handleInput_2(data)]
}