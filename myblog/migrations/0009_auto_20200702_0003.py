# Generated by Django 3.0.7 on 2020-07-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(default='Click the link to read the content!', max_length=255),
        ),
    ]
