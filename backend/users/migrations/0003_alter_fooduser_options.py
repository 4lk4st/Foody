# Generated by Django 4.2.4 on 2023-08-26 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_fooduser_first_name_alter_fooduser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fooduser',
            options={'ordering': ['-id']},
        ),
    ]