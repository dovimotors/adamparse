from dbftopandas import AdamImport

ai = AdamImport()

i = 'f:\\adamexports\\adamcache\Apcar\Data\\aparcinv.dbf'
#o = 'c:\\apps\output.csv'
#t = 'csv'

#ai.DBFConverter(i,o,t)

#t = 'pandas'

#pd = ai.DBFConverter(i,o,t)

#print pd.head()

headers = ai.GetColNames(i)

print headers

i = 'f:\\adamexports\\adamcache\Apcar\Data\\apinv.dbf'

headers = ai.GetColNames(i)

print headers

#data_types = ai.GetColNamesAndTypes(i)

#for d in data_types:
#    if data_types[d] == 'NoneType':
#        print d, data_types[d]

