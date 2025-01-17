# Generated by Django 4.1.5 on 2023-01-17 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0003_auto_20220117_0952"),
        ("zerowaste", "0004_auto_20221108_1347"),
    ]

    operations = [
        migrations.CreateModel(
            name="P122Buildings8Nov22",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fid", models.CharField(blank=True, max_length=100, null=True)),
                ("sac_number", models.CharField(blank=True, max_length=100, null=True)),
                ("wing_name", models.CharField(blank=True, max_length=100, null=True)),
                ("num_flat", models.CharField(blank=True, max_length=100, null=True)),
                ("num_shops", models.CharField(blank=True, max_length=100, null=True)),
                ("num_floors", models.CharField(blank=True, max_length=100, null=True)),
                ("building_n", models.CharField(blank=True, max_length=100, null=True)),
                ("building_t", models.CharField(blank=True, max_length=100, null=True)),
                ("prabhag_no", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "ward_name_field",
                    models.CharField(
                        blank=True, db_column="ward_name_", max_length=100, null=True
                    ),
                ),
                ("prop_add", models.CharField(blank=True, max_length=100, null=True)),
                ("cluster", models.CharField(blank=True, max_length=100, null=True)),
                ("clust_nm", models.CharField(blank=True, max_length=100, null=True)),
                ("population", models.CharField(blank=True, max_length=100, null=True)),
                ("bin_photo", models.CharField(blank=True, max_length=100, null=True)),
                ("username", models.CharField(blank=True, max_length=100, null=True)),
                ("date_time", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "qfield_username",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "db_table": "p122_buildings_8Nov22",
                "managed": False,
            },
        ),
        migrations.AlterField(
            model_name="employeedetails",
            name="ward",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="humanresourcedata",
            name="ward",
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name="compost_data",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prabhag_no", models.CharField(blank=True, max_length=254, null=True)),
                ("sac_no", models.CharField(blank=True, max_length=254, null=True)),
                ("road_name", models.CharField(blank=True, max_length=254, null=True)),
                (
                    "building_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "compost_weight",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "testing_done",
                    models.CharField(
                        blank=True,
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "compost_quality",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Good", "Good"),
                            ("Average", "Average"),
                            ("Poor", "Poor"),
                        ],
                        default="Average",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("coll_date", models.DateField(blank=True, null=True)),
                (
                    "ward",
                    models.ForeignKey(
                        blank=True,
                        default=0,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="map.mumbaiwardboundary2jan2022",
                        to_field="ward_id",
                    ),
                ),
            ],
            options={
                "db_table": "compost_data",
                "managed": True,
            },
        ),
    ]
