from django.core.management.base import BaseCommand
from crudApp.models import JourSemaine

class Command(BaseCommand):
    help = "Initialiser les jours de la semaine"

    def handle(self, *args, **kwargs):
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        for jour in jours:
            JourSemaine.objects.get_or_create(nom=jour)
        self.stdout.write(self.style.SUCCESS("Jours de la semaine ajoutés avec succès !"))
