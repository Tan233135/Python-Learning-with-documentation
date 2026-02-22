class Employee:
    language = "python"
    salary = 120000

    def __init__(self):  #Dunder method which is automatically called
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


tanvir = Employee()
tanvir.greet()
tanvir.getinfo()