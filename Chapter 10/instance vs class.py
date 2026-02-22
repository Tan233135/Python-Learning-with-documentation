class Employee:
    language = "python"  #This is a class attribute
    salary = 12000

Tanvir = Employee()
Tanvir.language = "Javascript"   #This is a instance language
print(Tanvir.language, Tanvir.salary)

#The output will be language=python. As instance is more prioratized then class attribute
