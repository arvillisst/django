# Generated by Django 2.2.1 on 2019-06-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20190523_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP строка')),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='ip_like',
            field=models.ManyToManyField(blank=True, to='tutorials.IpUser', verbose_name='Кто лайкнул (IP)'),
        ),
    ]
