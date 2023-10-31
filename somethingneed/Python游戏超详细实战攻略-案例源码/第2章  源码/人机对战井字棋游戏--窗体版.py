# Tic-Tac-Toe井字棋游戏
from tkinter import *
from tkinter.messagebox import *
#全局常量
X = "X"
O = "O"
EMPTY = " "
computer = X
human = O
#询问玩家你是否先走
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):			#如果输入不是"y", "n"，继续重新输入
        response = input(question).lower()
    return response
#询问谁先走，先走方为X，后走方为O
#函数返回电脑方、玩家的角色代号
def pieces():
    global computer, human
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

#产生保存走棋信息列表board
def new_board():
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board

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

#绘制整个游戏区域图形就是按照地图board储存图形代号，从imgs列表获取对应图像，显示到Canvas上。    
def drawGameImage(board):
    #print(board)
    for square in range(9):        
        if board[square] == X:
            img1= imgs[0]                  #从imgs列表获取对应图像X
            i=square%3
            j=square//3
            cv.create_image((i*40+20,j*40+20),image=img1) #显示到Canvas上
            cv.pack()
        elif board[square] == O:
            img1= imgs[1]                  #从imgs列表获取对应图像O
            i=square%3
            j=square//3
            cv.create_image((i*40+20,j*40+20),image=img1) #显示到Canvas上
            cv.pack()
#用户走棋
#游戏区的单击事件处理用户走棋过程。
#用户走棋时，判断此位置是否已经落过子了，如果是是合法位置才能落子。用户走完后，判断输赢,当返回False继续游戏（即电脑自动完成走棋并显示），如果游戏结束显示输赢结果。
def callback(event):   #走棋picBoard_MouseClick
    global computer, human, board
    print ("clicked at", event.x, event.y)
    x=(event.x)//40  #换算棋盘坐标
    y=(event.y)//40
    print ("clicked at", x, y )
    legal = legal_moves(board)
    move=y*3+x
    print(move,"合法位置",legal)
    if move not in legal:
        print("\n此位置已经落过子了")
        return
    board[move] = human
    if human==O:
        img= imgs[1]                        #从imgs列表获取对应图像O
    else:
        img= imgs[0]                        #从imgs列表获取对应图像X
    cv.create_image((x*40+20,y*40+20),image=img) #显示到Canvas上
    cv.pack()
    if not  winner(board):		#当返回False继续游戏
        #转换角色
        move = computer_move(board, computer, human)
        board[move] = computer
        drawGameImage(board)
    
    the_winner = winner(board)
    #如果游戏结束，输出输赢或和棋信息
    if the_winner == computer:
        print("电脑赢!\n")
        showinfo(title="提示",message="电脑赢了")
    elif the_winner == human:         
        print("玩家赢!\n")
        showinfo(title="提示",message="玩家赢了")
    elif the_winner == "TIE":				#"平局和棋"
        print("平局和棋，游戏结束\n")
        showinfo(title="提示",message="平局和棋，游戏结束")
def DrawQipan():
    cv.create_line(0,40,120,40)
    cv.create_line(0,80,120,80)
    cv.create_line(0,120,120,120)
    cv.create_line(40,0,40,120)
    cv.create_line(80,0,80,120)
    cv.create_line(120,0,120,120)
    cv.pack()
    
#主程序
# start the program
root = Tk()
imgs= [PhotoImage(file='Image\\X.gif'),PhotoImage(file='Image\\O.gif') ]
cv = Canvas(root, bg = 'green', width = 226, height = 226)
cv.pack()
cv.focus_set() #将焦点设置到cv上
computer, human = pieces()
turn = X
DrawQipan()
board = new_board()

if turn == human:
    pass
else:
    move = computer_move(board, computer, human)
    board[move] = computer
#display_board(board)
drawGameImage(board) #显示棋盘
#cv.bind("<Button-1>", lambda x:callback(x,board))
cv.bind("<Button-1>", callback)
root.mainloop()

