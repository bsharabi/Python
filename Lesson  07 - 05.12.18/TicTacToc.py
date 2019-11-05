"""
-------------------------Global Props--------------------
"""
rank=None
is_win=None
is_x_turn=None
matrix=None
x_array=None
o_array=None
"""
-------------------------Function--------------------
"""
def get_board_rank():
    global rank
    rank=int(input("Enter the rank of the board"))
def get_build_matrix():
    global matrix,rank
    matrix=[]
    for row in range(rank):
        matrix.append([])
        for col in range(rank):
            matrix[row].append(row*rank+col+1)
        print(matrix[row])
        print("")


get_board_rank()
get_build_matrix()

"""
-------------------------Main code--------------------
"""