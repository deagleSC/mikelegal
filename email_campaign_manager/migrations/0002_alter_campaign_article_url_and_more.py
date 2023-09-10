# Generated by Django 4.2.5 on 2023-09-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_campaign_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="article_url",
            field=models.URLField(default="www.example.com"),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="html_content",
            field=models.TextField(default="<p>HTML Content</p>"),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="plain_text_content",
            field=models.TextField(default="Plain text"),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="preview_text",
            field=models.CharField(default="Campaign Preview", max_length=200),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="subject",
            field=models.CharField(default="Email Campaign Subject", max_length=200),
        ),
    ]