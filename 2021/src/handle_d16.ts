import { parse } from "path/posix"

function parseHexa(line: string): Array<string> {
    return line.split('').map(c => parseInt(c, 16).toString(2).padStart(4, '0')).join('').split('')
}

type DataType = 'version' | 'type' | 'literal' | 'opLength' | 'opTypeLength' | 'operator' | 'end'

function getData(s: Array<string>, pos: number, type: DataType): string {
    const datasize = {
        'version': 3,
        'type': 3,
        'literal': 5,
        'end': pos % 16
    }

    return s.slice(pos, pos + datasize[type]).join('')
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
            return 'operator'
    }
}

function handleInput_1(line: string){
    const bin: Array<string> = parseHexa(line)
    console.log(bin.join(''));
    
    let i = 0
    let currentType: DataType = 'version'
    let currentData: string

    let versions: Array<number> = []

    while (i < bin.length) {
        currentData = getData(bin, i, currentType)
        
        if (currentType === 'version') versions.push(parseInt(currentData, 2))

        currentType = getNextType(currentType, currentData)
        i += currentData.length
    }

    return versions
}

function handleInput_2(line: string){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines[0]), handleInput_2(lines[0])]
}