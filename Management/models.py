from django.db import models

class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.id