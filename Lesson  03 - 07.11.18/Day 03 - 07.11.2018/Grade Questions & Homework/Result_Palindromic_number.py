#Method 2 - Long way
def Palindromic_number(num):
    temp=num
    cnt=0
    while temp !=0 :
        temp//=10
        cnt+=1
    temp=1
    while cnt-1!=0:
        temp*=10
        cnt-=1
    num2=0   
    while num!=0:
        num2+=(temp)*(num%10)
        num//=10
        temp//=10
    return num2
def main():
    num = int(input("Enter the number you want to check\n "))
    num2=Palindromic_number(num)
    if(num==num2):
        print("The number",num,"is a Palindromic\n")
    else:
        print("The number ", num , " is'nt a Palindromic\n")
main()

#Method 1 - short way
'''
def main():
    num = input("Enter the number you want to check\n ")
    if(int(num)==int(num[::-1])):
        print("The number is a Palindromic\n")
    else:
        print("The number is'nt a Palindromic\n")
main()
'''