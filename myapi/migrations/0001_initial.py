# Generated by Django 3.2.7 on 2021-09-03 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_PK', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('price', models.FloatField(max_length=25)),
                ('stock', models.IntegerField(max_length=25)),
            ],
        ),
    ]
