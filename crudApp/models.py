from django.db import models

class JourSemaine(models.Model):
    nom = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nom

class Tache(models.Model):
    nom = models.CharField(max_length=255)
    PERIODE_CHOICES = [
        ('6h-7h30', '6h-7h30'),
        ('8h30-16h30', '8h30-16h30'),
        ('17h-20h', '17h-20h'),
        ('19h-21h', '19h-21h'),
        ('20h-22h', '20h-22h'),
    ]
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES)
    jour = models.ForeignKey(JourSemaine, on_delete=models.CASCADE, related_name="taches")

    def __str__(self):
        return f"{self.nom} ({self.periode} )"
