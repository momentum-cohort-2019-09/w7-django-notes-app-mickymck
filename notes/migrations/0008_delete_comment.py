# Generated by Django 2.2.6 on 2019-10-24 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
