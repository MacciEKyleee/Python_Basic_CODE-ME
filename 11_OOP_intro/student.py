# studentjan = {
#     'imie' : 'Jan',
#     'nazwisko' : 'Kowalski',
#     'wiek' : 23,
#     'kierunek' : 'Informatyka'
# }

class Student(): #klasa
    university = 'UAM'
    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        self.email = f'{self.lastname}.{self.firstname}@{self.university}.pl'.lower()

    def email(self):
        return f'{self.lastname}.{self.firstname}@{self.university}.pl'.lower()


#stwórz obietk instancję klasy Student

obj_anna = Student('Anna','Kowalska','Informatyka',)

print(obj_anna.firstname, obj_anna.lastname,obj_anna.subject,obj_anna.university, obj_anna.email)


obj_jan = Student('Jan','Nowak','Biologia',)

print(obj_jan.firstname, obj_jan.lastname, obj_jan.subject, obj_jan.university, obj_jan.email)

print(Student.email(obj_anna))
# print(obj_jan.imie, obj_jan.name)