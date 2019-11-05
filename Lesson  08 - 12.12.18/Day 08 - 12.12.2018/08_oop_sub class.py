class SchoolMember:
    def tell(self):
        print('hello SchoolMember', end=" ")


class Teacher(SchoolMember):
    def tell(self):
        SchoolMember.tell(self)
        print('and Teacher')


m = SchoolMember()
t = Teacher()

t.tell()
m.tell()


"""
OUTPUT:
____________________________________

hello SchoolMember and Teacher
hello SchoolMember

"""
