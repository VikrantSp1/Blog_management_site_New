# Generated by Django 4.0.5 on 2022-07-05 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_remove_post_sec_head_alter_post_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_details',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_data', to='website.post'),
        ),
    ]
