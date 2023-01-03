# Generated by Django 4.1.2 on 2022-12-08 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("packagedb", "0052_package_index_error_package_last_indexed_date"),
        ("matchcode", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="approximatedirectorycontentindex",
            name="package",
            field=models.ForeignKey(
                help_text="The Package that this directory is a part of",
                on_delete=django.db.models.deletion.CASCADE,
                to="packagedb.package",
            ),
        ),
        migrations.AlterField(
            model_name="approximatedirectorystructureindex",
            name="package",
            field=models.ForeignKey(
                help_text="The Package that this directory is a part of",
                on_delete=django.db.models.deletion.CASCADE,
                to="packagedb.package",
            ),
        ),
        migrations.AlterField(
            model_name="exactfileindex",
            name="package",
            field=models.ForeignKey(
                help_text="The Package that this file is from",
                on_delete=django.db.models.deletion.CASCADE,
                to="packagedb.package",
            ),
        ),
        migrations.AlterField(
            model_name="exactpackagearchiveindex",
            name="package",
            field=models.ForeignKey(
                help_text="The Package that this file is from",
                on_delete=django.db.models.deletion.CASCADE,
                to="packagedb.package",
            ),
        ),
        migrations.DeleteModel(
            name="IndexablePackage",
        ),
    ]
