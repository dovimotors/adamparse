from django.core.management.base import BaseCommand
from adam.models import ADAMFiles
from dashboard.models import PartsInv
import pandas as pd

class Command(BaseCommand):

    def handle(self, *args, **options):
        """
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
        """

        ifile = 'F:\\adamexports\csvfiles\INVEN.csv'
        inv = pd.read_csv(ifile)
        ext = inv.ONHAND * inv.COST
        ext = sum(ext)
        print ext