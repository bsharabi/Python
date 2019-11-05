class SchoolMember:
    def __init__(self, name):
        self.name = name

    def tell(self):
        print('hello SchoolMember',self.name, end=" ")

# If subclass does not contain a constructor
# The subclass will have a default call to the base constructor
class Teacher(SchoolMember):
    def tell(self):
        SchoolMember.tell(self)
        print('and Teacher')


m = SchoolMember("Bob")
m.tell()
print("\n")
t = Teacher("Alice")
t.tell()
