# Generated by Django 4.2.7 on 2024-07-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addusermodel',
            fields=[
                ('uid', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
