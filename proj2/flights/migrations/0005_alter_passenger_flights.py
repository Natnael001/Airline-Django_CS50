# Generated by Django 5.0.2 on 2024-02-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_rename_passanger_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight'),
        ),
    ]
