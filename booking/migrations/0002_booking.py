# Generated by Django 4.2.11 on 2024-03-14 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('number', models.IntegerField()),
                ('notes', models.TextField()),
                ('signup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='booking.signup')),
            ],
        ),
    ]
