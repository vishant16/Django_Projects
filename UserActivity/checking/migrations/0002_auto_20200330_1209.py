# Generated by Django 3.0.4 on 2020-03-30 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(default='start_time', help_text='Feb 1 2020  1:33PM', max_length=120)),
                ('end_time', models.CharField(default='end_time', help_text='Feb 1 2020  1:33PM', max_length=120)),
                ('start_time1', models.CharField(default='start time', help_text='Feb 1 2020  1:33PM', max_length=120, verbose_name='start time')),
                ('end_time1', models.CharField(default='end time', help_text='Feb 1 2020  1:33PM', max_length=120, verbose_name='end time')),
                ('start_time2', models.CharField(default='start time', help_text='Feb 1 2020  1:33PM', max_length=120, verbose_name='start time')),
                ('end_time2', models.CharField(default='end time', help_text='Feb 1 2020  1:33PM', max_length=120, verbose_name='end time')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(default='vishant', max_length=10)),
                ('tz', models.CharField(default='India', max_length=10)),
                ('activity_periods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checking.SE')),
            ],
        ),
        migrations.RemoveField(
            model_name='bookdetails',
            name='addons',
        ),
        migrations.DeleteModel(
            name='Addons',
        ),
        migrations.DeleteModel(
            name='BookDetails',
        ),
    ]
