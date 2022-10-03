# Generated by Django 4.1.1 on 2022-10-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=250)),
                ('logo', models.URLField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['institution_id'],
            },
        ),
    ]