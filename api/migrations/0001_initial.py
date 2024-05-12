# Generated by Django 3.2.11 on 2024-05-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('colour', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
