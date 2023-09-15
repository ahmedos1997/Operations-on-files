# تمرين لعبة تيك تاك

theboard = { '7': ' ', '8': ' ', '9':' ',
             '4': ' ', '5': ' ', '6':' ',
             '1': ' ', '2': ' ', '3': ' '}

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')

def game():
    turn = 'x'
    count = 0

    for i in range(10):

        printboard(theboard)
        print(' its your turn ' + turn + ' move to wiche place? ')

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print('this place is full. \n move to which place? ')
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ': # الصف العلوي
                printboard(theboard)
                print('\n the game is over.\n')
                print('****' + turn + 'you win.****')
                break

            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ': # الصف في الوسط
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ': # الصف الاسفل
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': # العمود على اليسار
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': # العمود في الوسط
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': # العمود على اليمبن
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': # خط المائل الاول
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + 'you win.****')
                    break

            elif theboard['9'] == theboard['5'] == theboard['1'] != ' ': # الخط المائل الثاني
                    printboard(theboard)
                    print('\n the game is over.\n')
                    print('****' + turn + ' you win.****')
                    break

        if count == 9:
                print('\n GAMED OVER\n')
                print('its tai!')
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

if __name__ == "__main__":
    game()