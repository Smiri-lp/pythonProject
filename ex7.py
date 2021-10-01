class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

it = Person('Accul', 'Otal')
full_name = it.get_full_name()
print(f"{full_name}")

class Student(Person):
    pass
new = Student("Mike", "Olsen")
full_name = new.get_full_name()
print(f"{full_name} -st")