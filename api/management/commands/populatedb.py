from django.core.management.base import BaseCommand, CommandError
from api.models import Subject, Course
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
            