class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name} \nAge : {self.age}") 

class Student(Person):
        School_name = "ABC School"

        def __init__(self, name, age,class_name,roll,marks = 0):
            super().__init__(name, age)

            self.class_name = class_name
            self.roll = roll
            self.__marks = 0
            self.set_marks(marks)

        #setter method