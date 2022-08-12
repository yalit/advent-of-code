function parseStringLiteral(s: string): number {
   s = s.slice(1,s.length-1) //remove beginning and end "

    let i: number = 0
    let stringCharactersCount: number = 0
    let escapeFound: boolean = false
    while (i < s.length) {
        let char = s[i]
        if (!escapeFound && char !== "\\") {
            stringCharactersCount++
            i++ 
        } else if(!escapeFound && char === "\\") {
            escapeFound = true
            i++
        } else if (char === "\"" || char === "\\") {
            stringCharactersCount++
            escapeFound = false
            i++
        } else if (char === "x") {
            stringCharactersCount++
            escapeFound = false
            i += 3
        } else {
            throw `Not possible to arrive here : ${s} / ${i} / ${char}`
        }
    }

    return s.length + 2 - stringCharactersCount
}

function parseStringLiteral_2(s: string): number {
    s = s.slice(1,s.length-1) //remove beginning and end "
 
     let i: number = 0
     let addedEncodingChars: number = 0
     let escapeFound: boolean = false
     while (i < s.length) {
         let char = s[i]
         if (!escapeFound && char !== "\\") {
             i++ 
         } else if(!escapeFound && char === "\\") {
             escapeFound = true
             addedEncodingChars++
             i++
         } else if (char === "\"" || char === "\\") {
             addedEncodingChars++
             escapeFound = false
             i++
         } else if (char === "x") {
             escapeFound = false
             i += 3
         } else {
             throw `Not possible to arrive here : ${s} / ${i} / ${char}`
         }
     }
 
     return 4 + addedEncodingChars
 }

function handleInput_1(lines: Array<string>){
    const results = lines.map(parseStringLiteral)
    console.log(results);
    
    return results.reduce((s: number, x:number) => s+x,0)
}

function handleInput_2(lines: Array<string>){
    const results = lines.map(parseStringLiteral_2)
    console.log(results);
    
    return results.reduce((s: number, x:number) => s+x,0)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}