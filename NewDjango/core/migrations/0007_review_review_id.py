# Generated by Django 2.2.10 on 2020-07-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_id',
            field=models.IntegerField(default=0),
        ),
    ]
