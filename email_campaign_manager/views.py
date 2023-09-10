from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber, Campaign
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
from datetime import date
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string, get_template

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')

        Subscriber.objects.create(email=email, first_name=first_name)

        return HttpResponse("Subscribed")

@csrf_exempt
def unsubscribe(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            subscriber = Subscriber.objects.get(email=email)
            subscriber.is_active = False 
            subscriber.save()
            return HttpResponse("Unsubscribed")
        except Subscriber.DoesNotExist:
            return HttpResponse("Subscriber does not exist")

@csrf_exempt
def send_campaign_email(campaign, subscriber):
    recipients = [subscriber]

    # Mailgun SMTP configuration
    smtp_server = 'smtp.mailgun.org'
    smtp_port = 587
    smtp_username = settings.SMTP_USERNAME
    smtp_password = settings.SMTP_PASSWORD


    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)

            for recipient in recipients:
                msg = MIMEMultipart()
                msg['From'] = 'supratikchakraborty1@gmail.com'  # Replace with your email address
                msg['To'] = recipient.email
                msg['Subject'] = campaign.subject

                text_content = campaign.plain_text_content
                # html_content = campaign.html_content

                html_content = render_to_string("email_campaign.html", 
                {
                    "preview_text": campaign.preview_text,
                    "article_url": campaign.article_url,
                    "html_content": campaign.html_content
                })

                msg.attach(MIMEText(text_content, 'plain'))
                msg.attach(MIMEText(html_content, 'html'))

                # print(msg.as_string())

                server.sendmail(smtp_username, recipient.email, msg.as_string())
                print(f"Email sent to {recipient.email}")

    except Exception as e:
        print(f"Email sending failed: {str(e)}")

@csrf_exempt
def send_campaign_emails_parallel(request):

    if request.method == 'POST':

        try:

            campaign = Campaign.objects.create(published_date=date.today().strftime('%Y-%m-%d'))
            # campaign = Campaign.objects.get(published_date=date.today().strftime('%Y-%m-%d'))

            # Get a list of active subscribers
            recipients = Subscriber.objects.filter(is_active=True)

            # Number of threads for parallelization
            num_threads = 5  # Adjust as needed

            # Send emails in parallel
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                for subscriber in recipients:
                    executor.submit(send_campaign_email, campaign, subscriber)

            return HttpResponse("Emails dispatched")

        except Exception:
            return HttpResponse("Exception: ", str(Exception))