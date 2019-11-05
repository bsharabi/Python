class Room:

    def __init__(self, movie):
        self.room = [[False for i in range(8)]for i in range(10)]
        self.movie = movie

    def Order_Seats(self, amount):
        for row in range(0, len(self.room)):
            for col in range(0, len(self.room[row])):
                if not self.room[row][col]:
                    self.room[row][col] = True
                    amount -= 1
                    if amount == 0:
                        return True

        return False

    def GetInfo(self):
        str1 = ""
        for x in range(len(self.room)):
            for y in range(len(self.room[x])):
                str1 += str(self.room[x][y]) + " | "
            str1 += "\n"
        return self.movie.GetInfo()+"\n"+str1