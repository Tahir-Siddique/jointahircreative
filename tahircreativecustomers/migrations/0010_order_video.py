# Generated by Django 3.1.1 on 2022-02-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahircreativecustomers', '0009_order_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='video',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
    ]
