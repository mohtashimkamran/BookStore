# Generated by Django 4.0.5 on 2022-06-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_listed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='listed_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]