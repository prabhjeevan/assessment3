# Generated by Django 3.1.1 on 2020-11-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('time', models.IntegerField()),
                ('person', models.CharField(max_length=200)),
            ],
        ),
    ]
