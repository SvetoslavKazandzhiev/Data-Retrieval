import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

project_folder = os.path.expanduser('django-scrapy-integration-main/djscrapyquotes/djscrapyquotes')
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djscrapyquotes.settings')

application = get_wsgi_application()
