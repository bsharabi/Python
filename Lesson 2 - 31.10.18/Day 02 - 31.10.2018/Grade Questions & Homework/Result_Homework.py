num = int(input("Enter your number\n"))
mispar=["Zero","One","Two","Three","four","five","six","seven","eight","Nine"]
if num >=0 and num<10 :
    print(mispar[num])
elif num>=10 and num <100:
    digit=(num%10)+(num//10)
    print(num,"is 2 digit number, sum is",digit)
elif num>=100 and num <1000:
    digit=(num//100)*(num%100//10)*(num%10)
    print(num,"is 3 digit number, sum is",digit)
elif num < 0 or num >1000 :
    print("Invalid number, you need a number with one digit up to three digits")

