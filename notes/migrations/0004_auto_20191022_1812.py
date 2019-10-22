# Generated by Django 2.2.6 on 2019-10-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_delete_onenote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]