# Generated by Django 2.0.3 on 2018-06-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_delete_surveyresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
