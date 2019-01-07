arr=[False]*2


print(arr)   # [False, False]

matrix=[arr]*3 
print(matrix) # [[False, False], [False, False], [False, False]]



matrix[0][1]=True
print(matrix) # [[False, True], [False, True], [False, True]]



matrix=[[False]*2]*3 
print(matrix) # [[False, False], [False, False], [False, False]]


matrix[0][1]=True
print(matrix) # [[False, True], [False, True], [False, True]]


matrix=[[False for j in range(2)] for i in range(3)] 
print(matrix) # [[False, False], [False, False], [False, False]]


matrix[0][1]=True
print(matrix) # [[False, True], [False, False], [False, False]]
