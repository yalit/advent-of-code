import { link } from "fs"
import { isInteger, uint16 } from "./helpers"

type instruction = {
    'action': string,
    'to': string,
    'inputs': Array<string>
}

class Wire {
    name: string
    value: number | Operation | Wire
    actualValue: number

    constructor(name: string) {
        this.name = name
    }

    getValue(): number {
        if (this.actualValue !== undefined) {
            return this.actualValue
        }

        let value: number
        if (this.value instanceof Operation) {
             value = this.value.getResult()
        } else if (this.value instanceof Wire) {
            value = this.value.getValue()
        } else {
            value = this.value
        }

        this.actualValue = value
        return value
    }

    reset() {
        this.actualValue = undefined
    }
}

class Operation {
    action: string
    valueA: number | Wire
    valueB: number | Wire | undefined

    actions = {
        'SET': () => this.getValue(this.valueA),
        'AND': () => uint16(this.getValue(this.valueA) & this.getValue(this.valueB)),
        'OR': () => uint16(this.getValue(this.valueA) | this.getValue(this.valueB)),
        'LSHIFT': () =>  uint16(this.getValue(this.valueA) << this.getValue(this.valueB)),
        'RSHIFT': () =>  uint16(this.getValue(this.valueA) >> this.getValue(this.valueB)),
        'NOT': () => uint16(~ this.getValue(this.valueA))
    }

    constructor(action: string) {
        this.action = action
    }

    getResult(): number {
        return this.actions[this.action]()
    }

    setValues(values: Array<number|Wire>): void {
        this.valueA = values[0]

        if(values.length > 1) {
            this.valueB = values[1]
        }
    }

    getValue(a: number | Wire): number {
        if (a instanceof Wire) {
            return a.getValue()
        } else {
            return a
        }
    }

}

class Circuit {
    wires = {}
    inputs: Array<Wire> = []

    constructor(lines: Array<string>) {
        lines.forEach(line => {
            let instruction = this.readInputLine(line)
            this.setupWire(instruction)
        })
    }

    reset() {
        Object.keys(this.wires).forEach(k => this.wires[k].reset())
    }
    
    getWireValue(name: string): number {
        if (! (name in this.wires)) {
            throw `This wire does not exist in the circuit : ${name}`
        }

        return this.wires[name].getValue()
    }

    setupWire(instruction: instruction): void {
        let wire = this.getWire(instruction.to)

        const firstInput = instruction.inputs[0]

        if (instruction.action === 'SET') {
            wire.value = (isInteger(firstInput))? parseInt(firstInput) : this.getWire(firstInput)
            this.wires[instruction.to] = wire

            if (isInteger(firstInput)) {
                this.inputs.push(wire)
            }

            return
        } 

        let op = new Operation(instruction.action)        
        let opValues: Array<number|Wire> = []
        
        if (isInteger(firstInput)) {
            opValues.push(parseInt(firstInput))
        } else {
            let valueWire = this.getWire(firstInput)
            opValues.push(valueWire)
        }
        
        if (instruction.inputs.length > 1) {
            const secondInput = instruction.inputs[1]
            if (isInteger(secondInput)) {
                opValues.push(parseInt(secondInput))
            } else {
                let valueWire = this.getWire(secondInput)
                opValues.push(valueWire)
            }
        }
        
        op.setValues(opValues)
        wire.value = op
        this.wires[instruction.to] = wire
    }

    getWire(name: string): Wire {
        if (name in this.wires) {
            return this.wires[name]
        } else {
            this.wires[name] = new Wire(name)
            return this.getWire(name)
        }
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
    let circuit = new Circuit(lines)
    
    return circuit.getWireValue('a')
}

function handleInput_2(lines: Array<string>){
    let circuit = new Circuit(lines)
    let temp = circuit.getWireValue('a')
    circuit.reset()
    circuit.wires['b'].actualValue = temp
    
    return circuit.getWireValue('a')
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}