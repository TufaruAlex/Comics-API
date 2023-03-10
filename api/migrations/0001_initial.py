# Generated by Django 4.1.7 on 2023-03-05 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisherName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comicName', models.CharField(max_length=100, unique=True)),
                ('writer', models.CharField(default='null', max_length=100)),
                ('issuesNumber', models.IntegerField(default=0)),
                ('beginDate', models.DateField(default='00-00-0000')),
                ('endDate', models.DateField(default='00-00-0000')),
                ('comicPublisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.publisher')),
            ],
        ),
    ]
