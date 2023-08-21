# Generated by Django 4.0 on 2023-08-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('img', models.BinaryField()),
                ('is_active', models.BooleanField(null=True)),
            ],
        ),
    ]