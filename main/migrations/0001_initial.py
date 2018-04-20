# Generated by Django 2.0.4 on 2018-04-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('civilid', models.IntegerField()),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('work_tel', models.IntegerField()),
                ('home_tel', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('notes', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]