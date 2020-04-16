# Generated by Django 3.0.4 on 2020-03-29 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Thriller', 'Thriller'), ('Documentary', 'Documentary'), ('Romantic', 'Romantic'), ('Short Film', 'Short Film'), ('Action', 'Action')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('bingeinterest', models.CharField(choices=[('Very Likely', 'Very Likely'), ('Likely', 'Likely'), ('Maybe', 'Maybe')], max_length=50, null=True)),
                ('streamService', models.CharField(choices=[('Netflix', 'Netflix'), ('Prime Video', 'Prime Video'), ('Hotstar', 'Hotstar'), ('Voot', 'Voot'), ('Disney+', 'Disney+'), ('Zee 5', 'Zee 5'), ('Other', 'Other')], max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer')),
                ('tag', models.ManyToManyField(to='accounts.Tag')),
            ],
        ),
    ]
