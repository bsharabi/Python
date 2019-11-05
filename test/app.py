str1=["abcabcabcabc","abcabc","abababa"]
str2=input("Enter string  ")
max=0
index=None
for x in range(len(str1)):
	if(str1[x].count(str2)>max):
		max=str1[x].count(str2)
		index=x
print(index)
