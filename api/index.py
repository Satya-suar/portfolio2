#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')

# Get WSGI application
application = get_wsgi_application()
