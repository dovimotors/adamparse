from django.db import models

# Create your models here.
class ADAMFiles(models.Model):
    def __str__(self):
        return self.DBFPath



    DBFPath = models.FilePathField(
        path='c:\winADAM\\',
        recursive=True,
    )



