# Generated by Django 4.2.4 on 2023-09-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_favoriterecipe_recipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-pk']},
        ),
    ]
