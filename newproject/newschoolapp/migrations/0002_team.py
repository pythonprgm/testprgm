# Generated by Django 3.2.10 on 2022-01-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newschoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
            ],
        ),
    ]
