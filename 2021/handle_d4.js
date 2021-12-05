import _ from 'lodash'

function handleInput_1(lines){
    const bingoNumbers = lines[0].split(',')

    let boards = []
    _.range(2, lines.length, 6).forEach(n => {
        boards.push(getBoard(lines.slice(n, n+5)))
    });

    let numbers = {}
    boards.forEach((board, n) => {
        const boardNumbersData = getBoardNumbersData(board, n)
        Object.keys(boardNumbersData).forEach(number => {
            if (!Object.keys(numbers).includes(number)) numbers[number] = []
            numbers[number].push(boardNumbersData[number])
        })
    });

    bingoNumbers.forEach(n => {
        numbers[n].forEach(boardPosition => {
            boards[boardPosition.boardNumber]['lines'][boardPosition.lineNb] = 0
            boards[boardPosition.boardNumber]['columns'][boardPosition.columnNb] = 0
        })
        if (isBoardWinning(boards[boardPosition.boardNumber])){
            return getBoardValue(boards[boardPosition.boardNumber]);
        }
    })

    return 0
}

function isBoardWinning(board){
    board.lines.forEach(line => {})
}

function getBoardValue(board){
    return board.lines.reduce((acc, line) => acc + sumLine(line), 0)
}

function sumLine(line){
    return line.reduce((accline, elem) => accline + elem,0)
}

function getBoard(boardlines){
    const lines = boardlines.map(line => _.range(0,line.length, 3).map(n => line.slice(n, n+2)))
    let board = {
        lines,
        columns: _.range(0,lines[0].length).map(n => lines.map(line => line[n]))
    }



    return board
}

function getBoardNumbersData(board, boardNumber){
    let numbers = {}
    board.lines.forEach((line, lineNb) => {
        line.forEach((number, columnNb) => {
            numbers[number] = {
                boardNumber,
                lineNb,
                columnNb
            }
        })
    });
    return numbers
}


function handleInput_2(lines){
    
    return 0
}


export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_2(lines)]
}