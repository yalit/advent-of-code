import {isText} from "./libraries/types";

const getRules = (lines: Array<string>) => {
    const rules = {}

    const getRuleDetails = (rule: string) => {
        if (rule[0] === '"') {
            return rule[1]
        } else {
            return parseInt(rule)
        }
    }

    lines.forEach(line => {
        const [key, value] = line.split(': ')
        const elements = value.split(' | ').map(v => v.split(' ').map(getRuleDetails))
        rules[parseInt(key)] = elements
    })
    return rules
}

const matchMessage = (message: string, rules: any, rule: Array<number|string>, position: number = 0) => {
    if (position === message.length) {
        return true
    }

    if (rule.length === 0) {
        return false
    }

    let valid = false
    const element = rule[0]
    if (isText(element)){
        if (element === message[position]) {
            valid = matchMessage(message, rules, rule.slice(1), position+1)
        } else{
            valid = false
        }
    } else {
        const newRules = rules[element]
        for (let newRule of newRules) {
            valid = matchMessage(message, rules, newRule.concat(rule.slice(1)), position)
            if (valid) {
                break
            }
        }
    }
    return valid
}


function handleInput_1(lines: Array<string>){
    const split = lines.indexOf('')
    const rules = getRules(lines.slice(0, split))

    const messages = lines.slice(split+1)
    return messages.filter(m => matchMessage(m, rules, rules[0][0])).length
}

function handleInput_2(lines: Array<string>){
    const split = lines.indexOf('')
    const rules = getRules(lines.slice(0, split))
    const messages = lines.slice(split+1)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    console.log(rules)

    // const tobefound = [
    //     'bbabbbbaabaabba',
    //     'babbbbaabbbbbabbbbbbaabaaabaaa',
    //     'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
    //     'bbbbbbbaaaabbbbaaabbabaaa',
    //     'bbbababbbbaaaaaaaabbababaaababaabab',
    //     'ababaaaaaabaaab',
    //     'ababaaaaabbbaba',
    //     'baabbaaaabbaaaababbaababb',
    //     'abbbbabbbbaaaababbbbbbaaaababb',
    //     'aaaaabbaabaaaaababaa',
    //     'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
    //     'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'
    // ]
    // console.log(messages.filter(m => matchMessage(m, rules, rules[0][0])).filter(m => !tobefound.includes(m)))
    return messages.filter(m => matchMessage(m, rules, rules[0][0])).length
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}