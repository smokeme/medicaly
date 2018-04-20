# Generated by Django 2.0.4 on 2018-04-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180416_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='visit',
            name='billables',
            field=models.ManyToManyField(to='main.Billable'),
        ),
    ]
