# Generated by Django 3.2.4 on 2021-06-14 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojosninjas', '0008_alter_ninja_dojo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ninjas', to='dojosninjas.dojo'),
        ),
    ]