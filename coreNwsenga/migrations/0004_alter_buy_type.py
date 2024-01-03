# Generated by Django 5.0 on 2023-12-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreNwsenga', '0003_buy_date_buy_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='type',
            field=models.CharField(choices=[('pswla', 'پسولە'), ('xanu', 'خانوو'), ('bax', 'باخ'), ('zawi', 'زەوی')], default='pswla', max_length=20, verbose_name='جۆری کڕین'),
        ),
    ]
