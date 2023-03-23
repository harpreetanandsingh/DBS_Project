# Generated by Django 4.1.7 on 2023-03-23 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("add_id", models.AutoField(primary_key=True, serialize=False)),
                ("city", models.CharField(max_length=255)),
                ("street", models.CharField(max_length=255)),
                ("zipcode", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Authenticate",
            fields=[
                ("p_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("f_name", models.CharField(max_length=255)),
                ("l_name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="deliveryPersonnel",
            fields=[
                ("personnel_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Items",
            fields=[
                ("item_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                ("restaurant_id", models.AutoField(primary_key=True, serialize=False)),
                ("restaurant_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                ("status_id", models.AutoField(primary_key=True, serialize=False)),
                ("status_val", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("del_rev", models.CharField(max_length=255)),
                ("food_rev", models.CharField(max_length=255)),
                ("stars", models.IntegerField()),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="restPhNos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ph_no", models.IntegerField()),
                (
                    "restaurant_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.restaurant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RestAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "add_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.address",
                    ),
                ),
                (
                    "restaurant_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.restaurant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="personnelAddr",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "add_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.address",
                    ),
                ),
                (
                    "personnel_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.deliverypersonnel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="orders",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("total_price", models.IntegerField()),
                ("ordered_on", models.DateTimeField(auto_now=True)),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.customer",
                    ),
                ),
                (
                    "restaurant_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.restaurant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="orderItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "item_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.items",
                    ),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.orders",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustNos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ph_no", models.IntegerField()),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "add_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.address",
                    ),
                ),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food_delivery_app.customer",
                    ),
                ),
            ],
        ),
    ]
