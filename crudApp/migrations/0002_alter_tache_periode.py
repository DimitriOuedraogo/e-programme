# Generated by Django 5.1.7 on 2025-04-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='periode',
            field=models.CharField(choices=[('6h-7h30', '6h-7h30'), ('8h30-16h30', '8h30-16h30'), ('17h-20h', '17h-20h'), ('19h-21h', '19h-21h'), ('20h-22h', '20h-22h')], max_length=50),
        ),
    ]
