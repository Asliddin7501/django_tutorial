# Generated by Django 3.2 on 2021-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi_tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
