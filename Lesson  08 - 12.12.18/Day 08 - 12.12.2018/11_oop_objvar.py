class Robot:

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        # A instance variable
        self.name = name
        
        # When this person is created, the robot adds to the population
        Robot.population += 1



print(Robot.population)

r1 = Robot("R1")
print(r1.name)


print(Robot.population)


r2 = Robot("R2")
print(r2.name)

print(Robot.population)



"""
OUTPUT:
____________________________________

0
R1
1
R2
2
"""
