# Generated by Django 3.2.4 on 2021-06-17 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.note'),
        ),
    ]