from api.models import Course, Post, Student, Subject, Tag

print("GETTINGS courses")
engenharia = Course.objects.get(name="ENGENHARIA")
software = Course.objects.get(name="SOFTWARE")
eletronica = Course.objects.get(name="ELETRONICA")
aeroespacial = Course.objects.get(name="AEROESPACIAL")
energia = Course.objects.get(name="ENERGIA")

print("\nFGA STUDENTS")
fga_courses = [engenharia, software, eletronica, aeroespacial, energia]

for i, course in enumerate(fga_courses):
    username = 'student_' + course.name
    email = username + '@b.com'
    print("\tCreating student {}".format(username))
    student = Student.objects.create(email=email, course=course)
    student.set_password("test")
    student.save()

print("\nTAGs")
tags = [
    "boladao", "antietico", "cortella", "avestruz", "changemymind",
    "tanadisney"
]
for tag in tags:
    print("\tCreating tag {}".format(tag))
    Tag.objects.create(description=tag)

print("\nPOST")

contents = [
    "Trueborn son of Lannister.",
    "Tell my lord father",
    "Jon said.",
    "He favored Jon with a rueful grin.",
    "All dwarfs may be bastards",
    "Whistling a tune.",
    "Just a moment",
    "Tyrion Lannister stood tall as a king.",
    "― George R.R. Martin",
]

for i, content in enumerate(contents):
    student = Student.objects.all()[i % Student.objects.count()]
    subject = Subject.objects.all()[i % Subject.objects.count()]
    for j in range(5):
        emotion = Post.EMOTIONS[j % 2][0]
        post = Post.objects.create(content=content, author=student,
                subject=subject, emotion=emotion)
        tags_set = Tag.objects.all()
        tags = tags_set[i % tags_set.count()]
        post.tag.add(tags)
        post.save()
        print("\tCreating post {}".format(post))

