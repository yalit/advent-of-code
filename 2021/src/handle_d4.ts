import { _ } from 'lodash'
import internal = require('stream');

function handleInput_1(lines: Array<string>, first: boolean = true){
    const bingoNumbers: Array<string> = lines[0].split(',')

    let boards: Array<Board> = []
    _.range(2, lines.length, 6).forEach(n => {
        boards.push(getBoard(lines.slice(n, n+5)))
    });

    let numbers: BoardNumbers  = {}

    boards.forEach((board, n) => {
        const boardNumbersData: BoardNumbers = getBoardNumbersData(board, n)
        Object.keys(boardNumbersData).forEach(number => {
            if (!Object.keys(numbers).includes(number)) numbers[number] = []
            numbers[number].push(boardNumbersData[number])
        })
    });

    let winningBoard: Board;
    let winningNumber: string;
    let nbWinningBoard: number = 0;
    let winningBoardPositions: Array<number> = [];

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
            }
        })
    })

    return getBoardValue(winningBoard) * Number(winningNumber)
}

function isBoardWinning(board: Board): boolean {
    let lineN: number = 0
    while (lineN < board.lines.length){
        if (sumLine(board.lines[lineN]) === -1 * board.lines[lineN].length ){
            return true
        }
        lineN++
    }

    let columnN: number = 0
    while (columnN < board.columns.length){
        if (sumLine(board.columns[columnN]) === -1 * board.columns[columnN].length ){
            return true
        }
        columnN++
    }

    return false
}

function getBoardValue(board: Board){
    return board.lines.reduce((acc, line) => acc + line.reduce((accLine, elem) => (elem >=0) ? accLine + elem : accLine ,0), 0)
}

function sumLine(line: Array<number>){
    return line.reduce((accline, elem) => accline + elem,0)
}

interface Board {
    lines: Array<Array<number>>,
    columns: Array<Array<number>>
}

function getBoard(boardlines: Array<string>): Board{
    const lines = boardlines.map(line => _.range(0,line.length, 3).map(n => Number(line.slice(n, n+2))))

    let board: Board = {
        lines,
        columns: _.range(0,lines[0].length).map(n => lines.map(line => line[n]))
    }

    return board
}

interface BoardNumber {
    boardNumber: number,
    lineNb: number,
    columnNb: number
}

interface BoardNumbers {
    [key: number]: BoardNumber
}

function getBoardNumbersData(board: Board, boardNumber: number): BoardNumbers {
    let numbers: BoardNumbers = {}
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


export function handleInput(lines: Array<string>) {
    return [handleInput_1(lines), handleInput_1(lines, false)]
}