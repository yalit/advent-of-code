function handleInput_1(lines: Array<string>){
    return getNiceWords(lines).length
} 

function handleInput_2(lines: Array<string>){
    return getReallyNiceWords(lines).length
}

function getNiceWords(lines: Array<string>) {
    const rVowels = /((a|e|i|o|u)\w*(a|e|i|o|u)\w*(a|e|i|o|u))/g
    const rRepeat = /(\w)\1+/g    
    const rForbidden = /(ab|cd|pq|xy)/g
    
    return lines
        .filter(w => w.match(rVowels) !== null)
        .filter(w => w.match(rRepeat) !== null)
        .filter(w => w.match(rForbidden) === null)
    ;
}

function getReallyNiceWords(lines: Array<string>) {
    const rOneBetween = /(\w).\1/g
    const rRepeatNoOverlap = /(\w{2}).*(\1)/g
    return lines
        .filter(w => w.match(rOneBetween) !== null)
        .filter(w => w.match(rRepeatNoOverlap) !== null)
    ;
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}