from django.core.management.base import BaseCommand
from adam.models import ADAMFiles
from dashboard.models import PartsInv, ServiceRO
import pandas as pd
from dbftopandas import AdamImport

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

        ifile = 'F:\\adamexports\\adamcache\Incar\Data\INVEN.DBF'
        ofile = 'F:\\adamexports\csvfiles\INVEN.csv'
        out_type = 'csv'

        ai = AdamImport()
        ai.DBFConverter(ifile,ofile,out_type)

        inv = pd.read_csv(ofile)
        ext = inv.ONHAND * inv.COST
        ext = sum(ext)
        try:
            r = PartsInv(invvalue=ext)
            r.save()
            print "updated inventory value to %s" % ext
        except:
            print "There was an error updating invvalue"

        """


        ai = AdamImport()
        ai.DBFConverter(ifile,ofile,out_type)

        rofile = pd.read_csv(ofile)
        ext = rofile.ONHAND * inv.COST
        ext = sum(ext)
        try:
            r = PartsInv(invvalue=ext)
            r.save()
            print "updated inventory value to %s" % ext
        except:
            print "There was an error updating invvalue"
        """
