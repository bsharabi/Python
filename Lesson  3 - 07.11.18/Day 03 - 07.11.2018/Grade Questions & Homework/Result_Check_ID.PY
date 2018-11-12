def checkID(IDnum):
    sum1=0
    for x in range(0,9):
        i=1
        if(x%2!=0):
            i=2
        if(int(IDnum[x])*i>9):
            sum1+=((int(IDnum[x])*i)%10)+((int(IDnum[x])*i)//10)
        else:
            sum1+=int(IDnum[x])*i
    return sum1
    
def main():
    while 1:
        IDnum=input("Please enter your ID card for review\n")
        if(len(IDnum)<=9 and len(IDnum)>0 and IDnum.isdigit()== True):
            IDnum=IDnum.zfill(9)
            break
        print("ID is invalid, ID is longer than 9 digits or contains characters or less than 0 characters long\n")
    check=checkID(IDnum)
    if(check%10==0):
        print("The ID number is valid\n")
    else:
        print("Invalid ID number\n")

main()
