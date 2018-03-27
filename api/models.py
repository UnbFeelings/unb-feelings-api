from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str(self):
        return self.description
