# Generated by Django 4.2.6 on 2023-11-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_carusellanding_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carusellanding',
            name='image_title',
            field=models.ImageField(blank=True, upload_to='Carrusel', verbose_name='Imagen de titulo'),
        ),
    ]
