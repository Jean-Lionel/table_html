from django.db import models

# Create your models here.

class Commande(models.Model):
	groupes_sanguis_list = (
		("A+","A+"),
		("B+","B+"),
		("AB+","AB+"),
		("O+","O+"),
		("A-","A-"),
		("B-","B-"),
		("AB-","AB-"),
		("O-","O-"),
		)
 	 	 			
	services=(
		("Pédiatrie","Pédiatrie"),
		("Maternité","Maternité"),
		("Médecine interne","Médecine interne"),
		("Bloc Opératoire","Bloc Opératoire"),
		("Néonatologie","Néonatologie"),
		("Autres services","Autres services"),
		("Quantité détruite","Quantité détruite"),
		)

	groupe_sanguin = models.CharField(max_length=25,choices=groupes_sanguis_list)
	date = models.DateField()
	quantite_recu = models.FloatField()
	service = models.CharField(max_length=50, choices=services)
	quantite_restant = models.FloatField()
	quantite_demandee = models.FloatField()
	quantite_servi = models.FloatField()
	observations = models.TextField()

