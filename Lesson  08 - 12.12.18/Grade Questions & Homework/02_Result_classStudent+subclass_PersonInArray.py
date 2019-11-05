arr=[]

class Person:

    def __init__(self,name,lname):
        self.name=name
        self.lname=lname

    def print1(self):
         print("my name is {}\nlast name is {}".format(self.name,self.lname))

class Student(Person):
    sumAge=0
    sumScore=0
    sum_student=0
    
    def __init__(self,Score,Age,name,lname):
        self.Score=Score
        self.Age=Age
        Person.__init__(self,name,lname)
        Student.sumAge+=Age
        Student.sumScore+=Score
        Student.sum_student+=1

    def print_stud(self):
        Person.print1(self)
        print("The score of student is {}".format(self.Score))
        print("The age of student is {}".format(self.Age))
        
        

    @classmethod
    def Avg_Score(S):
        if(Student.sum_student!=0):
            print("The average of Score {} for {} Student".format(S.sumScore/S.sum_student,S.sum_student))
        else:
            print("The average of Score {} for {} Student".format(S.sumScore,S.sum_student))

    @classmethod
    def Avg_Age(A):
        if(Student.sum_student!=0):
            print("The average of age {} for {} Student".format(A.sumAge/A.sum_student,A.sum_student))
        else:
            print("The average of age {} for {} Student".format(A.sumAge,A.sum_student))


def getStudent(size):
    grade=None
    age=None
    for x in range(size):
        name=input("Enter your name\n")
        lname=input("Enter your Last name\n")
        while grade<0 or grade >100 or grade == None:
            grade=int(input("Enter your grade\n"))
        while age<0 or age >120 grade == None:
            age=int(input("Enter your age\n"))
        arr.append(Student(grade,age,name,lname))
        grade=None
        age=None
        

def PrintStudent():
    for x in arr:
        x.print_stud()
        print("\n")

    Student.Avg_Score()
    Student.Avg_Age()


getStudent(3)
PrintStudent()