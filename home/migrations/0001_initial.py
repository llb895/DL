# Generated by Django 2.2.5 on 2021-08-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DANQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output', models.CharField(max_length=600)),
                ('hn', models.CharField(max_length=600)),
                ('cn', models.CharField(max_length=600)),
            ],
        ),
    ]