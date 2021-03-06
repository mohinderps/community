# Generated by Django 2.0.7 on 2018-09-14 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0002_auto_20180914_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_uploads', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_uploads', to='institution.Institution'),
        ),
    ]
