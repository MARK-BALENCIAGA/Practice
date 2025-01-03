from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_userpassword_date_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpassword',
            name='application_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='game_developer',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='game_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='website_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='website_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
