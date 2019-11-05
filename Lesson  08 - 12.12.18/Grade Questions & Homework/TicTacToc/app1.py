import os
import random
"""
---------------GLOBAL PROPS------------------
"""
rank= None#Size of the game
is_win= False
is_x_turn= False
play_again = "y"
matrix= None
x_array= None
o_array= None
computer=None
choice=None

"""
---------------FUNCTIONS----------------------
"""
def get_board_rank():# input of size the game
    global rank
    rank=int(input("Enter the rank of the board: "))

def build_matrix():#create of the array
    global matrix
    global x_array
    global o_array

    x_array=[]
    o_array=[]
    matrix=[]
    for row in range(0,rank):
        matrix.append([])
        for col in range(0,rank):
            matrix[row].append(row*rank+col+1)

    for element in range(0,rank*2+2):
        x_array.append(0)
        o_array.append(0)

def Player_selection():
    global is_x_turn
    global choice
    turn=None
    global computer
    while 1:
        if(choice!='x' and choice!='o'and choice!='X'and choice!='O'):
            choice = input("Please select the player you want to play with (|X| or |O|)")
            continue
        if turn != 'y' and turn != 'Y' and turn != 'N' and turn != 'n' :
            turn = input("Do you want to start a game ?(|Y| or |N|)")
            continue
        else:
            break
    if (((choice=='x'or choice=='X') and (turn == 'y' or turn == 'Y')) or ((choice=='o'or choice=='O') and (turn == 'n' or turn == 'N'))):
        is_x_turn=True
    else:
        is_x_turn= False
    if turn == 'n' or turn == 'N':
        computer= True
    else:
        computer= False


def computer_position():
    global rank
    global x_array
    global o_array
    global choice
    global matrix  
    """
    for i in range(rank):
        for j in range(rank):
            if matrix[i][j] != "x" and matrix[i][j] !="o":
                row=(matrix[i][j]-1)//rank
                col= (matrix[i][j]-1) %rank
                """
               
    if choice =="o" or choice =="O":
        for x in range(rank*2+2):     
            if x_array[x]==rank-1:       
                if x <rank:
                    for j in range(rank):
                        if matrix[x][j] != "x" and matrix[x+1][j] !="o":
                            row=(matrix[x][j]-1)//rank
                            col= (matrix[x][j]-1) %rank
                            return matrix[row][col]
                elif x>=rank and x < rank*2:
                    for i in range(rank):
                        if matrix[i][x-rank] != "x" and matrix[x+1][j] !="o":
                            row=(matrix[i][x-rank]-1)//rank
                            col= (matrix[i][x-rank]-1) %rank
                            return matrix[row][col]
                else:
                    for i in range(rank):
                        for j in range(rank):
                            if i==j :
                                if matrix[i][j] != "x" and matrix[i][j] !="o":
                                    row=(matrix[i][j]-1)//rank
                                    col= (matrix[i][j]-1) %rank
                                    return matrix[row][col]
        for x in range(rank*2+2):     
            if o_array[x]==rank-1:       
                if x <rank:
                    for j in range(rank):
                        if matrix[x][j] != "x" and matrix[x][j] !="o":
                            row=(matrix[x][j]-1)//rank
                            col= (matrix[x][j]-1) %rank
                            return matrix[row][col]
                elif x>=rank and x < rank*2:
                    for i in range(rank):
                        if matrix[i][x-rank] != "x" and matrix[x][x-rank] !="o":
                            row=(matrix[i][x-rank]-1)//rank
                            col= (matrix[i][x-rank]-1) %rank
                            return matrix[row][col]
                else:
                    for i in range(rank):
                        for j in range(rank):
                            if i==j :
                                if matrix[i][j] != "x" and matrix[i][j] !="o":
                                    row=(matrix[i][j]-1)//rank
                                    col= (matrix[i][j]-1) %rank
                                    return matrix[row][col]

        return random.randint(0,rank*rank)
    else:
        for x in range(rank*2+2):    
            if o_array[x]==rank-1:       
                if x <rank:
                    for j in range(rank):
                        if matrix[x][j] != "x" and matrix[x][j] !="o":
                            row=(matrix[x][j]-1)//rank
                            col= (matrix[x][j]-1) %rank
                            return matrix[row][col]
                elif x>=rank and x < rank*2:
                    for i in range(rank):
                        if matrix[i][x-rank] != "x" and matrix[i][x-rank] !="o":
                            row=(matrix[i][x-rank]-1)//rank
                            col= (matrix[i][x-rank]-1) %rank
                            return matrix[row][col]
                else:
                    for i in range(rank):
                        for j in range(rank):
                            if i==j :
                                if matrix[i][j] != "x" and matrix[i][j] !="o":
                                    row=(matrix[i][j]-1)//rank
                                    col= (matrix[i][j]-1) %rank
                                    return matrix[row][col]
        for x in range(rank*2+2):     
            if x_array[x]==rank-1:       
                if x <rank:
                    for j in range(rank):
                        if matrix[x][j] != "x" and matrix[x][j] !="o":
                            row=(matrix[x][j]-1)//rank
                            col= (matrix[x][j]-1) %rank
                            return matrix[row][col]
                elif x>=rank and x < rank*2:
                    for i in range(rank):
                        if matrix[i][x-rank] != "x" and matrix[i][x-rank] !="o":
                            row=(matrix[i][x-rank]-1)//rank
                            col= (matrix[i][x-rank]-1) %rank
                            return matrix[row][col]
                else:
                    for i in range(rank):
                        for j in range(rank):
                            if i==j :
                                if matrix[i][j] != "x" and matrix[i][j] !="o":
                                    row=(matrix[i][j]-1)//rank
                                    col= (matrix[i][j]-1) %rank
                                    return matrix[row][col]
        return random.randint(0,rank*rank)
    
      

    return random.randint(0,rank*rank)

