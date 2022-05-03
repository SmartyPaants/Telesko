class Student:
    school = "Siddhant's Academy"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                                                     #Instance Method, Works with instance variables
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod                                                 #To work with class methods
    def get_school(cls):                                               #Class method, Works with class variables
        return cls.school

    @staticmethod                                             #Works with neither class or instance variable
    def info():
        print('This is Student Class')


s1 = Student(12, 31, 46)
s2 = Student(23, 15, 37)
print(s1.avg())
print(s2.avg())
print(Student.info())