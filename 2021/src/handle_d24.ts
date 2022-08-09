type Program = Array<string>
type NOMAD = Array<Program>

class ALU {
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    ops = {
        'inp': (v: string, value: number) => this.variables[v] = value,
        'add': (v1: string, v2: string) =>  this.variables[v1] = this.variables[v1] + ((v2 in this.variables) ? this.variables[v2] : parseInt(v2)),
        'mul': (v1: string, v2: string ) => this.variables[v1] = this.variables[v1] * ((v2 in this.variables) ? this.variables[v2] : parseInt(v2)),
        'div': (v1: string, v2: string) => this.variables[v1] = Math.floor(this.variables[v1] / ((v2 in this.variables) ? this.variables[v2] : parseInt(v2))),
        'mod': (v1: string, v2: string) => this.variables[v1] = this.variables[v1] % ((v2 in this.variables) ? this.variables[v2] : parseInt(v2)),
        'eql': (v1: string, v2: string) => this.variables[v1] = (this.variables[v1] === ((v2 in this.variables) ? this.variables[v2] : parseInt(v2))) ? 1 : 0,
    }

    programs: Array<Program> = []

    runNomad(nomad: NOMAD, input: number): number {
        const inputs: Array<number> = input.toString().split('').map(e => parseInt(e))
        console.log(inputs)
        let z: number

        nomad.forEach((program, index) => {
            z = this.runProgram(program, inputs[index])
            console.log(this.variables)
        })

        return z
    }
    
    runProgram(lines: Program, input: number): number {
        lines.forEach((line, index) => {
            this.runInstruction(line, input)
        })

        return this.variables['z']
    }

    runInstruction(line: string, input: number = undefined) {
        const instructions = line.split(' ')

        if (instructions[0] === 'inp') {
            this.ops['inp'](instructions[1], input)
        } else {
            this.ops[instructions[0]](instructions[1], instructions[2])
        }
    }
}

function getNextProgram(lines: Array<string>): Array<string> {  
    let nextProgram = [lines[0]]
    let l = 1
    while (l < lines.length && lines[l].slice(0,3) !== 'inp') {
        nextProgram.push(lines[l])
        l++
    }

    return nextProgram
}

function handleInput_1(lines: Array<string>){
    const alu = new ALU()
    let i = 0
    let z = 0
    let nomad: NOMAD

    while (i < lines.length) {
        let program = getNextProgram(lines.slice(i))
        nomad.push(program)
        i += program.length
    }

    return alu.runNomad(nomad, 99999999999999)
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}