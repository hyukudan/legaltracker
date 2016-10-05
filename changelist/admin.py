# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import Law, textLaw, Company, Contract, articleLaw

class articleInline(admin.TabularInline):
	model = articleLaw
	extra = 1

class articlesInline(admin.TabularInline):
    	model = Contract.applied_laws.through


class LawAdmin(admin.ModelAdmin):
	fieldsets=[
                (None, {'fields' : ['name','area']}),
                (None, {'fields' : ['date_publication']}),

	]
	list_filter = ['date_publication']
        search_fields = ['name']

	inlines = [articleInline]


class articleLawAdmin(admin.ModelAdmin):
        list_display = ('article','text')
        list_filter = ['fromLaw']
        search_fields = ['text']

class contractAdmin(admin.ModelAdmin):
	search_fields = ['nameContract']
	list_display = ('nameContract','ownerContract')
        fieldsets=[
                (None, {'fields' : ['nameContract','isUpdated','dateLastRevision']}),
		('Contenido', {'fields' : ['textContract']}),
		
        ]
	inlines = [articlesInline]


admin.site.register(Law, LawAdmin)
admin.site.register(textLaw)
admin.site.register(Company)
admin.site.register(Contract, contractAdmin)
admin.site.register(articleLaw,articleLawAdmin)
