# Generated by Django 3.1.1 on 2022-02-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahircreativecustomers', '0005_auto_20220210_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='included',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]