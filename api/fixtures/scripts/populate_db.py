
from api.models import (
    Campus, Course, Post, Student, Subject, Tag, Emotion
)

#populate
# Creating campus
Campus.objects.create(name='Campus FGA')
Campus.objects.create(name='Campus Darcy Ribeiro')

# Creating courses
# for FGA campus
Course.objects.create(name='Engenharia de Software', campus=Campus.objects.filter(name='Campus FGA')[0])
Course.objects.create(name='Engenharia Eletrônica', campus=Campus.objects.filter(name='Campus FGA')[0])
# for Darcy campus
Course.objects.create(name='Direito', campus=Campus.objects.filter(name='Campus Darcy Ribeiro')[0])
Course.objects.create(name='Medicina', campus=Campus.objects.filter(name='Campus Darcy Ribeiro')[0])

# Creating subjects
Subject.objects.create(name='Cálculo 1', course=Course.objects.filter(name='Engenharia de Software')[0])
Subject.objects.create(name='PED 1', course=Course.objects.filter(name='Engenharia Eletrônica')[0])
Subject.objects.create(name='Introdução ao Direito 1', course=Course.objects.filter(name='Direito')[0])
Subject.objects.create(name='Citologia', course=Course.objects.filter(name='Medicina')[0])
Subject.objects.create(name='Computação Básica', course=Course.objects.filter(name='Engenharia de Software')[0])
Subject.objects.create(name='TED 1', course=Course.objects.filter(name='Engenharia Eletrônica')[0])
Subject.objects.create(name='Teoria Geral do Estado', course=Course.objects.filter(name='Direito')[0])
Subject.objects.create(name='Psicologia Médica', course=Course.objects.filter(name='Medicina')[0])

# Creating Students
Student.objects.create(username='AlunoSoftware1', email='aluno_soft1@gmail.com', course=Course.objects.filter(name='Engenharia de Software')[0])
Student.objects.create(username='AlunoSoftware2', email='aluno_soft2@gmail.com', course=Course.objects.filter(name='Engenharia de Software')[0])

Student.objects.create(username='AlunoEletronica1', email='aluno_eletronica1@gmail.com', course=Course.objects.filter(name='Engenharia Eletrônica')[0])
Student.objects.create(username='AlunoEletronica1', email='aluno_eletronica2@gmail.com', course=Course.objects.filter(name='Engenharia Eletrônica')[0])

Student.objects.create(username='AlunoDireito1', email='aluno_dir1@gmail.com', course=Course.objects.filter(name='Direito')[0])
Student.objects.create(username='AlunoDireito2', email='aluno_dir2@gmail.com', course=Course.objects.filter(name='Direito')[0])

Student.objects.create(username='AlunoMedicina1', email='aluno_med1@gmail.com', course=Course.objects.filter(name='Medicina')[0])
Student.objects.create(username='AlunoMedicina2', email='aluno_med2@gmail.com', course=Course.objects.filter(name='Medicina')[0])

# Creating Emotions

Emotion.objects.create(emotion_type='g', image_link='cool-website/with/cool-images/good')
Emotion.objects.create(emotion_type='b', image_link='cool-website/with/cool-images/bad')
