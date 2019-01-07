class Room:
	
	def __init__(self, movie):
		self.movie=movie
		self.matrix_seat = [[False for j in range(8)] for i in range(10)] 

	def room_seat(self,amount):
		for i in range(0,len(self.matrix_seat)) :
			for j in range(0,len(self.matrix_seat[i])):
				if not self.matrix_seat[i][j]:
					self.matrix_seat[i][j]=True
					amount-=1
				if(amount==0):
					return True			
		return False


	def getinfo(self):
		seat_room="\n"
		for i in self.matrix_seat:
			for j in i:
				if not j :
					seat_room+= "X | "
				else:
					seat_room+=	"V | "
			seat_room+="\n-------------------------------------\n"
		return seat_room+self.movie.getinfo()