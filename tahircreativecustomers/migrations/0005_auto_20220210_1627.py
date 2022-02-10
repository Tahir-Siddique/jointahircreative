# Generated by Django 3.1.1 on 2022-02-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahircreativecustomers', '0004_auto_20220210_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='options',
            field=models.ManyToManyField(blank=True, null=True, to='tahircreativecustomers.Options'),
        ),
    ]
