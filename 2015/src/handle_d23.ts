type Operation = {action: string, register: string, value: number}

const getRegisters = (lines: Array<string>, a: number) => {
    let registers = {a, b: 0}
    let operations: Array<Operation> = lines.map(line => {
        let [action, register, value] = line.replace("\r", "").replace(",", "").split(' ')
        if (action === 'jmp') {
            return {action, register: '', value: parseInt(register)}
        }
        return {action, register, value: parseInt(value)}
    })
    let index = 0

    while (index < operations.length) {
        const operation = operations[index]
        if (operation.action === 'hlf') {
            registers[operation.register] /= 2
            index++
            continue
        }
        if (operation.action === 'tpl') {
            registers[operation.register] *= 3
            index++
            continue
        }
        if (operation.action === 'inc') {
            registers[operation.register]++
            index++
            continue
        }
        if (operation.action === 'jmp') {
            index += operation.value
            continue
        }
        if (operation.action === 'jie') {
            if (registers[operation.register] % 2 === 0) {
                index += operation.value
            } else {
                index++
            }
            continue
        }
        if (operation.action === 'jio') {
            if (registers[operation.register] === 1) {
                index += operation.value
            } else {
                index++
            }
            continue
        }
    }
    return registers
}
function handleInput_1(lines: Array<string>){
    return getRegisters(lines, 0).b
}

function handleInput_2(lines: Array<string>){
    return getRegisters(lines, 1).b
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}