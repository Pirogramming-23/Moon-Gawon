# Generated by Django 5.2.4 on 2025-07-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_actor_review_running_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='actor',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='review',
            name='running_time',
            field=models.PositiveIntegerField(),
        ),
    ]
