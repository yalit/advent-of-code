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
    const reindeers = lines.map(line => {
        return line.match(/[a-zA-Z]+ can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds./).slice(1,4).map(n => +n)
    })
    const distances = reindeers.map(([speed, speedDuration, restDuration]) => {
        return getDistanceForReindeer(2503, {speed, speedDuration, restDuration})
    })

    return Math.max(...distances)
}

function handleInput_2(lines: Array<string>){
    const reindeers = lines.map(line => {
        return line.match(/[a-zA-Z]+ can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds./).slice(1,4).map(n => +n)
    })

    let s = 1
    let reindeersPoints = reindeers.map(_ => 0)
    while(s < 2503){
        const distances = reindeers.map(([speed, speedDuration, restDuration]) => {
            return getDistanceForReindeer(s, {speed, speedDuration, restDuration})
        })
        const max = Math.max(...distances)
        distances.forEach((d, idx) => reindeersPoints[idx] += d === max ? 1 : 0)
        s+=1
    }
    return Math.max(...reindeersPoints)
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}