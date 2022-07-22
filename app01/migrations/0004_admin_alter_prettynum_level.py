# Generated by Django 4.0.5 on 2022-07-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_userinfo_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.IntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级')], default=1, verbose_name='级别'),
        ),
    ]