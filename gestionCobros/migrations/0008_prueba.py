# Generated by Django 3.0.8 on 2020-08-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionCobros', '0007_auto_20200801_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id_prueba', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': 'PruebaHub',
            },
        ),
    ]