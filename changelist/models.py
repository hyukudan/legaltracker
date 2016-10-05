# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Law(models.Model):
        name = models.CharField(max_length=200)
        CIVIL = 'CV'
        PENAL = 'PN'
        SOCIAL = 'SO'
        ADMINISTRATIVO = 'AD'
        area_choices = (
                (CIVIL, 'Civil'),
                (PENAL, 'Penal'),
                (SOCIAL, 'Social'),
                (ADMINISTRATIVO, 'Administrativo'),
        )
        area = models.CharField(
                max_length=2,
                choices = area_choices,
                default = CIVIL,
        )
	total_articles = models.IntegerField(default=0)
        date_last_revision = models.DateTimeField('Última modificación')
        def __str__(self):
                return self.name.encode('utf8')

class articleLaw(models.Model):
	fromLaw = models.ForeignKey(Law)
	article = models.IntegerField(default=0)
	text = models.CharField(max_length=200)
	version = models.IntegerField(default=0)

class textLaw(models.Model):
        law = models.ForeignKey(Law)
        revision_text = models.CharField(max_length=200)
        revision_date = models.DateTimeField('Actualización de fecha')

        def __str__(self):
		return self.law.name.encode('utf8')

class Company(models.Model):
        nameCompany=models.CharField(max_length=200)
        NIF=models.CharField(max_length=10)
	mail=models.CharField(max_length=200,default="info@localhost.com")
        def __str__(self):
                return self.nameCompany.encode('utf8')

class Contract(models.Model):
	nameContract=models.CharField(max_length=200)
	applied_laws=models.ManyToManyField(articleLaw)
	
	class Meta:	
		verbose_name = 'contrato'
        	verbose_name_plural = 'contratos'
        def __str__(self):
                return self.nameContract.encode('utf8')

