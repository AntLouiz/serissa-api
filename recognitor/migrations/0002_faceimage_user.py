# Generated by Django 3.0.3 on 2020-03-20 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('recognitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faceimage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
            preserve_default=False,
        ),
    ]
