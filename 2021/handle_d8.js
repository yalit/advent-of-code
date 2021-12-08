const numbers = ['abcefg',  'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    

const defaultSizes = sortSizes(numbers.map(n => n.split('')))

function handleInput_1(lines){
    const decryptedLines = lines.map(line => decryptLine(line))
    
    const matched = [1,4,7,8]
    let nbInstancesMatched = 0
    decryptedLines.forEach(line => {
        matched.forEach(m => {
            nbInstancesMatched += getCommon(line, [m]).length
        })
    })

    return nbInstancesMatched
}

function handleInput_2(lines){
    const decryptedLines = lines.map(line => decryptLine(line))
    
    return decryptedLines.reduce((acc, line) => acc + Number(line.join('')), 0)
}

/* extract data from line */
function getSecretsAndInput(line) {
    return line.split(' | ').map(e => e.split(' ').map(f => f.split('').sort()))
}

/* analysis to get the decryption of each input */
function decryptLine(line) {
    const [secrets,input] = getSecretsAndInput(line)
    const mapping = getLineMappingFromSecrets(secrets)

    const convertedInput = input.map(i => convertInput(i, mapping).join('')).map(ci => numbers.indexOf(ci))
    return convertedInput
}

/* convert one input number based on the decyphered mapping */
function convertInput(input, mapping) {
    return input.map(c =>  mapping[c]).sort()
}

/* fetch mapping from secrets */
function getLineMappingFromSecrets(secrets) {
    const sizes = sortSizes(secrets)
    let mapping = {}

    //1. find a
    const a = findA(sizes)
    mapping[a] = 'a'

    //2. get other than a
    const cf = sizes[2][0]

    //3. compare cf to 4
    const bd = unique(sizes[4][0], cf)

    //4. extract unique pairs from 5
    const [one, two] = getUniquePairsFromFives(sizes[5])

    //5. Match one & two with bd to find ef
    let ef = []
    let cb = []
    if (getCommon(bd, one).length === 0) {
        ef = one
        cb = two
    } else {
        ef = two
        cb = one
    }

    //6. match cf and ef
    const f = getCommon(cf, ef)[0]
    const c = cf.filter(char => char !== f)[0]
    const e = ef.filter(char => char !== f)[0]
    const b = cb.filter(char => char !== c)[0]
    const d = bd.filter(char => char !== b)  [0] 
    
    mapping[b] = 'b'
    mapping[c] = 'c'
    mapping[d] = 'd'
    mapping[e] = 'e'
    mapping[f] = 'f'

    //7. get g
    const g = unique(sizes[7][0], Object.keys(mapping))
    mapping[g] = 'g'

    return mapping
}

/* get each secrets sorted by length*/
function sortSizes(numbers) {
    const sizes = {2: [], 3:[], 4:[], 5:[], 6:[], 7:[]}
    numbers.forEach(n => sizes[n.length].push(n))  
    
    return sizes
}

/* a is the unique value in 7 compared to 1 */
function findA(sizes) {
    return unique(sizes[3][0], sizes[2][0])[0]
}

/* get unique data in from compared to comparedTo */
function unique(from, comparedTo) {
    return from.filter(c => !comparedTo.includes(c))
}

/* get unique in boths of the array from one another */
function getUniqueInBoth(one, two) {
    const u1 = unique(one, two)
    const u2 = unique(two, one)
    
    if (u1.length === 1 && u2.length === 1 && u1 !== u2) return [u1[0], u2[0]].sort()

    return null
}

/* get element in two from one */
function getCommon(one, two) {
    return one.filter(c => two.includes(c))
}

/**  
 * 3 fives : acdeg | acdfg | abdfg  
 * from 1 & 2 you can isolate e & f ==> then use with the already mapped ones
 * from 2 & 3 you can isolate b & c ==> then use with the already mapped ones
 */
function getUniquePairsFromFives(fives) {
    const uniques = []

    for (let i = 0; i< fives.length; i++) {
        for (let j = i+1; j<fives.length; j++) {
            const u = getUniqueInBoth(fives[i], fives[j])
            if (u !== null) uniques.push(u)
        }
    }
    return uniques
}

export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}