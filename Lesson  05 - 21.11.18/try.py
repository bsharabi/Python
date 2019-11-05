def create_size_game(size):
    table=[]
    table_g=[]
    k=1
    for i in range(size):
        for i in range(size):
            table.append(k)
            k+=1
        table_g.append(table)
        table=[]
    return table_g    
'''Function print'''
def print_game(table,size):
    print("-"*(size)*3)
    for i in range(size):
        for j in range(size):
            if table[i][j]<10:
                print("| "+ str(table[i][j]) ,end="")
            else:
                print("|"+ str(table[i][j]) ,end="")
        print("|")
        print("-"*(size)*3) 
def main():
    while(1):
        size= int(input("Type the size of the game 3 bettwen 9"))
        if(size>=3 and size <=9):
            break
    table=create_size_game(size)
    print_game(table,size)
    user=int(input("enter"))
    print(user)
    for x in table:
        for i in range(size):
            if user == x[i]:
                print("ok")
main()