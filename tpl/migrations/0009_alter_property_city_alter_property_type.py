# Generated by Django 4.1.2 on 2023-05-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpl', '0008_alter_property_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(choices=[('tirana-albania', 'Tirana'), ('brno-czech_republic', 'Brno'), ('prague-czech_republic', 'Prague'), ('undefined', 'Undefined')], default='undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('room', 'Room'), ('residence', 'Residence'), ('flat', 'Flat')], default='room', max_length=9),
        ),
    ]
