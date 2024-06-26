# Generated by Django 4.2.11 on 2024-06-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('tags', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]
