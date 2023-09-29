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
        
class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Categorias(models.Model):
    id_categoria = models.AutoField(db_column='ID_categoria', primary_key=True)  # Field name made lowercase.
    nombre_categoria = models.CharField(db_column='Nombre_categoria', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categorias'