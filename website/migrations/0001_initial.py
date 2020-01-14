# Generated by Django 3.0.2 on 2020-01-14 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('bio', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('url_link', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(default='now', on_delete=django.db.models.deletion.CASCADE, to='website.Profile')),
            ],
        ),
    ]