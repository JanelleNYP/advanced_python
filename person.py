class Person:
    def __init__(self, name: str, date_of_birth: str, gender: str, status: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.status = status

    def speak(self):
        print(f"Hello my name is {self.name}")

    def walk(self):
        print("walking away")
        