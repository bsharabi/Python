str1=["abcabcabcabc","abcabc","abababa"]
str2=input("Enter string  ")
max=0
index=None
k=0
cnt=0
for x in range(len(str1)):
	for y in range(len(str1[x])):
		if str1[x][y]!=str2[k]:
			k=0
		else:
			k+=1
		if(k==len(str2)):
			cnt+=1
			k=0	
	if(max<cnt):
		max=cnt
		index=x
		cnt2=cnt
	k=0
	cnt=0

print(index)
print(cnt2)
print(str1[index])
