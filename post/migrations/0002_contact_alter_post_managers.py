# Generated by Django 4.0.6 on 2022-07-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('subject', models.CharField(max_length=256)),
                ('text_box', models.TextField(max_length=2048)),
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
    ]
