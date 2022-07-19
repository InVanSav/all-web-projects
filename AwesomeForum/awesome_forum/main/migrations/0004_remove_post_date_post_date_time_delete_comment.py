# Generated by Django 4.0.4 on 2022-05-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]