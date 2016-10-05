# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import Law, textLaw, Company, Contract, articleLaw

class LawAdmin(admin.ModelAdmin):
        list_display = ('name','area')
	list_filter = ['date_last_revision']
	search_fields = ['name']

class articleLawAdmin(admin.ModelAdmin):
        list_display = ('article','text')
        list_filter = ['fromLaw']
        search_fields = ['text']



admin.site.register(Law, LawAdmin)
admin.site.register(textLaw)
admin.site.register(Company)
admin.site.register(Contract)
admin.site.register(articleLaw,articleLawAdmin)
