from django.db import models


class HOSTNAME(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(null=True, max_length=100)
    password = models.CharField(max_length=100, null=True)
    # password = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

