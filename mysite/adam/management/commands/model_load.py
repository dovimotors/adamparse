from django.core.management.base import BaseCommand
from adam.models import ADAMFiles

class Command(BaseCommand):

    def handle(self, *args, **options):
        a = ADAMFiles.objects.all()
        print a
        for x in a:
            print x
        print
        b = ADAMFiles.objects.filter(id=1)
        print b
        p = 'c:\winADAM\\test\\test.dbf'
        #c= ADAMFiles(DBFPath = p)
        #c.save()
        #d = ADAMFiles.objects.get(id=3)
        #d.delete()