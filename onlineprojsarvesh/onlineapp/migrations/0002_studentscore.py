# Generated by Django 2.1 on 2018-10-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Score', models.CharField(max_length=25)),
            ],
        ),
    ]
