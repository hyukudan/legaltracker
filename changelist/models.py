# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class datePublished(models.Model):
	date_publication = models.DateField('Versión de fecha',default=now)

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
        date_publication = models.DateField('Versión de fecha',default=now)
        def __str__(self):
                return self.name.encode('utf8')

class articleLaw(models.Model):
	fromLaw = models.ForeignKey(Law)
	article = models.IntegerField(default=0)
	text = models.TextField(default="")
	version = models.DateField(default=now)

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
	ownerContract = User
	nameContract=models.CharField(max_length=200)
	textContract=models.TextField(default="")
	applied_laws=models.ManyToManyField(articleLaw)
	dateLastRevision=models.DateTimeField(default=now)
	isUpdated=models.BooleanField(default=True)

	class Meta:	
		verbose_name = 'contrato'
        	verbose_name_plural = 'contratos'
        
	def __str__(self):
                return self.nameContract.encode('utf8')

	def showAppliedLaws(self):
		return('1')		

	def saveAppliedLaws(self):
		return('1')