def get_position():
    global rank
    global matrix
    global is_x_turn
    global computer
    #os.system('cls')
    for row in range(0,rank):  
        strFormat=""  
        for col in range(0,rank):
            strFormat+=str(matrix[row][col]) + " | "
        print(strFormat)
        print("-----"*rank)
    if is_x_turn:
        char="x"
    else:
        char="o"
    if(computer):
        print("************ Computer ",char,"****************")
        return computer_position()
    else:
         print("************ user ",char,"****************")
         return int(input("Enter the position (1 - "+ str(rank*rank)+")"))

def check_if_win(row,col):
    global is_x_turn
    global is_win
    global rank
    global x_array
    global o_array
    if is_x_turn:
        arr=x_array
    else:
        arr=o_array

    arr[row]+=1
    arr[rank+col]+=1

    if row==col:
        arr[rank+rank]+=1

    if (row+col)==(rank-1):
        arr[rank+rank+1]+=1

    is_win=(arr[row]==rank) or (arr[rank+col]==rank) or (arr[rank+rank+1]==rank) or (arr[rank+rank]==rank)

    if(is_win):
        if(is_x_turn):
            print("x won")
        else:
            print("o won")
    else:
        sum=0
        for element in range(0,rank):
            sum+=x_array[element]
            sum+=o_array[element]
        if(sum==rank*rank):
            is_win=True
            print("Game Over")

def handle_turn(position):
    global matrix
    global is_x_turn         
    global computer
    row=(position-1)//rank
    col= (position-1) %rank

    if matrix[row][col]!="x" and matrix[row][col]!="o":
        if is_x_turn:
            matrix[row][col]="x"
        else:
            matrix[row][col]="o"
        
        check_if_win(row,col)

        # change the turn to the other player
        # if is_x_turn was true - it will get false
        # if is_x_turn was false - it will get true
        is_x_turn=not is_x_turn
        computer=not computer
        return True
    else:
        return False

"""
---------------MAIN CODE-----------------------
"""
while play_again=="y":
    get_board_rank()
    build_matrix()
    Player_selection()
    while not is_win:
        flag=False
        while not flag:
            selectedPos=get_position()
            #os.system('cls')
            flag=handle_turn(selectedPos)
    is_win=False
    play_again=input("Do you want to play again (y or n)")

