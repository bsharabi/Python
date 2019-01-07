class Cinema:
    def __init__(self):
        self.arr_room = [] 
        self.arr_movie = []
        self.max_movie=100
        self.max_room=6

    def add_room(self,room):
        if len(self.arr_room) < self.max_room:
            self.arr_room.append(room)



    def add_movie(self,movie):
        if len(self.arr_movie) < self.max_movie:
            self.arr_movie.append(movie)


    def order_seats(self,amount,name):
        for ind in range(0,len(self.arr_room)):
            if self.arr_room[ind].movie.NameMovie==name:
                return self.arr_room[ind].room_seat(amount)
        return False


    def get_info(self):
        room_status="\n"
        for ind in range(0,len(self.arr_room)):
            room_status+=self.arr_room[ind].getinfo()          
            room_status+="\n________________________________________________\n"
        return room_status