import os
'''Function print'''
def print1(mat):
    print("-------")
    for i in range(3):
        for j in range(3): 
            print("|"+ mat[i][j] ,end="")
        print("|")
        print("-------")
'''A function that checks whether there is a winner or a draw'''       
def if_check(mat):
    if mat[0][0]==mat[0][1] and mat[0][1]==mat[0][2]:
        return mat[0][0]
    if mat[1][0]==mat[1][1] and mat[1][1]==mat[1][2]:
        return mat[1][0]
    if mat[2][0]==mat[2][1] and mat[2][1]==mat[2][2]:
        return mat[2][0]
    if mat[0][0]==mat[1][0] and mat[1][0]==mat[2][0]:
        return mat[0][0]
    if mat[0][1]==mat[1][1] and mat[1][1]==mat[2][1]:
        return mat[0][1]
    if mat[0][2]==mat[1][2] and mat[1][2]==mat[2][2]:
        return mat[0][2]
    if mat[0][0]==mat[1][1] and mat[1][1]==mat[2][2]:
        return mat[0][0]
    if mat[0][2]==mat[1][1] and mat[1][1]==mat[2][0]:
        return mat[0][2]
    cnt=0
    for l in range(3):
        for j in range(3):
            if mat[l][j]=='x' or mat[l][j]=='o':
                cnt+=1
    if cnt==9:
        return 0
    else:
        return 1
'''A function that receives values from the user and sends the function to the test of victory'''      
def Game():
    win=["X = ",0,"O = ",0]
    while(1):
        i=0
        mat =[["1","2","3"],
          ["4","5","6"],
          ["7","8","9"]]
        os.system('cls')
        print1(mat)
        while  i < 9:
            if i % 2 == 0:
                var1 = input('Player with x enter yore number: ')
                os.system('cls')
                if ord(var1) > 48 and ord(var1) < 58:
                    for g in range(3):
                        for h  in range(3):
                            if mat[g][h] == var1:
                                mat[g][h] = 'x'
                                print1(mat)
                                over=if_check(mat)
                                if(over=='x' or over=='o' or over == 0):
                                    i=9
                                else:
                                    i+=1
                else:
                    print("worng number!")
                    continue
            else:
                var2= input('Player with o enter yore number:')
                os.system('cls')
                if ord(var2) > 48 and ord(var2) < 58:
                    for g in range(3):
                        for h  in range(3):
                            if mat[g][h] == var2:
                                mat[g][h] = 'o'
                                print1(mat)
                                over=if_check(mat)
                                if(over=='x' or over=='o' or over == 0):
                                    i=9
                                else:
                                    i+=1
                else:
                    print('worng number!')
                    continue
        if over=='x':
            win[1]+=1
            print("x = winer")
        elif over=='o':
            win[3]+=1
            print("o = winer")
        elif over==0:
            print("shave")
        print("Scoreboard ")
        str1=" ".join(str(x) for x in win)
        print(str1)
        andr=int(input("Another round Press 1 otherwise press each character"))
        if(andr==1):
            continue
        else:
            print("Good bay!!")
            break  

'''Primary function'''
Game()
    