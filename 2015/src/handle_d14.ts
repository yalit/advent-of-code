type Reindeer = {
    speed: number, 
    speedDuration: number,
    restDuration: number
}

const comet: Reindeer = {speed: 14, speedDuration: 10, restDuration: 127}
const dancer: Reindeer = {speed: 16, speedDuration: 11, restDuration: 162}

function getDistanceForReindeer(sec:number, reindeer : Reindeer): number {

    if (sec <= reindeer.speedDuration) {
        return sec * reindeer.speed
    } 

    if (sec <= reindeer.speedDuration + reindeer.restDuration) {
        return reindeer.speedDuration * reindeer.speed
    }

    const nbIter: number = Math.floor(sec / (reindeer.speedDuration + reindeer.restDuration))
    const remainingSeconds = sec - ((reindeer.speedDuration + reindeer.restDuration) * nbIter)

    return (nbIter * reindeer.speed * reindeer.speedDuration) + ((remainingSeconds <= reindeer.speedDuration) ? remainingSeconds * reindeer.speed : reindeer.speedDuration * reindeer.speed )
}


function handleInput_1(lines: Array<string>){
    return Math.max(getDistanceForReindeer(2503, comet), getDistanceForReindeer(2503, dancer))
}

function handleInput_2(lines: Array<string>){
    let i = 1
    let points = [0,0]
    let dComet: number
    let dDancer: number
    while (i <= 2503) {
        dComet = getDistanceForReindeer(i, comet)
        dDancer = getDistanceForReindeer(i, dancer)

        if (dComet >= dDancer) {
            points[0]++
        }
        if (dDancer >= dComet) {
            points[1]++
        }

        i++
    }

    return Math.max(...points)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}