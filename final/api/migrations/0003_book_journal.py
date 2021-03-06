# Generated by Django 3.2 on 2022-05-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('type', models.CharField(choices=[('B', 'Bullet'), ('F', 'Food'), ('T', 'Travel'), ('S', 'Sport')], default='B', max_length=128)),
                ('publisher', models.CharField(max_length=123)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
