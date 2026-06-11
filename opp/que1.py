# Q1

class Employee :
    __salary = 50000

    def Increment(self):
        self.__salary += 10000

    def Deduct(self):
        self.__salary -= 5000

    def GetSalary(self):
        print(self.__salary)


emp1 = Employee()
emp2 = Employee()

emp1.GetSalary()
emp1.Increment()
emp1.Deduct()
emp1.GetSalary()

emp2.GetSalary()
emp2.Increment()
emp2.Deduct()
emp2.GetSalary()