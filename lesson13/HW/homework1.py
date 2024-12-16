class Student:

    def __init__(self, name, surname, age, average_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.__average_mark = average_mark

    def change_average_mark(self, new_mark):
        self.__average_mark = new_mark

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.__average_mark}"


Artem = Student("Artem", "Drobotun", 22, 80)
print(Artem.__str__())
Artem.change_average_mark(99)
print(Artem.__str__())
