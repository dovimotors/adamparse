from dbftopandas import AdamImport

ai = AdamImport()

i = 'c:\winADAM\Incar\Data\INVEN.DBF'
o = 'c:\\apps\output.csv'
t = 'csv'

ai.DBFConverter(i,o,t)

