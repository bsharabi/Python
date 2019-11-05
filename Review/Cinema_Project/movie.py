class Movie:

	def __init__(self,MovieName,MovieLength):
		self.MovieName=MovieName
		self.MovieLength=MovieLength

	def GetInfo(self):
		return "The movie is {}\nThe length movie is {}".format(self.MovieName,self.MovieLength)


