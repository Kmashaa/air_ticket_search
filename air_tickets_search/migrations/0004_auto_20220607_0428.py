# Generated by Django 3.2.13 on 2022-06-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_tickets_search', '0003_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aviacompany', models.CharField(max_length=50)),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('departure_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('total_number_of_seats', models.IntegerField()),
                ('reserved_number_of_seats', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
