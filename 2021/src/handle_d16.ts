let executionDisplay: string

class Instructions {
    versions: Array<number> = []
    instructions: Array<Instruction> = []
    currentInstruction: Instruction

    createNewInstruction(): Instruction {
        this.currentInstruction = new Instruction()
        this.currentInstruction.type = 'main'
        this.instructions.push(this.currentInstruction)
        return this.currentInstruction
    }

}

class Instruction {
    type: PacksetType
    operator: Operator
    instructions: Array<Instruction> = []
    literalValue: string = ''

    setOperator(type: number) {
        this.operator = new Operator(type)
    }

    addLiteral(l :string) {
        this.literalValue += l
    }

    addInstruction(instruction: Instruction) {
        this.instructions.push(instruction)
    }

    execute(): number {
        if (this.operator.type === 'literal') {
            return parseInt(this.literalValue, 2)
        }          
        const result = this.operator.execute(this.instructions)
        return result
    }
}

class Value {
    value:  number
    constructor(value: number) {
        this.value = value
    }
}

type OperatorType = 'sum' | 'product' | 'minimum' | 'maximum' | 'greaterThan' | 'lessThan' | 'equalTo' | 'literal'

class Operator {
    type: OperatorType
    
    types: {[key: number]: OperatorType}= {
        0: 'sum',
        1: 'product',
        2: 'minimum',
        3: 'maximum',
        4: 'literal',
        5: 'greaterThan',
        6: 'lessThan',
        7: 'equalTo'
    }

    constructor(value: number) {
        this.type = this.types[value]
    }

    execute(instructions: Array<Instruction>): number {
        let a: number
        let b: number
        switch(this.type){
            case 'greaterThan':
            case 'lessThan':
            case 'equalTo':
                a = instructions[0] ? instructions[0].execute() : null
                b = instructions[1] ? instructions[1].execute() : null
                break;
        }

        switch (this.type) {
            case 'sum':
                return instructions.reduce((s: number, i: Instruction) => s + i.execute(), 0)
            case 'product':
                return instructions.reduce((s: number, i: Instruction) => s * i.execute(), 1)
            case 'minimum':
                return instructions.reduce((min: number, i: Instruction) => Math.min(min, i.execute()), Infinity)
            case 'maximum':
                return instructions.reduce((max: number, i: Instruction) => Math.max(max, i.execute()), 0)
            case 'greaterThan':
                return ( a > b) ? 1 : 0
            case 'lessThan':
                return ( a < b) ? 1 : 0
            case 'equalTo':
                return ( a === b) ? 1 : 0
        }
    }
}

type PacksetType = 'main' | 'sub'
type DataType = 'version' | 'type' | 'literal' | 'opLength' | 'opTypeLength' | 'subpacket' | 'end'
type SubPacksetSize = {
    type: 'length' | 'occurences',
    value: number
}

function parseHexa(line: string): Array<string> {
    return line.split('').map(c => parseInt(c, 16).toString(2).padStart(4, '0')).join('').split('')
}

function getDataSize(s: Array<string>, pos: number, type: DataType, opLengthSize: number = 0): number {
    const datasize = {
        'version': 3,
        'type': 3,
        'literal': 5,
        'end': (pos % 8 === 0) ? 0 : 8 - (pos % 8),
        'opTypeLength': 1,
        'opLength': opLengthSize,
        'subpacket': 0
    }

    return datasize[type]
}

function getData(s: Array<string>, pos: number, type: DataType, opLengthSize: number): string {
    return s.slice(pos, pos + getDataSize(s, pos, type, opLengthSize)).join('')
}

function getNextType (type: DataType, data: string): DataType {
    switch(type){
        case 'version':
            return 'type'
        case 'type':
            switch(parseInt(data, 2)){
                case 4:
                    return 'literal'
                default:
                    return 'opTypeLength'
            }
        case 'literal':
            if (data.slice(0,1) === '0') return 'end'
            else return 'literal'
        case 'end':
            return 'version'
        case 'opTypeLength':
            return 'opLength'
        case 'opLength':
            return 'subpacket'
        case 'subpacket':
            return 'end'
    }
}

function handlePacket(instructions: Instructions,  s: Array<string>, pos: number, packsetType: PacksetType, instruction: Instruction): number {
    let i = pos
    let currentType: DataType = 'version'
    let currentData: string
    let currentDataValue: number
    let opLengthSize: number = 0
    let subPacksetsEnd: SubPacksetSize
    
    if (packsetType === 'main' && currentType === 'version') console.log("Main packset...");
    

    while (currentType !== 'end') {
        currentData = getData(s, i, currentType, opLengthSize)
        
        currentDataValue = parseInt(currentData, 2)

        if (currentType === 'version' && currentDataValue !== 0) instructions.versions.push(currentDataValue)
        if (currentType === 'type') instruction.setOperator(currentDataValue)
        if (currentType === 'literal') instruction.addLiteral(currentData.slice(1))
        if (currentType === 'opTypeLength') (currentDataValue === 0) ? opLengthSize = 15 : opLengthSize = 11
        if (currentType === 'opLength' && opLengthSize === 15) subPacksetsEnd = {type: 'length', value: i + currentData.length + currentDataValue}
        if (currentType === 'opLength' && opLengthSize === 11) subPacksetsEnd = {type: 'occurences', value: currentDataValue}
        if (currentType === 'subpacket') {

            let currentNbSubPackset = 0
            while ((subPacksetsEnd.type === 'length' && i < subPacksetsEnd.value) || (subPacksetsEnd.type == 'occurences' && currentNbSubPackset < subPacksetsEnd.value)){
                let subInstruction = new Instruction()
                subInstruction.type = 'sub'
                i += handlePacket(instructions, s.slice(i), 0, 'sub', subInstruction)
                currentNbSubPackset++
                instruction.addInstruction(subInstruction)
            }
        } else {
            i += currentData.length
        }

        currentType = getNextType(currentType, currentData)
    }

    return i + ((packsetType === 'main') ? getDataSize(s, i, currentType) : 0) //to add the size of 'end' bytes at the end of the packet only at the end of the main packset
}

function handleInput_1(line: string){
    const bin: Array<string> = parseHexa(line)
    let instructions = new Instructions()
    executionDisplay = ''
    
    let i = 0
    while (i < bin.length){
        let instruction = instructions.createNewInstruction()
        i = handlePacket(instructions, bin, i, 'main', instruction)
    }    

    return instructions.versions.reduce((sum: number, n: number) => sum + n, 0)
}

function handleInput_2(line: string){
    const bin: Array<string> = parseHexa(line)
    let instructions = new Instructions()
    executionDisplay = ''
    let i = 0
    while (i < bin.length){
        let instruction = instructions.createNewInstruction()        
        i = handlePacket(instructions, bin, i, 'main', instruction)
    }    
    console.log(executionDisplay)
    return Number(instructions.instructions.map(i => i.execute()).join(''))
}


export function handleInput(lines: Array<string>) {
    return handleInput_2(lines[0])
}