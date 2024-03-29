# Generated by Django 4.0.5 on 2022-07-19 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('message', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
    ]
