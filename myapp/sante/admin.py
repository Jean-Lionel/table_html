from django.contrib import admin
from .models import Commande

# Register your models here.

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('groupe_sanguin', 'date', 'quantite_recu','service','quantite_restant',
    	'quantite_demandee','quantite_servi','observations')

admin.site.register(Commande,CommandeAdmin)