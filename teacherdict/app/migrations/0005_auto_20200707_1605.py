# Generated by Django 3.0.8 on 2020-07-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200707_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profil_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
