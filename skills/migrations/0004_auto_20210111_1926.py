# Generated by Django 3.1.4 on 2021-01-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_others'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HardSkills',
            new_name='HardSkill',
        ),
        migrations.RenameModel(
            old_name='Others',
            new_name='Other',
        ),
        migrations.RenameModel(
            old_name='SoftSkills',
            new_name='SoftSkill',
        ),
    ]
