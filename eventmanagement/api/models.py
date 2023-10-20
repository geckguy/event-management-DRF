from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
