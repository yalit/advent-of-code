import { _ } from 'lodash'
import { start } from 'repl'

const getPositions = (lines: Array<string>): [number, number] => {
    return [Number(lines[0].split(' ').reduce((_,c) => c,'')), Number(lines[1].split(' ').reduce((_,c) => c,''))]
}

function handleInput_1(lines: Array<string>){
    let p: [number, number] = getPositions(lines)
    let s = [0,0]
    let die = _.range(101).slice(1)
    let turn = 0
    while (s[0] < 1000 && s[1] < 1000) {
        const startRoll = (turn * 3) % 100
        const endRoll = (((turn * 3) % 100) + 3) % 100
        let rolls = die.slice(startRoll, endRoll)
        if (startRoll > endRoll) {
            rolls = die.slice(startRoll)
            rolls = rolls.concat(die.slice(0, endRoll))
        }

        const roll = (_.sum(rolls)) % 10
        p[turn % 2] = p[turn % 2] + roll <= 10 ? p[turn % 2] + roll : p[turn % 2] + roll - 10
        s[turn % 2] += p[turn % 2]
        turn++
    }

    if (s[0] < s[1]) {
        return s[0] * turn * 3
    } else {
        return s[1] * turn * 3
    }
}

type Data = {
    turn: number,
    rolls: Array<number>,
    positions: [number, number],
    scores: [number, number]
}

function handleInput_2(lines: Array<string>){
    let positions: Array<number> = getPositions(lines)
    const nbWins: Array<number> = [0,0]
    let scores: Array<number> = [0,0]

    let gameCounts = {
        [[positions, scores].join(';')]: 1,
    };

    const players = [0,1]
    const rolls = [1,2,3]

    while(Object.entries(gameCounts).length > 0) {
        for (const p of players) {
            let newGameCounts = {}
            for (const [state, gameCount] of Object.entries(gameCounts)) {
                [positions, scores] = state
                  .split(';')
                  .map((s) => s.split(',').map(Number))

                for (const r1 of rolls) {
                    for (const r2 of rolls) {
                        for (const r3 of rolls) {
                            const nextPosition = [...positions]
                            nextPosition[p] = ((nextPosition[p] + r1 + r2 + r2 -1) % 10) + 1

                            const nextScores = [...scores]
                            scores[p] += nextPosition[p]

                            if (nextScores[p] >= 21) {
                                nbWins[p] += gameCount
                                continue
                            }

                            const nextState = [nextPosition, nextScores].join(";")
                            newGameCounts[nextState] = (newGameCounts[nextState] ?? 0) + gameCount
                        }
                    }
                }
            }
            gameCounts = newGameCounts
        }
    }
    

    return Math.max(...nbWins)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}