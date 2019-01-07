class Movie:
	def __init__(self,NameMovie,lenght):
		self.NameMovie=NameMovie
		self.lenght=lenght

	def getinfo(self):
		return "Name is : {} , Lenght is : {}".format(self.NameMovie,self.lenght)
