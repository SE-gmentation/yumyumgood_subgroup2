# Generated by Django 3.2.2 on 2021-05-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_menu_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.CharField(choices=[('판매 가능', '판매 가능'), ('판매 중지', '판매 중지')], default='판매 가능', max_length=20),
        ),
    ]
