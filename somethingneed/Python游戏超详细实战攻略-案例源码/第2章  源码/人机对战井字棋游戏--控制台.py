﻿# Tic-Tac-Toe井字棋游戏
#全局常量
X = "X"
O = "O"
EMPTY = " "
#询问是否继续
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):			#如果输入不是"y", "n"，继续重新输入
        response = input(question).lower()
    return response
#输入位置数字
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
#询问谁先走，先走方为X，后走方为O
#函数返回电脑方、玩家的角色代号
def pieces():
    go_first = ask_yes_no("玩家你是否先走 (y/n): ")
    if go_first == "y":
        print("\n玩家你先走.")
        human = X
        computer = O
    else:
        print("\n电脑先走.")
        computer = X
        human = O
    return computer, human

#产生新的保存走棋信息列表board
def new_board():
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board
#显示棋盘
def display_board(board):
    board2=board[:]     #创建副本，修改不影响原来列表board
    for i in range(len(board)):
        if board[i]==EMPTY:
            board2[i]=i
    print("\t", board2[0], "|", board2[1], "|", board2[2])
    print("\t", "---------")
    print("\t", board2[3], "|", board2[4], "|", board2[5])
    print("\t", "---------")
    print("\t", board2[6], "|", board2[7], "|", board2[8])
#产生可以合法走棋位置序列（也就是还未下过子位置）
def legal_moves(board):
    moves = []
    for square in range(9):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
#判断输赢
def winner(board):
    #所有赢的可能情况，例如(0, 1, 2)就是第一行，(0, 4, 8), (2, 4, 6)就是对角线
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6) )  
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner				#返回赢方
    #棋盘没有空位置
    if EMPTY not in board:
        return "TIE"					#"平局和棋，游戏结束"
    return False
#人走棋
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("你走那个位置? (0 - 8):", 0, 9)
        if move not in legal:
            print("\n此位置已经落过子了")
    #print("Fine...")
    return move
#电脑走棋
def computer_move(board, computer, human):
    # make a copy to work with since function will be changing list
    board = board[:]     #创建副本，修改不影响原来列表board
    #按优劣顺序排序的下棋位置
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7) #最佳下棋位置顺序表
    # 如果电脑能赢，就走那个位置
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print("电脑下棋位置..." ,move)
            return move
        # 取消走棋方案
        board[move] = EMPTY    
    # 如果玩家能赢，就堵住那个位置
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print("电脑下棋位置..." ,move)
            return move
        #取消走棋方案
        board[move] = EMPTY
    #不是上面情况则，也就是这一轮时都赢不了则
    #从最佳下棋位置表中挑出第一个合法位置
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print("电脑下棋位置..." ,move)
            return move
#转换角色
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
#主函数
def main():
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):		#当返回False继续，否则结束循环
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)#转换角色
    #游戏结束输出输赢或和棋信息
    the_winner = winner(board)
    if the_winner == computer:
        print("电脑赢!\n")    
    elif the_winner == human:         
        print("玩家赢!\n")
    elif the_winner == "TIE":				#"平局和棋"
        print("平局和棋，游戏结束\n")
#主程序，很简单就是调用main()函数
# start the program
main()
input("按任意键退出游戏.")
