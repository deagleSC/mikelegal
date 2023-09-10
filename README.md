# mikelegal

### Clone the repository
```
git clone https://github.com/deagleSC/mikelegal.git
```

### Create a virtual environment
```
virtualenv venv
```

### Activate virtual environment
(Windows)
```
venv\Scripts\activate
```

(Mac/Linux)
```
source bin/activate
```

### Install dependancies
```
pip install -r requirements.txt
```

### Add Mailgun Sandbox credentials

Go to temp/settings.py and edit the following:
```
SMTP_USERNAME = ''
SMTP_PASSWORD = ''
```

### Start server
```
python manage.py runserver
```
