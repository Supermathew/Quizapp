# Generated by Django 4.1.4 on 2022-12-26 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0008_userattempt'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmitted',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quizcategory'),
            preserve_default=False,
        ),
    ]
