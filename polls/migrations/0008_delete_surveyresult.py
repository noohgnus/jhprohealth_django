# Generated by Django 2.0.3 on 2018-06-12 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_surveycompactresult'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SurveyResult',
        ),
    ]
