# Generated by Django 5.0.4 on 2024-05-06 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newspaper", "0003_alter_newspaper_publishers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newspaper",
            old_name="context",
            new_name="content",
        ),
    ]