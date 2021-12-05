import _ from 'lodash'

function handleInput_1(lines, first = true){
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

    let winningBoard;
    let winningNumber;
    let nbWinningBoard = 0;
    let winningBoardPositions = [];

    bingoNumbers.forEach(number => {
        if (first && winningBoard !== undefined) return
        if (!Object.keys(numbers).includes(number)) return 
        if (nbWinningBoard === boards.length) return

        numbers[number].forEach(boardPosition => {
            if (first && winningBoard !== undefined) return
            if (nbWinningBoard === boards.length) return

            boards[boardPosition.boardNumber]['lines'][boardPosition.lineNb][boardPosition.columnNb] = -1
            boards[boardPosition.boardNumber]['columns'][boardPosition.columnNb][boardPosition.lineNb] = -1

            if ((!first || winningBoard === undefined) && !winningBoardPositions.includes(boardPosition.boardNumber) && isBoardWinning(boards[boardPosition.boardNumber])){
                winningBoard = boards[boardPosition.boardNumber]
                winningNumber = number;
                winningBoardPositions.push(boardPosition.boardNumber)
                nbWinningBoard++;
                //console.log(winningNumber, boardPosition.boardNumber, nbWinningBoard, winningBoard)
            }
        })
    })

    return getBoardValue(winningBoard) * winningNumber
}

function isBoardWinning(board){
    let lineN = 0
    while (lineN < board.lines.length){
        if (sumLine(board.lines[lineN]) === -1 * board.lines[lineN].length ){
            return true
        }
        lineN++
    }

    let columnN = 0
    while (columnN < board.columns.length){
        if (sumLine(board.columns[columnN]) === -1 * board.columns[columnN].length ){
            return true
        }
        columnN++
    }

    return false
}

function getBoardValue(board){
    return board.lines.reduce((acc, line) => acc + line.reduce((accLine, elem) => (elem >=0) ? accLine + elem : accLine ,0), 0)
}

function sumLine(line){
    return line.reduce((accline, elem) => accline + elem,0)
}

function getBoard(boardlines){
    const lines = boardlines.map(line => _.range(0,line.length, 3).map(n => parseInt(line.slice(n, n+2))))
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


export function handleInput(lines) {
    return [handleInput_1(lines), handleInput_1(lines, false)]
}