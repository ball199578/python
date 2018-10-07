class Student():
    # 此处必须有pass
    pass


mingyue = Student()


class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I 在做作业")
        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.doHomework()


