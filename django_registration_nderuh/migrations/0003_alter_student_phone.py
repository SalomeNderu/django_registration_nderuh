# Generated by Django 4.1.7 on 2023-03-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_registration_nderuh', '0002_student_phone_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=254),
        ),
    ]
