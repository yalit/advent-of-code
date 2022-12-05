import { off } from "process"

function handleInput_1(lines: Array<string>){
    const departTime: number = parseInt(lines[0])
    const busses: Array<number> = lines[1].split(',').filter(e => e !== 'x').map(n => parseInt(n))

    type BusData = {id: number, wait: number}
    const nearestBus = busses.reduce((nearest: BusData, b: number) => {
        const wait = (Math.ceil(departTime/b) * b) - departTime
        if (nearest === undefined || wait < nearest.wait) {
            return {id: b, wait}
        }
        return nearest

    }, undefined)
    
    return nearestBus.id * nearestBus.wait
}

function handleInput_2(lines: Array<string>){
    const data: Array<string> = lines[1].split(',')
    const active = data.filter(n => n !== 'x')
    let busses = {}
    active.forEach(a => busses[a] = data.indexOf(a) % parseInt(a))

    let t = parseInt(active[0])
    let delta = t

    Object.keys(busses).sort((a,b) => parseInt(b) - parseInt(a)).forEach((bus) => {
        let offset = busses[bus]
        if (bus === active[0]) {
            console.log(`Bus ${bus} schedule is baseline, time interval ${delta}`)
            return
        }
        const busNumber = parseInt(bus)
        while (1) {
            if ((t+offset) % busNumber === 0) {
                delta *= busNumber
                console.log(`Bus ${bus} schedule found at time ${t}, new interval ${delta}`)
                break
            }
            t += delta
        }
    })

    return t
}


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_2(lines)]
}