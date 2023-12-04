from django.db import models

# Create your models here.

class Employee(models.Model):
    email=models.EmailField(null=True)
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.uname

class Student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)


class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    p_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.author
    
    def __str__(self):
        return self.p_year
    
    def __str__(self):
        return self.genre
