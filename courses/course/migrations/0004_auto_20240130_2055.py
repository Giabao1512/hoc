# Generated by Django 3.2.23 on 2024-01-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='lessons/%Y/%m'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='lessons/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('subject', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subject', 'course')},
        ),
    ]
