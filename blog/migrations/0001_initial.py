# Generated by Django 4.1.3 on 2022-12-11 12:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email_address", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("captions", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("excerpt", models.CharField(max_length=200)),
                ("image_name", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now=True)),
                ("slug", models.SlugField(unique=True)),
                ("content", models.TextField(validators=[django.core.validators.MinLengthValidator(25)])),
                (
                    "author",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="posts", to="blog.author"
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
        ),
    ]
