class Student:
    sumAge=0
    sumScore=0
    sum_student=0
    def __init__(self,Score,Age):
        self.Score=Score
        self.Age=Age
        Student.sumAge+=Age
        Student.sumScore+=Score
        Student.sum_student+=1

    def print_stud(self):
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



print("----------------------------")
S1 = Student(100,22)
S1.print_stud()
Student.Avg_Score()
Student.Avg_Age()
print("----------------------------")


print("----------------------------")
S2 = Student(80,45)
S2.print_stud()
Student.Avg_Score()
Student.Avg_Age()
print("----------------------------")

print("----------------------------")
S3 = Student(65,25)
S3.print_stud()
Student.Avg_Score()
Student.Avg_Age()
print("----------------------------")


print("----------------------------")
S4 = Student(35,26)
S4.print_stud()
Student.Avg_Score()
Student.Avg_Age()
print("----------------------------")