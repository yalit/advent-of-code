type Operation = 'nop' | 'acc' | 'jmp'

interface Instruction {
    operation: Operation,
    argument: number
}

interface Processor {
    line: number,
    accumulator: number,
    executedLines: Array<number>,
    infinite: boolean
}

function getInstruction(line: string): Instruction {
    const data =line.split(' ')

    return {
        operation: data[0] as Operation,
        argument: parseInt(data[1])
    }
}

const handleInstruction: {[k in Operation]: (p: Processor, instruction: Instruction) => Processor} = {
    nop: (p: Processor, instruction: Instruction) => {return {...p, line: p.line+1}},
    jmp: (p: Processor, instruction: Instruction) => {return {...p, line: p.line + instruction.argument}},
    acc: (p: Processor, instruction: Instruction) => {return {...p, line: p.line+1, accumulator: p.accumulator + instruction.argument}},
}

function runProgram(processor: Processor, lines: Array<Instruction>): Processor {
    while (!processor.executedLines.includes(processor.line) && processor.line < lines.length) {
        processor.executedLines.push(processor.line)
        const instruction: Instruction = lines[processor.line]
        processor = handleInstruction[instruction.operation](processor, instruction)        
    }

    if (processor.line >= lines.length) {
        processor.infinite = false
    }

    return processor
}

function initProcessor(): Processor {
    return {line: 0, accumulator: 0, executedLines: [], infinite: true}
}

function handleInput_1(lines: Array<Instruction>){
    let processor: Processor = initProcessor()
    return runProgram(processor, lines).accumulator
}

function handleInput_2(initialLines: Array<Instruction>){
    const switchOperation = (operation: Operation) : Operation => {
        return operation === 'nop' ? 'jmp' : 'nop'
    }
    
    let lineToChange = 0
    let processor: Processor
    while (processor === undefined || processor.infinite) {
        let lines = initialLines.map(x => {return {...x}})
        if (lines[lineToChange].operation !== 'acc') {
            processor = initProcessor()
            lines[lineToChange].operation = switchOperation(lines[lineToChange].operation)
            processor = runProgram(processor, lines)
        }
        lineToChange++
    }

    return processor.accumulator
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines.map(getInstruction)), handleInput_2(lines.map(getInstruction))]
}