# CLASS
class Student:
    college_name = "ABC COLLEGE" #class attribute
    def __init__(self,fullname,marks):
        self.name = fullname #object attribute
        self.marks = marks
        
    # METHOD
    def welcome(self):
        print("Welcome student",self.name)
        
    def get_marks(self):
        return self.marks
       
# OBJECT
s1 = Student('Prayash', 98)
s1.welcome()
print(s1.get_marks())

# QUESTION
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("Hello")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello",self.name,"your avg marks in three subject is",sum/3)
    
s1 = Student('Prayash',[98,95,96])
s1.get_avg()
s1.hello()

# ABSTRACTION
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started..")
        
    def stop(self):
        self.brk = True
        print("Car stopped..")
        
Car1 = Car()
Car1.start()
Car1.stop()
