# Generated by Django 4.1.7 on 2023-03-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_userrelations_userbookrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.SmallIntegerField(choices=[(1, 'OK'), (2, 'Fine'), (3, 'Good'), (4, 'Amaizing'), (5, 'Incredible')], null=True),
        ),
    ]