function isPasswordOK(a: Array<number>): boolean {
    return isOkForFirst(a) && isOkForSecond(a) && isOkForThird(a)
} 

function isOkForFirst(s: Array<number>): boolean {
    let i = 0
    let isPasswordOK = false
    while (i < s.length-3) {
        if (!isPasswordOK) {
            isPasswordOK = s[i+1] === s[i]+1 && s[i+2] === s[i]+2
        }
        i++
    }
    return isPasswordOK
}

function isOkForSecond(s: Array<number>): boolean {
    let isPasswordOK = true
    let impossibleChars = [8,11,14]

    impossibleChars.forEach(n => {
        if(isPasswordOK) {
            isPasswordOK =  s.indexOf(n) === -1
        }
    })

    return isPasswordOK
}

function isOkForThird(s: Array<number>): boolean {
    let a = transformBackToString(s)
    const m = a.match(/(\w)\1/g)
    let isPasswordOK = m !== null && m.length >= 2
    
    return isPasswordOK 
}

function transformString(s: string): Array<number> {
    return s.split('').map(c => c.charCodeAt(0)-97)
}

function transformBackToString(a: Array<number>): string {
    return a.map(n => String.fromCharCode(n+97)).join('')
}

function getNextPasssword(a: Array<number>): Array<number> {
    let i = 1
    let newPasswordFound = false
    let newPassword = [...a]
    while (!newPasswordFound && i < a.length) {
        let newChar = (a[a.length-i] + 1) % 26
        newPassword[a.length-i] = newChar

        if (newChar > 0) {
            newPasswordFound = true
        }

        i++
    }

    return newPassword
}

function handleInput_1(s: string){
    let a = transformString(s)
    let isPassOK = false
    let newPassword: Array<number> = a
    
    while (!isPassOK) {
        newPassword = getNextPasssword(newPassword)
        isPassOK = isPasswordOK(newPassword)
    }

    return transformBackToString(newPassword)
}

function handleInput_2(s: string){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines[0]), handleInput_2(lines[0])]
}