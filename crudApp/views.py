from django.shortcuts import render
from .models import JourSemaine, Tache
from .forms import TacheForm
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.http import HttpResponse

def creer_tache(request):
    if request.method == "POST":
        form = TacheForm(request.POST)
        jour_nom = request.POST.get("jour_nom")
        if form.is_valid():
            jour = JourSemaine.objects.get(nom=jour_nom)
            if jour:
                tache = form.save(commit=False)
                tache.jour = jour
                tache.save()
                form = TacheForm()
                success_message = "Tâche créée avec succès !"
            return render(request, "tache.html", {"form": form, "success": success_message})
        else:
            return render(request, "tache.html", {"form": form, "error": "Il y a une erreur dans le formulaire."})

    else:
        form = TacheForm()
    return render(request, "tache.html", {"form": form})


def generer_programme(request):
    periodes = ["6h-7h30", "8h30-16h30",'17h-20h', "19h-21h", "20h-22h"]
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    programme = defaultdict(lambda: defaultdict(list))
    taches = Tache.objects.all()

    # Organiser les tâches par jour et période
    for tache in taches:
        jour = tache.jour.nom
        print(jour)
        periode = tache.periode
        print(periode)
        programme[periode][jour].append(tache.nom)
        print( programme)

   # Image settings
    cell_width = 150
    cell_height = 100
    space_x = 50
    space_y = 40
    largeur = cell_width * (len(jours) + 1)
    hauteur = cell_height * (len(periodes) + 1)
    image = Image.new("RGB", (largeur , hauteur ), "white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
        header_font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default(size=20)
        header_font = ImageFont.load_default(size=20)

    # Entête des jours (colonnes)
    for j, jour in enumerate(jours):
        x = space_x + (j + 0.8) * cell_width
        y = space_y-35
        draw.rectangle([x, y, x + cell_width, y + cell_height-45], fill="#E1F5FE", outline="black")
        draw.text((x + 10, 10), jour, fill="black", font=font)

    # Entête des périodes (lignes)
    for i, periode in enumerate(periodes):
        y = space_y + (i ) * cell_height
        draw.rectangle([space_x-50, y+20, space_x + cell_width-30, y+20 + cell_height], fill="#B3E5FC", outline="black")
        draw.text((10, y + 30), periode, fill="black", font=font)

    # Remplir le tableau avec les tâches
    for i, periode in enumerate(periodes):
        for j, jour in enumerate(jours):
            taches = programme.get(periode, {}).get(jour, [])
            texte = "\n".join(taches)
            x = space_x + (j + 0.8) * cell_width
            y = space_y + (i + 0.2) * cell_height
            draw.rectangle([x, y, x + cell_width, y + cell_height], outline="black")
            draw.text((x + 5, y + 5), texte, fill="black", font=font)

    # Envoyer l'image comme réponse HTTP
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    Tache.objects.all().delete()
    return HttpResponse(buffer.getvalue(), content_type="image/png")
