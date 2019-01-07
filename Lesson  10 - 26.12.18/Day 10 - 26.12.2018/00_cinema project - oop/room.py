class Room:
    def __init__(self, movie):
        self.matrix_seat = [[False for j in range(8)] for i in range(10)] 
        self.movie=movie


    def order_seats(self,amount):
        for row in range(0,len(self.matrix_seat)):
            for col in range(0,len(self.matrix_seat[row])):
                if not self.matrix_seat[row][col]:
                    self.matrix_seat[row][col]=True
                    amount-=1
                    if amount==0: 
                        return True
            
        return False


    def get_info(self):
        seat_status="\n"
        for row in range(0,len(self.matrix_seat)):
            for col in range(0,len(self.matrix_seat[row])):
                if self.matrix_seat[row][col]:
                    seat_status+=" V |"
                else:
                    seat_status+=" X |"
            seat_status+="\n----------------------------------\n"
        return self.movie.get_info() + seat_status
