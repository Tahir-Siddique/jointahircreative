# Generated by Django 3.1.1 on 2022-02-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahircreativecustomers', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
