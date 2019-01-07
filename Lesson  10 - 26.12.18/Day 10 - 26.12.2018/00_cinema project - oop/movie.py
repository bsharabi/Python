class Movie:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def get_info(self):
        return "name: "+self.name +" ,length: " + str(self.length)
