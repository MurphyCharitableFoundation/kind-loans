# Generated by Django 3.2.25 on 2024-09-14 06:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('core', '0002_rename_is_admin_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='business_category',
            field=models.CharField(blank=True, help_text="The category of the user's business, if applicable.", max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='business_name',
            field=models.CharField(blank=True, help_text="The name of the user's business, if applicable.", max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, help_text='The city where the user is located.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, help_text='The country where the user is located.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.country'),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='The date and time when the user was created.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.TextField(blank=True, help_text='The interests of the user.'),
        ),
        migrations.AddField(
            model_name='user',
            name='photoURL',
            field=models.URLField(blank=True, help_text="The URL of the user's photo."),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('lender', 'Lender'), ('borrower', 'Borrower'), ('admin', 'Admin')], default='borrower', help_text='The role of the user in the system.', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='story',
            field=models.TextField(blank=True, help_text='The personal story of the user.'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='The date and time when the user was last updated.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='The email address of the user.', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='The full name of the user.', max_length=255),
        ),
    ]