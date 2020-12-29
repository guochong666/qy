from django.db import models

class TemplateId(models.Model):
    ID = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    class Meta:
        db_table = 'templateid'
        
    def __str__(self):
        return self.ID + " " + self.name