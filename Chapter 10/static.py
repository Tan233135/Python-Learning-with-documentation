class Employee:
    language = "python"
    salary = 120000

    def __init__(self, name, salary, language):  #Dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


tanvir = Employee("Tanvir", 130000, "javascript")
print(tanvir.name,tanvir.salary,tanvir.language)