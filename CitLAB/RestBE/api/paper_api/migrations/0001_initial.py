# Generated by Django 3.0.6 on 2020-06-09 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('abstract', models.TextField(null=True)),
                ('type_paper', models.CharField(blank=True, max_length=200, null=True)),
                ('isbn', models.CharField(max_length=200, null=True)),
                ('issn', models.CharField(max_length=200, null=True)),
                ('publishing_company', models.CharField(max_length=200, null=True)),
                ('doi', models.CharField(max_length=200, null=True)),
                ('pages', models.IntegerField(null=True)),
                ('site', models.URLField(null=True)),
                ('created_on', models.DateField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('n_citation', models.IntegerField(default=0)),
                ('n_version', models.IntegerField(default=1)),
                ('rating', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('eprint', models.URLField(null=True)),
                ('pdf', models.URLField(null=True)),
                ('picture', models.URLField(null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('writers', models.CharField(blank=True, max_length=200, null=True)),
                ('have_category', models.ManyToManyField(to='category_api.Category')),
                ('mentioned_in', models.ManyToManyField(related_name='_paper_mentioned_in_+', to='paper_api.Paper')),
                ('owns_version', models.ManyToManyField(related_name='_paper_owns_version_+', to='paper_api.Paper')),
            ],
            options={
                'db_table': 'paper',
            },
        ),
    ]
