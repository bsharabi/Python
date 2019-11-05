def print1(mat):
    for i in range(3):
        print(mat[i])
def if_check(mat):
    eq=[0,0,0,0,0,0,0,0]
    for i in range(3):
        for j in range(3):
            if i==j:
                if mat[i][j]== mat[0][0]:
                    eq[0]=eq[0]+1
            elif i+j==2:
                if mat[i][j]== mat[0][2]:
                    eq[1]=eq[1]+1
            elif i==0:
                if mat[i][j]== mat[0][0]:
                    eq[2]=eq[2]+1
            elif i==1:
                if mat[i][j]== mat[1][0]:
                    eq[3]=eq[3]+1
            elif i==2:
                if mat[i][j]== mat[2][0]:
                    eq[4]=eq[4]+1
            elif j==0:
                if mat[i][j]== mat[0][0]:
                    eq[5]=eq[5]+1
            elif j==1:
                if mat[i][j]== mat[0][1]:
                    eq[6]=eq[6]+1
            elif j==2:
                if mat[i][j]== mat[0][2]:
                    eq[7]=eq[7]+1
    cnt=0
    print(eq)
    for l in range(3):
        for j in range(3):
            print(mat[l][j])
            if mat[l][j]=='x' or mat[l][j]=='o':
                cnt+=1
    if cnt==9:
        return 0
    for x in range(len(eq)):
        if eq[x]==3:
            return 1
    print(eq)
    return 2
def main():
    mat =[["x","x","x"],
          ["o","o","o"],
          ["x","x","o"]]
    win=[0,0]
    while(1):
        cheek=if_check(mat)
        print(cheek)
        if cheek==1:
            print("winer")
            break
        elif cheek==0:
            print("shave")
            break
        elif cheek==2:
            continue
        

main()