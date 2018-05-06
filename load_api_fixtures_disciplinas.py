from xml.dom import minidom

from api.models import Campus, Course, Subject

xml = minidom.parse('api/fixtures/disciplinas.xml')
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
