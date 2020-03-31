theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
             'low-L': '','low-M': '', 'low-R': ''}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        if theBoard['top-L' and 'top-M' and 'top-R'] == 'X':
            print('X Won!')
            break
        elif theBoard['mid-L' and 'mid-M' and 'mid-R'] == 'X':
            print('X Won!')
            break
        elif theBoard['low-L' and 'low-M' and 'low-R'] == 'X':
            print('X Won!')
            break
        elif theBoard['top-L' and 'mid-M' and 'low-R'] == 'X':
            print('X Won!')
            break
        elif theBoard['top-L' and 'mid-M' and 'low-L'] == 'X':
            print('X Won!')
            break
        elif theBoard['top-M' and 'mid-M' and 'low-M'] == 'X':
            print('X Won!')
            break
        elif theBoard['top-L' and 'mid-L' and 'low-L'] == 'X':
            print('X Won!')
            break
        elif theBoard['top-R' and 'mid-R' and 'low-R'] == 'X':
            print('Y Won!')
            break
            if theBoard['top-L' and 'top-M' and 'top-R'] == 'O':
                print('O Won!')
                break
            elif theBoard['mid-L' and 'mid-M' and 'mid-R'] == 'O':
                print('O Won!')
                break
            elif theBoard['low-L' and 'low-M' and 'low-R'] == 'O':
                print('O Won!')
                break
            elif theBoard['top-L' and 'mid-M' and 'low-R'] == 'O':
                print('O Won!')
                break
            elif theBoard['top-L' and 'mid-M' and 'low-L'] == 'O':
                print('O Won!')
                break
            elif theBoard['top-M' and 'mid-M' and 'low-M'] == 'O':
                print('O Won!')
                break
            elif theBoard['top-L' and 'mid-L' and 'low-L'] == 'O':
                print('O Won!')
                break
            elif theBoard['top-R' and 'mid-R' and 'low-R'] == 'O':
                print('O Won!')
                break
        
printBoard(theBoard)

