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
    _quantity = models.IntegerField(default=0, null=True, blank=True)
    
    @property
    def quantity(self):
        return len(self.post_set.all())

    def __str__(self):
        return self.description

class Post(models.Model):
    content = models.CharField(max_length=280)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
