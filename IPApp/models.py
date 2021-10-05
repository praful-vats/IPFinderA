from django.db import models


class HOST(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=100, blank=True)
    ipv4 = models.CharField(max_length=100, blank=True)
    ipv6 = models.CharField(max_length=100, blank=True)
    # password = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.hostname
