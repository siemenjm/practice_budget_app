# Generated by Django 4.1.2 on 2022-10-06 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_institution_user_transaction_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['description']},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='account_id',
            new_name='account_identification',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='institution_id',
            new_name='institution_identification',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_id',
            new_name='transaction_identification',
        ),
    ]
