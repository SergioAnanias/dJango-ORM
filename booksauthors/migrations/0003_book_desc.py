# Generated by Django 3.2.4 on 2021-06-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksauthors', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
