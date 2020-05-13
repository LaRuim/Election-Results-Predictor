import time
class Student:
    count=0
    def __init__(self, name):
        self.name = name
        Student.count += 1
    @staticmethod
    def display():
        print(Student.count)
    def __del__(self):
        time.sleep(1)
        print('Deleting')
        Student.count -= 1

a = Student("Chethas")
a.display()
b = Student("Apoorva")
b.display()