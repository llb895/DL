# Generated by Django 2.2.5 on 2021-07-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('comments', models.CharField(max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
