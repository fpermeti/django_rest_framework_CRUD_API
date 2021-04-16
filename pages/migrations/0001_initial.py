# Generated by Django 3.2 on 2021-04-16 20:52

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('price', models.FloatField(validators=[pages.models.min_max_range])),
            ],
        ),
    ]
