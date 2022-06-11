# Generated by Django 4.0.5 on 2022-06-10 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=10)),
                ('makeYear', models.CharField(max_length=10)),
                ('registrationNo', models.CharField(max_length=100)),
                ('horsePower', models.CharField(max_length=20)),
                ('carCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carcategories')),
            ],
        ),
    ]