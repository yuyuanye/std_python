import random
'''
words = ('python','jumble','easy','c++','java','ruby','fortran','lisp','go')
word = random.choice(words)
print(word)
jumble = ''
while word:
    postion = random.randrange(len(word))
    jumble += word[postion]
    word = word[:postion] + word[postion+1:]
print('disorder word: ' + jumble)
'''
'''
print(random.random())
print(random.uniform(10,20))
print(random.uniform(20,10))
'''
import random as rd
'''
print(rd.randint(12,20))
print(rd.randint(20,20))
#print(rd.randint(20,10))
print(rd.randrange(10,200,2))
'''
'''
print(rd.choice('studypython'),end='\n======\n')
print(rd.choice(['python','jumble','easy','c++']),end='\n======\n')
print(rd.choice(('java','ruby','fortran','lisp')),end='\n======\n')
'''
'''
words = ['python','jumble','easy','c++','java','ruby','fortran','lisp','go']
rd.shuffle(words)
print(words)

list = [1,2,3,4,5,6,7,8,9]
slice = rd.sample(list,5)
print(slice, end='\n======\n')
print(list,end='\n======\n')

egchar = 'sdfsdeewrvc998756&*^$%'
#print(rd.choice(egchar))
#print(rd.sample(egchar,3))
print(''.join(rd.sample(egchar,3)))
#print(''.join(rd.sample(egchar,3)).replace(' ',''))

for i in range(5):
    print(i,end=' ')
    print(rd.choice(['apple','pear','orange','peach','lemon']))
print('finish')

items = [1,2,3,4,5]
rd.shuffle(items)
print(items)

for i in range(10):
    print(rd.randrange(0,101,2))
print('finish')


for i in range(5):
    print(rd.uniform(0,100))
print('finish')
'''
'''
words = ['python','jumble','easy','c++','java','ruby','fortran','lisp','go']
print(
    '欢迎参加猜单词游戏'
    '把字母组合成一个正确的单词'
)
iscontinue = 'y'
while True:
    while iscontinue == 'y' or iscontinue == 'Y':
        word = rd.choice(words)
        correct = word
        jumble = ''
        while word:
            postion = random.randrange(len(word))
            jumble += word[postion]
            word = word[:postion] + word[postion + 1:]
        print('乱序后的单词',jumble)
        iscontinue =''
    guess = input('\n请你猜单词：\n')
    while guess != correct and guess != '':
        print('对不起，不正确')
        guess = input('继续猜：')
    if guess == correct:
        print('真棒，你猜对了')
    iscontinue = input('\n是否继续猜(y/n):')
    if iscontinue == 'n' or iscontinue == 'N':
        print('游戏结束')
        break
'''
'''
words = ['python','jumble','easy','c++','java','ruby','fortran','lisp','go']
key = words[:]
print(words)
print('key=',key)
'''
X = 'X'
O = '%'
EMPTY = ''
def ask_yes_no(question):
    response = None
    while response not in ('y','n'):
        response = input(question).lower()
    return response

def pieces():
    go_first = ask_yes_no('玩家你是否先走（y/n）:')
    if go_first == 'y':
        print('\n玩家你先走')
        human = X
        computer = O
    else:
        print('\n电脑先走')
        human = X
        computer = O
    return computer, human

def new_board():
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board

def display_board(board):
    board2 = board[:]
    for i in range(len(board)):
        if board[i] == EMPTY:
            board2[i] = i
    print('\t',board2[0],'|',board2[1],'|',board2[2])
    print('\t','-'*20)
    print('\t', board2[3], '|', board2[4], '|', board2[5])
    print('\t', '-' * 20)
    print('\t', board2[6], '|', board2[7], '|', board2[8])

def legal_moves(board):
    moves = []
    for square in range(9):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('你走哪个位置？（0-8）',0, 9)
        if move not in legal:
            print('\n此位置已经落过子了')
    return move

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return  response

def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print('计算机下棋位置。。。',move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print('计算机下棋位置。。。...',move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print('计算器下棋位置，，，',move)
            return move
def winner(board):
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] and board[row[0]] != EMPTY:
            player = board[row[0]]
            return player
    if EMPTY not in board:
        return 'TIE'
    return False
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def main():
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
        if the_winner == computer:
            print('计算机赢')
        elif the_winner == human:
            print('玩家赢')
        elif the_winner == 'TIE':
            print('平局')
        else:
            print('继续')
if __name__ == '__main__':
    main()


