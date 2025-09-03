class Student:
    def __init__(self,marks):
        self.marks=marks
        self.total()
    def total(self):
        self.total=0
        for i in  self.marks:
            self.total=self.total+i
        print(self.total)
    def rank(*self):
        l=[]
        for i in self:
            l.append(i.total)
        print(l)
        sort=sorted(l)
        print(l)


ramya=Student([100,95,97,92,95])
roja=Student([95,96,97,92,98])
Student.rank(roja,ramya)
# class Student:
#     def __init__(self,*marks):
#         self.m1 = marks[0]
#         self.m2 = marks[1]
#         self.m3 = marks[2]
#         self.m4 = marks[3]
#         self.m5 = marks[4]
#         self.total()
#     def total(self):
#         self.total=self.m1+self.m2+self.m3+self.m4+self.m5
#         print(self.total)
#     def rank(self,other):
#         if ramya.total>roja.total:
#             print('1.Ramya')
#         else:
#             print('1.Roja')
# ramya=Student(100,95,97,92,95)
# roja=Student(95,96,97,92,98)
# ramya.total()
# roja.total()
# Student.rank(ramya,roja)
