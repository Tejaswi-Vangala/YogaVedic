# Generated by Django 4.1.1 on 2023-01-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_asana_asanas_asana1_asanas_asana2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asanas',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='asanas',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='asanas',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
