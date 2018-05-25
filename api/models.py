from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Campus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.name


class Student(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    # Override username to set unique constraint to False
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
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
    description = models.CharField(max_length=200, unique=True)
    _quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def quantity(self):
        return len(self.post_set.all())

    def __str__(self):
        return self.description


class Post(models.Model):
    EMOTIONS = (
        ('b', 'Bad'),
        ('g', 'Good'),
    )

    content = models.CharField(max_length=280)
    tag = models.ManyToManyField(Tag, blank=True, related_name="posts")
    author = models.ForeignKey(Student, on_delete=None, related_name="posts")
    subject = models.ForeignKey(
        Subject,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="posts")
    emotion = models.CharField(max_length=1, choices=EMOTIONS, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        tags = ['#' + tag.description for tag in self.tag.all()]
        tags_str = '(' + ', '.join(tags) + ')'

        fields = [
            self.content, tags_str, self.author.username, self.subject,
            self.emotion
        ]
        out = ', '.join(map(str, fields))
        return out


def validate_post_emotion_choice(sender, instance, **kwargs):
    valid_emotions = [t[0] for t in sender.EMOTIONS]

    if instance.emotion not in valid_emotions:

        raise ValidationError(
            'Post Emotion "{}" is not one of the permitted values: {}'.format(
                instance.emotion, ', '.join(valid_emotions)))


models.signals.pre_save.connect(validate_post_emotion_choice, sender=Post)
