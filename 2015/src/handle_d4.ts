const md5 = require('js-md5')

function handleInput_1(key: string){
    let n = 1
    let c = md5(key+n.toString())

    while(c.slice(0,5) !== '00000') {
        n++
        c = md5(key+n.toString())
    }
    return n
} 

function handleInput_2(key: string){
    let n = 1
    let c = md5(key+n.toString())
    
    while(c.slice(0,6) !== '000000') {
        n++
        c = md5(key+n.toString())
    }
    return n
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines[0]), handleInput_2(lines[0])]
}