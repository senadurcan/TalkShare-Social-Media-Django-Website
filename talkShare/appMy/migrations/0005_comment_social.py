# Generated by Django 4.1.3 on 2023-03-28 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_comment_date_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.social', verbose_name='Sosyal'),
        ),
    ]
