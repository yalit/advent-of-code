const get_Rules = (lines: Array<string>) => {
    const rules = new Map()
    let i = 0
    while (lines[i] !== '') {
        const [key, value] = lines[i].split(': ')
        rules.set(key, value)
        i++
    }
    return rules
}

const get_regex = (rules: Map<string, string>, key: string, full: boolean = true): RegExp => {
    let re = ''

    const get_rule = (key: string): string => {
        const rule = rules.get(key)
        if (rule.match(/"[a-z]"/)) {
            return rule[1]
        }
        return `(${rule.split(' | ').map(r => r.split(' ').map(k => get_rule(k)).join('')).join('|')})`
    }

    return new RegExp(`${full ? '^' : ''}${get_rule(key)}${full ? '$' : ''}`)
}

function handleInput_1(lines: Array<string>){
    const split = lines.indexOf('')
    const rules = get_Rules(lines)

    const regex = get_regex(rules, '0')
    return lines.slice(split + 1).filter(l => regex.test(l)).length
}

function handleInput_2(lines: Array<string>){
    const split = lines.indexOf('')
    const rules = get_Rules(lines)

    // change is that rule 8 is now 42 | 42 8 and rule 11 is 42 31 | 42 11 31
    // this means that rule 0 is now 8 11
    rules.set('8', '42 | 42 8')
    rules.set('11', '42 31 | 42 11 31')

    // so it means that we always need at least 2 42's and 1 31 timed n times
    // and that you'll have all 42 at the beginning and all 31 at the end
    // so let's compute the regex for 42 and 31
    const regex_42 = get_regex(rules, '42', false)
    const regex_31 = get_regex(rules, '31', false)

    return lines.slice(split + 1).filter(l => {
        let n42 = 0
        let n31 = 0
        let i = 0
        let m = l.match(regex_42)
        while (m && m.index === 0) {
            n42++
            i += m[0].length
            m = l.slice(i).match(regex_42)
        }
        m = l.slice(i).match(regex_31)
        while (m && m.index === 0) {
            n31++
            i += m[0].length
            m = l.slice(i).match(regex_31)
        }
        return n42 > n31 && n31 > 0 && i === l.length
    }).length
}

export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}