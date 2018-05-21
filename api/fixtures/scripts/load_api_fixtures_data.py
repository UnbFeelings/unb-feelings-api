import os
from xml.dom import minidom

from api.models import (
    Campus, Course, Post, Student, Subject, Tag,
)

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

print('BASE_DIR = {}'.format(BASE_DIR))
xml = minidom.parse(BASE_DIR + '/disciplinas.xml')
items_root = xml.getElementsByTagName('items')[0]

ENGENHARIA = items_root.getElementsByTagName('ENGENHARIA')
SOFTWARE = items_root.getElementsByTagName('SOFTWARE')
ELETRONICA = items_root.getElementsByTagName('ELETRONICA')
AEROESPACIAL = items_root.getElementsByTagName('AEROESPACIAL')
ENERGIA = items_root.getElementsByTagName('ENERGIA')

print("Getting or creating campus FGA")
fga = Campus.objects.get_or_create(name="FGA")[0]

print("Getting or creating couse Engenharia")
engenharia = Course.objects.get_or_create(name="ENGENHARIA", campus=fga)[0]

print("Getting or creating couse software")
software = Course.objects.get_or_create(name="SOFTWARE", campus=fga)[0]

print("Getting or creating couse eletronica")
eletronica = Course.objects.get_or_create(name="ELETRONICA", campus=fga)[0]

print("Getting or creating couse aeroespacial")
aeroespacial = Course.objects.get_or_create(name="AEROESPACIAL", campus=fga)[0]

print("Getting or creating couse energia")
energia = Course.objects.get_or_create(name="ENERGIA", campus=fga)[0]

print("\nCOURSE ENGENHARIA")
for s in ENGENHARIA:
    name = s.firstChild.nodeValue
    print("\tGetting or creating subject {}".format(name))
    sub = Subject.objects.get_or_create(name=name, course=engenharia)[0]

print("\nCOURSE SOFTWARE")
for s in SOFTWARE:
    name = s.firstChild.nodeValue
    print("\tGetting or creating subject {}".format(name))
    sub = Subject.objects.get_or_create(name=name, course=software)[0]

print("\nCOURSE ELETRONICA")
for s in ELETRONICA:
    name = s.firstChild.nodeValue
    print("\tGetting or creating subject {}".format(name))
    sub = Subject.objects.get_or_create(name=name, course=eletronica)[0]

print("\nCOURSE AEROESPACIAL")
for s in AEROESPACIAL:
    name = s.firstChild.nodeValue
    print("\tGetting or creating subject {}".format(name))
    sub = Subject.objects.get_or_create(name=name, course=aeroespacial)[0]

print("\nCOURSE ENERGIA")
for s in ENERGIA:
    name = s.firstChild.nodeValue
    print("\tGetting or creating subject {}".format(name))
    sub = Subject.objects.get_or_create(name=name, course=energia)[0]

print("\nFGA STUDENTS")
fga_courses = [engenharia, software, eletronica, aeroespacial, energia]

for i, course in enumerate(fga_courses):
    username = 'student_' + course.name
    email = username + '@b.com'
    print("\tGetting or creating student {}".format(username))
    Student.objects.get_or_create(username=username, email=email, course=course)[0]

print("\nTAGs")
tags = ["boladao", "antietico", "cortella", "avestruz", "changemymind", "tanadisney"]
for tag in tags:
    print("\tGetting or creating tag {}".format(tag))
    Tag.objects.get_or_create(description=tag)[0]


print("\nPOST")
for tag in Tag.objects.all():
    pass

contents = ["Trueborn son of Lannister.",
            "Tell my lord father",
            "Jon said.",
            "He favored Jon with a rueful grin.", \
            "All dwarfs may be bastards",
            "Whistling a tune.",
            "Just a moment", \
            "Tyrion Lannister stood tall as a king.",
            "― George R.R. Martin",]

for i, content in enumerate(contents):
    student = Student.objects.all()[i % Student.objects.count()]
    subject = Subject.objects.all()[i % Subject.objects.count()]
    emotion = Post.EMOTIONS[i % 2]

    post, created = Post.objects.get_or_create(content=content, author=student, subject=subject, emotion=emotion)
    if created:
        tags = Tag.objects.all()[i:]
        post.tag.add(*tags)
        post.save()

    print("\tGetting or creating post {}".format(post))
