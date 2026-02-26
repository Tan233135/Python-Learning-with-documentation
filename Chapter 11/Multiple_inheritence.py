class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

'''class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
'''
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languges here is your language: {self.language}")

class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguges()
b.showLanguage()
