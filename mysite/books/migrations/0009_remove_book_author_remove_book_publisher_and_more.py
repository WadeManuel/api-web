# Generated by Django 5.0.6 on 2025-01-28 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_task_created_alter_task_datecompleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
