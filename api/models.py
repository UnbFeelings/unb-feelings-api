from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    # Override username to set unique constraint to False
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.DO_NOTHING,
        related_name="users",
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


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
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Student, on_delete=None)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
