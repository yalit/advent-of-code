import { arraySum } from "./libraries/array"

const switchChar = (word: string, n: number, value: string) => {
    let tw = word.split('')
    tw[n] = value
    return tw.join('')
}

const getAllFloatingCombinations = (mask: string, i: number, combinations = []) => {
    if (i === mask.length) {
        return [...combinations, mask]
    }
    if (mask.slice(i, i+1) !== 'X') {
        return [...combinations, ...getAllFloatingCombinations(mask, i+1, combinations)]
    }
    return [...combinations, ...getAllFloatingCombinations(switchChar(mask, i, '0'), i + 1, combinations), ...getAllFloatingCombinations(switchChar(mask, i, '1'), i + 1, combinations)]
}

function handleInput_1(lines: Array<string>){
    let mask = ''
    let memory = {}

    const applyMask = (mask: string, n: number) => {
        const m = mask.split('')
        const apply = {
            'X': (n: string) => n,
            '1': (n: string) => '1',
            '0': (n: string) => '0'
        }
        return parseInt((n >>> 0).toString(2).padStart(36, '0').split('').map((e: string, idx: number) => apply[m[idx]](e)).join(''), 2)
    }

    lines.forEach(l => {
        if (l.slice(0,4) === 'mask') {
            mask = l.slice(7)
            return
        }
        const maskInput = l.match(/^mem\[(?<id>\d+)\].=.(?<number>\d+)$/)
        memory[maskInput.groups.id] = applyMask(mask, parseInt(maskInput.groups.number))
    })
    return arraySum(Object.values(memory))
}

function handleInput_2(lines: Array<string>){
    let mask = ''
    let memory = {}

    const applyMaskToMemory = (mask: string, n: number) => {
        const m = mask.split('')
        const apply = {
            'X': (n: string) => 'X',
            '1': (n: string) => '1',
            '0': (n: string) => n
        }
        return (n >>> 0).toString(2).padStart(36, '0').split('').map((e: string, idx: number) => apply[m[idx]](e)).join('')
    }
    
    lines.forEach(l => {
        if (l.slice(0,4) === 'mask') {
            mask = l.slice(7)
            return
        }
        const input = l.match(/^mem\[(?<id>\d+)\].=.(?<number>\d+)$/)
        const floatingMemory = applyMaskToMemory(mask, parseInt(input.groups.id))
        getAllFloatingCombinations(floatingMemory, 0, []).forEach(m => {
            memory[parseInt(m, 2)] = parseInt(input.groups.number)
        });
    })
    
    return arraySum(Object.values(memory))
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}