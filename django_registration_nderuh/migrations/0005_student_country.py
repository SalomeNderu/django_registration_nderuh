# Generated by Django 4.1.7 on 2023-03-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_registration_nderuh', '0004_student_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
