# Generated by Django 2.0.10 on 2019-03-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190227_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='GPA',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='faculty',
            field=models.IntegerField(choices=[(1, 'Faculty of Engineering'), (2, 'Faculty of Law'), (3, 'Faculty of Education')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linked_in',
            field=models.URLField(null=True),
        ),
    ]
