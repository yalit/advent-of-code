function Value(a, b = null) {
    this.a = a
    this.b = b
}

function Instruction(line) {
    const actions =  {
        'assign': (grid, value) => Number(value.a),
        'NOT':  (grid, value) => ~grid[value.a],
        'AND': (grid, value) => grid[value.a] & grid[value.b],
        'OR': (grid, value) => grid[value.a] | grid[value.b],
        'LSHIFT': (grid, value) => grid[value.a] << Number(value.b),
        'RSHIFT': (grid, value) => grid[value.a] >> Number(value.b),
    }

    let [instr, to] = line.split(' -> ')
    this.to = to
    this.instruction = actions['assign']

    let instrData = instr.split(' ')
    switch (instrData.length) {
        case 1:
            this.value = new Value(Number(instrData[0]))
            break
        case 2:
            this.instruction = actions['NOT']
            this.value = new Value(instrData[1])
            break
        case 3:
            this.instruction = actions[instrData[1]]
            this.value = new Value(instrData[0], instrData[2])
            break
    }

    this.getResult = function(grid) {
        let result = this.instruction(grid, this.value)
        
        if (result < 0) result += 65536
        if (result >= 65536) result -= 65536
        
        return result
    }
}

function handleInput_1(lines){
    const grid = {}

    let instruction
    lines.forEach(line => {
        instruction = new Instruction(line)
        grid[instruction.to] = instruction.getResult(grid)
        console.log(instruction, )
    });
    return grid[instruction.to]
}

function handleInput_2(lines){
    return 0
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}