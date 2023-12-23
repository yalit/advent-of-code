import {arraySum} from "../../2020/src/libraries/array";

class Dice {
    currentPosition: number = 0
    diceValues: Array<number> = []
    maxDiceValue: number = 100

    constructor() {
        for(let a = 1; a <=this.maxDiceValue; a++) {
            this.diceValues.push(a)
        }
    }

    roll(): number {
        let rolledValues: Array<number> = this.diceValues.slice(this.currentPosition, this.currentPosition+3)
        
        if (this.currentPosition > 97) {
            rolledValues = rolledValues.concat(this.diceValues.slice(0,3-(100-this.currentPosition)))
        }

        this.currentPosition = (this.currentPosition + 3) % 100
        return rolledValues.reduce((s, e) => s+e, 0)
    }
}

class Player {
    position: number
    score: number = 0

    constructor(position: number) {
        this.position = position - 1 // to match the position in an array
    }

    advance(steps: number) {
        this.position = (this.position + steps) % 10
        this.score += this.position + 1
    }
}

class Game {
    players: Array<Player>
    dice: Dice = new Dice()
    currentTurn = 0
    maxScore: number = 1000

    constructor(posA: number, posB: number) {
        this.players = [new Player(posA), new Player(posB)]
    }

    isFinished(): boolean {
        return this.players[0].score >= this.maxScore || this.players[1].score >= this.maxScore
    }

    play(): void {
        this.players[this.currentTurn % 2].advance(this.dice.roll())
        this.currentTurn++
    }

    loser(): Player {
        return (this.players[0].score > this.players[1].score) ? this.players[1] : this.players[0]
    }

    loserScore(): number {
        return this.loser().score * this.currentTurn * 3
    }
}

class DiracGame {
    maxScore = 21
    playerPosition: Array<number>
    rolls: number[] = [] //Dirac Dice possible rolls sum
    playerWins: Array<number> = [0,0]

    cache = {}

    constructor(a: number, b: number) {
        this.playerPosition = [a,b]

        let possibleRolls: Array<number> = [1,2,3]
        possibleRolls.forEach(a => {
            possibleRolls.forEach(b => {
                possibleRolls.forEach(c => {
                    this.rolls.push(a+b+c)
                });
            });
        });
    }

    play() {
        this.playerWins = this.play2(this.playerPosition[0], this.playerPosition[1])
    }

    play2(cpPos: number, opPos: number, cpScore: number = 0, opScore: number = 0) {
        if (cpScore >= this.maxScore) {
            return [1,0]
        } else if (opScore >= this.maxScore) {
            return [0,1]
        }

        let my_wins = 0 
        let other_wins = 0

        let state = ''
        this.rolls.forEach(r => {
            let newPosition = (cpPos + r) % 10
            let newScore = cpScore + newPosition + 1

            state = `${cpPos}-${opPos}-${newPosition}-${newScore}-${opScore}`

            let [other_next_wins, my_next_wins] = [0,0]
            if (state in this.cache) {
                [other_next_wins, my_next_wins] =  this.cache[state]
            } else {
                [other_next_wins, my_next_wins] = this.play2(opPos, newPosition, opScore, newScore)
                this.cache[state] = [other_next_wins, my_next_wins]
            }
            my_wins += my_next_wins
            other_wins += other_next_wins
        });

        return [my_wins, other_wins]
    }

    mostWins() : number {
        return (this.playerWins[0] > this.playerWins[1]) ? this.playerWins[0] : this.playerWins[1]
    }
}

const getPositions = (lines: Array<string>): [number, number] => {
    return [Number(lines[0].split(' ').reduce((_,c) => c,'')), Number(lines[1].split(' ').reduce((_,c) => c,''))]
}


function handleInput_1(lines: Array<string>){
    let [a, b] = getPositions(lines)
    let game = new Game(a, b)
    
    while (!game.isFinished()) {
        game.play()
    }

    return game.loserScore()
}

function handleInput_2(lines: Array<string>){
    let [a, b] = getPositions(lines)
    let game = new DiracGame(a, b)
    
    game.play()
    
    return game.mostWins()
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}