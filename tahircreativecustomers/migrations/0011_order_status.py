# Generated by Django 3.1.1 on 2022-02-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahircreativecustomers', '0010_order_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
