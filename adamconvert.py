from dbftopandas import AdamImport

ai = AdamImport()

i = 'c:\winADAM\Sicar\Data\\arcrof.dbf'
o = 'c:\\apps\output.csv'
t = 'csv'

ai.DBFConverter(i,o,t)

