# Generated by Django 3.2.25 on 2024-11-04 04:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20241018_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanprofile',
            name='deadline_to_receive_loan',
            field=models.DateField(default=datetime.datetime(2025, 11, 4, 4, 4, 41, 74704, tzinfo=utc), help_text='The deadline to receive the loan.'),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
