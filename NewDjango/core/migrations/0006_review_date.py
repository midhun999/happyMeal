# Generated by Django 2.2.10 on 2020-07-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
