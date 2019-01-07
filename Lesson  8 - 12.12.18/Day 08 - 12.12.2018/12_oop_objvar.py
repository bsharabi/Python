class Robot:

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        # A instance variable
        self.name = name
        
        # When this person is created, the robot adds to the population
        Robot.population += 1


    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1


    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))


    @classmethod
    def how_many(class_level):
        print("We have {} robots.".format(class_level.population))


Robot.how_many()

r1 = Robot("R1")
r1.say_hi()


Robot.how_many()

r2 = Robot("R2")
r2.say_hi()

Robot.how_many()


r2.die()

Robot.how_many()


"""
OUTPUT:
____________________________________

We have 0 robots.
Greetings, my masters call me R1.
We have 1 robots.
Greetings, my masters call me R2.
We have 2 robots.
R2 is being destroyed!
We have 1 robots.

"""