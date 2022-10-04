# Generated by Django 4.1.1 on 2022-10-04 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_transaction_credited_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='credited_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_transactions', to='main_app.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debited_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_transactions', to='main_app.account'),
        ),
    ]
