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
def Select_location(table,size): 
    win=['X = ',0,'O = ',0] 
    while(1):
        i=0
        check=table
        cnt=0
        while(i<size*size):
            if i%2==0:
                user1=int(input('Player with X enter yore number: \n'))
                if(user1<1 or user1>size*size):
                    print("Type the size of the game 1 bettwen"+ size*size)
                    continue
                elif user1:
                    for x in table:
                        for i in range(size):
                            if user1 != x[i]:
                                cnt+=1
                    if cnt==size*size:             
                        print("Busy location Try another place")
                        continue
                i+=1
                cnt=0
            else:
                user1=int(input('Player with O enter yore number: \n'))
                if(user1<1 or user1>size*size):
                    print("Type the size of the game 1 bettwen"+ size*size)
                    continue
                elif user1:
                    for x in table:
                        for i in range(size):
                            if user1 != x[i]:
                                cnt+=1
                    if cnt==size*size:             
                        print("Busy location Try another place")
                        continue
                i+=1
                cnt=0
def main():
    while(1):
        size= int(input("Type the size of the game 3 bettwen 5"))
        if(size>=3 and size <=5):
            break
    table=create_size_game(size)
    Select_location(table,size)

    print_game(table,size)
main()