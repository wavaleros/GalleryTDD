# Generated by Django 2.1.15 on 2020-03-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), to='gallery.PortfolioCollection'),
        ),
    ]
