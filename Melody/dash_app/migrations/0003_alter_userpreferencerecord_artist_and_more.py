# Generated by Django 4.1.3 on 2022-12-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_app', '0002_userpreferencerecord_remove_favoritegenres_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferencerecord',
            name='artist',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='userpreferencerecord',
            name='song',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
