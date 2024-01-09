# Generated by Django 3.2.7 on 2023-07-13 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=150)),
                ('N', models.CharField(max_length=200)),
                ('P', models.CharField(max_length=150)),
                ('K', models.CharField(max_length=150)),
                ('temperature', models.CharField(max_length=150)),
                ('humidity', models.CharField(max_length=150)),
                ('ph', models.CharField(max_length=150)),
                ('rainfall', models.CharField(max_length=150)),
                ('result', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ftlzr_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=150)),
                ('N', models.CharField(max_length=200)),
                ('P', models.CharField(max_length=150)),
                ('K', models.CharField(max_length=150)),
                ('crop_type', models.CharField(max_length=150)),
                ('result', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='plant_disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=150)),
                ('file', models.FileField(max_length=200, upload_to='')),
                ('label', models.CharField(max_length=250)),
                ('remedies', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('crop_type', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=100)),
                ('pr_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('cardtype', models.CharField(max_length=100)),
                ('cardname', models.CharField(max_length=100)),
                ('cardnumber', models.CharField(max_length=100)),
                ('cvv', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='reg_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
