from django.db import models
from django.urls import reverse

category_choices =(
	('web', 'Web'),
	('mobile', 'Mobile' ),
	('cloud', 'Cloud')
	)

etat_choices = (
	('active', 'Activé'),
	('nonactive', 'Pas encore activé')
	)



class Formation(models.Model):
	title = models.CharField(max_length=150)
	category = models.CharField(
		max_length=150,
		choices = category_choices)
	etat = models.CharField(
		max_length=150,
		choices = etat_choices )
	logo = models.ImageField(null=True, blank=True)
	description = models.TextField(max_length=1000)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("formation_detail", kwargs={
        "pk": self.id
    })
    	
   
