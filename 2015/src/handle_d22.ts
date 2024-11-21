interface Effect {
    name: string
    timer: number
    effect: string
}

interface Spell {
    name: string
    cost: number
    action: string
}

type State = {
    currentPlayer: 'player' | 'boss'
    boss: {
        hp: number
        dmg: number
    }
    player: {
        hp: number
        mana: number
        armor: number
    }
    manaSpent: number
    effects: Array<Effect>
}

const actions = {
    magicMissile: (state: State) => state.boss.hp -= 4,
    drain: (state: State) => {state.boss.hp -= 2; state.player.hp += 2},
    shield: (state: State) => state.effects.push({name: 'Shield', timer: 6, effect: 'shield'}),
    poison: (state: State) => state.effects.push({name: 'Poison', timer: 6, effect: 'poison'}),
    recharge: (state: State) => state.effects.push({name: 'Recharge', timer: 5, effect: 'recharge'})
}

const effects = {
    shield: (state: State) => state.player.armor = 7,
    poison: (state: State) => state.boss.hp -= 3,
    recharge: (state: State) => state.player.mana += 101
}

const magicMissile: Spell = { name: 'Magic Missile', cost: 53, action: 'magicMissile'}
const drain: Spell = { name: 'Drain', cost: 73, action: 'drain'}
const shield: Spell = { name: 'Shield', cost: 113, action: 'shield'}
const poison: Spell = { name: 'Poison', cost: 173, action: 'poison'}
const recharge: Spell = { name: 'Recharge', cost: 229, action: 'recharge'}

const spells = [magicMissile, drain, shield, poison, recharge]

const canCast = (spell: Spell, state: State) => {
    return state.player.mana > spell.cost && state.effects.filter(e => e.name === spell.name).length === 0
}

const bossTurn = (state: State) => {
    applyEffects(state)
    state.player.hp -= Math.max(1, state.boss.dmg - state.player.armor)
    state.currentPlayer = 'player'
}

const playerTurn = (state: State, spell: Spell) => {
    applyEffects(state)
    state.player.mana -= spell.cost
    state.manaSpent += spell.cost
    actions[spell.action](state)
    state.currentPlayer = 'boss'
}

const isDead = (state: State) => state.player.hp <= 0
const isWin = (state: State) => state.boss.hp <= 0

const applyEffects = (state: State) => {
    state.effects.forEach(e => {effects[e.effect](state); e.timer--})
    state.effects = state.effects.filter(e => e.timer > 0)
}

const deepCopy = (state: State): State => {
    let newState = JSON.parse(JSON.stringify(state))
    newState.player.armor = 0
    return newState
}

let memoization: Map<string, number> = new Map()

const dfs = (state: State): number => {
    if (isWin(state)) return state.manaSpent
    if (isDead(state)) return Infinity

    let key = JSON.stringify(state)
    if (memoization.has(key)) return memoization.get(key)

    let minCost = Infinity

    if (state.currentPlayer === 'player') {
        for (let spell of spells) {
            if (canCast(spell, state)) {
                let newState = deepCopy(state)
                playerTurn(newState, spell)
                minCost = Math.min(minCost, dfs(newState))
            }
        }
    } else {
        let newState = deepCopy(state)
        bossTurn(newState)
        minCost = Math.min(minCost, dfs(newState))
    }

    memoization.set(key, minCost)

    return minCost
}

function handleInput_1(lines: Array<string>){
    let player = {hp: parseInt(lines[0].split(' ')[2]), mana: parseInt(lines[1].split(' ')[1]), armor: 0}
    let boss = {hp: parseInt(lines[3].split(' ')[2]), dmg: parseInt(lines[4].split(' ')[1])}

    return dfs({currentPlayer: 'player', player, boss, manaSpent: 0, effects: []})
}

function handleInput_2(lines: Array<string>){
    return 0
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}