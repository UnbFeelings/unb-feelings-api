from django.core.management.base import BaseCommand, CommandError
from api.models import Subject, Course, Campus
import xml.etree.ElementTree as ET
import os

class Command(BaseCommand):
    help = 'Populates the subjects table'

    def handle(self, *args, **options):
        dirr = os.path.dirname(__file__)
        filename = os.path.join(dirr, '../../fixtures/disciplinas.xml')
        tree = ET.parse(filename)
        root = tree.getroot()
        subjects = []
        subject = Subject.objects.all()
        self.create_campuses()
        self.create_courses()
        if subject.count() <= 0:
           for child in root:
            for v in child:
                c = Subject(name=v.text, course=Course.objects.get(name=v.tag))
                match = [c1.name for c1 in subjects if c1.name == c.name]
                if match == []:
                    subjects.append(c)
        if len(subjects):
            Subject.objects.bulk_create(subjects)
            self.stdout.write("Subjects added!")
        else:
            self.stdout.write("No subjects added. Please remove already inserted subjects from db!")

    def create_campuses(self):
        c = Campus.objects.all()
        if c.count() <= 0:
            campuses_name = ["FGA" ,"FCE", "DARCY RIBEIRO", "FUP"]
            campuses = []
            for name in campuses_name:
                campus = Campus(name=name)
                campuses.append(campus)

            Campus.objects.bulk_create(campuses)
            self.stdout.write("Campuses added!")
        else:
            self.stdout.write("No campuses added. Please remove already inserted campuses from db!")

    def create_courses(self):
        c = Course.objects.all()
        if c.count() <= 0:
            courses_name = ["ENGENHARIA" ,"SOFTWARE", "ELETRONICA", "AEROESPACIAL", "ENERGIA", "AUTOMOTIVA"]
            courses = []
            for name in courses_name:
                course = Course(name=name, campus=Campus.objects.get(pk=1)) # fix logic to add other campuses courses
                courses.append(course)

            Course.objects.bulk_create(courses)
            self.stdout.write("Courses added!")
        else:
            self.stdout.write("No courses added. Please remove already inserted courses from db!")
