# Generated by Django 3.2.9 on 2021-11-30 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetsParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=256)),
                ('clock', models.IntegerField(blank=True, null=True)),
                ('params', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.widgetsparam')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=80)),
                ('widgets', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.widgets')),
            ],
        ),
    ]