class Employee:
    language = "python"
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


tanvir = Employee()
tanvir.greet()
tanvir.getinfo()