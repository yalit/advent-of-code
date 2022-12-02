interface SeatData {
    row: Array<string>,
    column: Array<string>
}

const seatDataMap = {'F': '0','B': '1','L': '0','R': '1'}

function getSeatId(data: SeatData): number {
    const row: number = parseInt(data.row.map(n=>seatDataMap[n]).join(''), 2)
    const column: number = parseInt(data.column.map(n=>seatDataMap[n]).join(''), 2)
    return (row * 8) + column
}

function handleInput_1(lines: Array<SeatData>){
    return Math.max(...lines.map(getSeatId))
}

function handleInput_2(lines: Array<SeatData>){
    const seats: Array<number> = lines.map(getSeatId)
    seats.sort((a,b) => a-b)
    
    return seats.reduce((nb, seat, index) => {
        if (nb !==0) {
            return nb
        }
        if (index > 0 && seat - 1 !== seats[index-1]) {
            return seat - 1
        }
        return nb
    }, 0)
}


export function handleInput(lines: Array<string>) {
    const seatData: Array<SeatData> = lines.map(l => {return {row: l.slice(0,7).split(''), column: l.slice(7).split('')}})
    return [handleInput_1(seatData), handleInput_2(seatData)]
}