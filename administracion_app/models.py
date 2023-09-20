from django.db import models

# Create your models here.
class Marcas(models.Model):
    id_marcas = models.AutoField(db_column='ID_marcas', primary_key=True)  # Field name made lowercase.
    nombre_marca = models.CharField(db_column='Nombre_marca', max_length=80, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marcas'