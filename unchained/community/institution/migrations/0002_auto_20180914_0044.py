# Generated by Django 2.0.7 on 2018-09-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]