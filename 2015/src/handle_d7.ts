interface Grid {
    [key: number]: number
}

class Value {
    a: string 
    b: string
    constructor(a: string, b: string = null){
        this.a = a
        this.b = b
    }
}

class Instruction {
    to: string
    value: Value
    instruction: (grid: Grid, value: Value) => number

    constructor(line: string){
        let [instr, to] = line.split(' -> ')
        this.to = to
        this.instruction = this.actions['assign']
        let instrData = instr.split(' ')
        switch (instrData.length) {
            case 1:
                this.value = new Value(instrData[0])
                break
            case 2:
                this.instruction = this.actions['NOT']
                this.value = new Value(instrData[1])
                break
            case 3:
                this.instruction = this.actions[instrData[1]]
                this.value = new Value(instrData[0], instrData[2])
                break
        }
    }
       
    actions: {[key: string]: (grid: Grid, value: Value) => number} =  {
        'assign': (grid, value) => Number(value.a),
        'NOT':  (grid, value) => ~grid[value.a],
        'AND': (grid, value) => grid[value.a] & grid[value.b],
        'OR': (grid, value) => grid[value.a] | grid[value.b],
        'LSHIFT': (grid, value) => grid[value.a] << Number(value.b),
        'RSHIFT': (grid, value) => grid[value.a] >> Number(value.b),
    }

    getResult = function(grid: Grid) {
        let result = this.instruction(grid, this.value)
        
        if (result < 0) result += 65536
        if (result >= 65536) result -= 65536
        
        return result
    }
}

function handleInput_1(lines: Array<string>){
    const grid: Grid = {}

    let instruction: Instruction
    lines.forEach(line => {
        instruction = new Instruction(line)
        grid[instruction.to] = instruction.getResult(grid)
    });
    return grid[instruction.to]
}

function handleInput_2(lines: Array<string>){
    return 0
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}