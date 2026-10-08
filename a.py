class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name} \nAge : {self.age}") 

class Student(Person):
    School_name = "ABC School"

    def __init__(self, name, age, class_name, roll, marks=0):
        super().__init__(name, age)
        self.class_name = class_name
        self.roll = roll
        self.__marks = 0
        self.set_marks(marks)  # Calls the setter for validation

    # Setter method with validation
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    # Getter method to access private marks
    def get_marks(self):
        return self.__marks

    # Optional: Overriding show_info to display student-specific details
    def show_info(self):
        super().show_info()
        print(f"School: {Student.School_name} \nClass: {self.class_name} \nRoll: {self.roll} \nMarks: {self.__marks}")
