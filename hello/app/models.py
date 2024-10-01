from django.db import models
from django.db.models import F

class Person(models.Model):
 name = models.CharField(max_length=20)
 age = models.IntegerField()
 objects = models.Manager()
 DoesNotExist = models.Manager
class Company(models.Model):
 name = models.CharField(max_length=30)
class Product(models.Model):
 company = models.ForeignKey(Company, on_delete=models.CASCADE)
 name = models.CharField(max_length=30)
 price = models.IntegerField()
class Course(models.Model):
 name = models.CharField(max_length=30)
class Student(models.Model):
 name = models.CharField(max_length=30)
 courses = models.ManyToManyField(Course)

class User(models.Model):
 name = models.CharField(max_length=20)
class Account(models.Model):
 login = models.CharField(max_length=20)
 password = models.CharField(max_length=20)
 user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# создаем объект Company с именем Электрон
#firma = Company.objects.create(name=" Электрон")
# создание товара компании
#firma.product_set.create(name="Samsung S20", price=42000)
# отдельное создание объекта с последующим добавлением в БД
#ipad = Product(name="iPad", price=34200)
# при добавлении необходимо указать параметр bulk =False
#firma.product_set.add(ipad, bulk=False)
# исключает из компании все товары,
# при этом товары остаются в БД и не привязаны к компании
# работает, если в зависимой модели ForeignKey(Company, null = True)
#firma.product_set.clear()
# то же самое, только в отношении одного объекта
#ipad = Product.objects.get(name="iPad")
#firma.product_set.remove(ipad)

# создадим студента
#stud_viktor = Student.objects.create(name="Виктор")
# создадим один курс и добавим его в список курсов Тома
#stud_viktor.courses.create(name="Математика")
# получим все курсы студента
#all_courses = Student.objects.get(name="Виктор").courses.all()
# получаем всех студентов, которые посещают курс Алгебра
#all_students = Student.objects.filter(courses__name="Математика")

# создадим курс
#kurs_python = Course.objects.create(name="Python")
# создаем студента и добавляем его на курс
#kurs_python.student_set.create(name="Виктор")
# отдельно создаем студента и добавляем его на курс
#sam = Student(name="Александр")
#sam.save()
#kurs_python.student_set.add(sam)
# получим всех студентов курса
#students = kurs_python.student_set.all()
# получим количество студентов по курсу
#number = kurs_python.student_set.count()
# удялем с курса одного студента
#kurs_python.student_set.remove(sam)
# удаляем всех студентов с курса
#kurs_python.student_set.clear()

# создадим пользователя
#alex = User.objects.create(name="Александр")
     
# создадим аккаунт пользователя
#acc = Account.objects.create(login = "1234", password="6565", user=alex)
#alex.account = acc
#alex.account.save()
 
# обновляем данные
#alex.account.login = "qwerty"
#alex.account.password = "123456"
#alex.account.save()




#igor = Person (name="Игорь", age=23)
#igor.save()

# klient1 = Person.objects.get(name="Виктор")
# klient2 = Person.objects.get(age=25)
# klient3 = Person.objects.get(name="Василий",age=23)

# bob, created = Person.objects.get_or_create(name="Bob",age=24)
# print(bob.name)
# print(bob.age)

# people = Person.objects.exclude(age=23)

# people = Person.objects.filter(age=23)
# people2 = Person.objects.filter(name="Tom", age="23")

# people = Person.objects.filter(name="Tom").exclude(age=23)

# people = Person.objects.in_bulk()
# for id in people:
#  print(people[id].name)
#  print(people[id].age)

# people2 = Person.objects.in_bulk([1,3])
# for id in people2:
#  print(people2[id].name)
#  print(people2[id].age)

# nic = Person.objects.get(id=2)
# nic.name = "Николай Петров"
# nic.save()

# nic = Person.objects.get(id=2)
# nic.name = "Николай Петров"
# nic.save(update_fields=["name"])

# Person.objects.filter(id=2).update(name="Михаил")

# Person.objects.all(id=2).update(age =F("age")+1)

# Person.objects.all().update(name="Михаил")
# Person.objects.all().update(age =F("age")+1)

# values_for_update={"name":"Михаил", "age":31}
# bob, created = Person.objects.update_or_create(id=2, defaults= values_for_update)

# person = Person.objects.get(id=2)
# person.delete()

# Person.objects.filter(id=4).delete()
# people = Person.objects.filter(name="Tom").exclude(age=34)
# print(people.query)