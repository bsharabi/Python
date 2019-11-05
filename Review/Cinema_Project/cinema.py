class Cinema:
	
	def __init__(self):
		self.List_movie=[]
		self.List_room=[]

	def Insert_Room(self,room):
		if len(self.List_room)<=6:
			self.List_room.append(room)


	def Insert_Movie(self,movie):
		if len(self.List_movie)<=100:
			self.List_movie.append(movie)


	def order_seats(self,amount,name):
		for ind in range(0,len(self.List_room)):
			if self.List_room[ind].movie.MovieName==name:
				return self.List_room[ind].Order_Seats(amount)
		return False


	def GetInfo(self):
		room_status="\n"
		for ind in range(0,len(self.List_room)):
			room_status+=self.List_room[ind].GetInfo()          
			room_status+="\n________________________________________________\n"
		return room_status
		


