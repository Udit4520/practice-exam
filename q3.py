class person():
    def __init__(self , name , salary):
        self.nam = name
        self.sal = salary
    def increaseSalary(self , increment):
        self.sal += increment
        print("After increment the new salary is " + str(self.sal))    
        
    def displayInfo(self):
        print("Information about the person :" + "\n" + "Name : " + self.nam + "\n" + "Salary : " + str(self.sal))
person1 = person("Uditanshu" , 2000)
person1.displayInfo()
person1.increaseSalary(1000)
person1.increaseSalary(2500)