# Generated by Django 4.1.1 on 2023-01-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_user_det_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_det',
            name='age',
            field=models.IntegerField(),
        ),
    ]
