from django.db import models

from institutions_app.validators import validate_nif

class Institution(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    address = models.TextField(verbose_name="Dirección")
    creation_date = models.DateTimeField(verbose_name="Fecha de creación", auto_now=True)
    nif = models.CharField(verbose_name="NIF", max_length=9, validators=[validate_nif])