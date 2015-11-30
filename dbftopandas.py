from dbfpy import dbf
import csv
import pandas as pd
import numpy as np

db = dbf.Dbf('deal.dbf')
fpath = 'output.csv'
f = open(fpath,'w')
hdr = []
c = csv.writer(f)

for fieldName in db.fieldNames:
    hdr += [fieldName]

c.writerow(hdr)

for rec in db:
    c.writerow(rec.asList())


from_csv = pd.read_csv(fpath)

print from_csv.head()



