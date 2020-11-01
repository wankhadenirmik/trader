# Generated by Django 3.1.2 on 2020-10-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('age', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
