# Generated by Django 4.0.3 on 2022-04-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blog_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cust_id',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
