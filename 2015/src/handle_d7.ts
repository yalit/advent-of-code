import { isInteger, uint16 } from "./helpers"

type instruction = {
    'action': string,
    'to': string,
    'inputs': Array<string>
}

class Grid {
    operations = {
        'SET': (a: number) => a,
        'AND': (a: number, b: number) => uint16(a & b),
        'OR': (a: number, b: number) => uint16(a | b),
        'LSHIFT': (a: number, nb: number) =>  uint16(a << nb),
        'RSHIFT': (a: number, nb: number) =>  uint16(a >> nb),
        'NOT': (a: number) => uint16(~ a)
    }

    wires = {}

    setup(lines: Array<string>): void {
        lines.forEach(line => {
            let instruction = this.readInputLine(line)
            
        })
    }

    readInputLine(line: string): instruction {
        let instruction: instruction = {action: 'SET', to: '', inputs: []}
        let regex = line.match(/[a-zA-Z0-9]+/g)

        instruction.to = regex[regex.length - 1]
        
        let inputs = regex.slice(0, -1)
        if (inputs.length === 1) {
            instruction.inputs = inputs
        } else if(inputs.length === 2) {
            instruction.action = inputs[0]
            instruction.inputs = inputs.slice(1)
        } else {
            instruction.action = inputs[1]
            instruction.inputs = inputs.slice(0,1).concat(inputs.slice(2))
        }

        return instruction
    }
}


function handleInput_1(lines: Array<string>){
    return 0
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}