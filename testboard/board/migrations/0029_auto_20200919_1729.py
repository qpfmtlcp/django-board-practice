# Generated by Django 2.2.16 on 2020-09-19 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0028_auto_20200919_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='board.Board'),
        ),
    ]
