class Employee:
    language = "python"   #This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Good morning")

Tanvir = Employee()
Tanvir.language = "Javascript"
print(Tanvir.language, Tanvir.salary)
Employee.getInfo(Tanvir)
Tanvir.getInfo()
Tanvir.greet()