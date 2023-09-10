# campaigns/models.py
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Campaign(models.Model):
    subject = models.CharField(max_length=200, default="Email Campaign Subject")
    preview_text = models.CharField(max_length=200, default="Campaign Preview")
    article_url = models.URLField(default="www.example.com")
    html_content = models.TextField(default="<p>HTML Content</p>")
    plain_text_content = models.TextField(default="Plain text")
    published_date = models.DateField()
