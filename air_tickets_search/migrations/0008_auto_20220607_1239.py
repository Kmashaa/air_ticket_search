# Generated by Django 3.2.13 on 2022-06-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_tickets_search', '0007_auto_20220607_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights_bought',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('aviacompany', models.CharField(max_length=50)),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]