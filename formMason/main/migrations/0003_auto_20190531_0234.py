# Generated by Django 2.2 on 2019-05-31 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_formresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formresponse',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FormSchema'),
        ),
    ]
