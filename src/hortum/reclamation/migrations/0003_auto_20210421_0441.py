# Generated by Django 3.1.7 on 2021-04-21 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamation', '0002_auto_20210420_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamation',
            name='description',
            field=models.CharField(max_length=450),
        ),
    ]
