from django.db import models

class VirtualMachine(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Stopped')

