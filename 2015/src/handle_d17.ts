function handleInput_1(lines: Array<string>){
    let data: number[] = []
    lines.forEach((line) => {data.push(+line) })

    let comb = combinations(data, 150)

    return comb.length
}

function handleInput_2(lines: Array<string>){
    let data: number[] = []
    lines.forEach((line) => {data.push(+line) })

    let comb = new Set(combinations(data, 150))
    let min = Infinity

    comb.forEach(s => min = s.length < min ? s.length : min)
    return Array.from(comb).filter(a => a.length == min).length
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}

function combinations(array, sum) {
  return new Array(1 << array.length).fill("").map(
    (e1, i) => array.filter((e2, j) => i & 1 << j))
      .filter(a => a.reduce((s,a) => s +a, 0) === sum);
}