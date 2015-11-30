from dbfpy import dbf
import csv
import pandas as pd
import numpy as np


class AdamImport:
    def convert(self, filename):
        #create the DBF reader object
        db = dbf.Dbf(filename)
        #create the file to output CSV data to
        fpath = 'output.csv'
        f = open(fpath,'w')
        #initiat the header container and CSV writer
        hdr = []
        c = csv.writer(f)

        #loop through all the field names and create the header row
        for fieldName in db.fieldNames:
            hdr += [fieldName]

        #write the head to the CSV file
        c.writerow(hdr)

        #loop through all the records and write each line to the CSV file
        for rec in db:
            #using asList makes a list as opposed to asDict
            c.writerow(rec.asList())

        #take the csv file and open it as a pandas dataframe
        from_csv = pd.read_csv(fpath)

        #close the CSV file
        f.close()
        #return a dataframe object
        return from_csv



