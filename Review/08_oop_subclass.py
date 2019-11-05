class SchoolMember:
    def __init__(self, name):
        self.name = name

    def tell(self):
        print('hello SchoolMember',self.name, end=" ")

# If subclass contains a constructor
# The subclass must call to the base constructor
class Teacher(SchoolMember):

    def __init__(self, name, salary):
        SchoolMember.__init__(self, name)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('and Teacher',self.salary)


m = SchoolMember("Bob")
t = Teacher("Alice",200)


m.tell()
t.tell()

