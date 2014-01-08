import os
from django.conf import settings  # import the settings file
from pipeline.jinja2 import ext
project_path = settings.PROJECT_DIR

def static_settings(context):
    session_timeout = settings.SESSION_COOKIE_AGE * 1000
    return {'YUI_URL': settings.YUI_URL, 'SESSION_TIMEOUT': session_timeout,
            'compressed_css': ext.compressed_css,
            'compressed_js': ext.compressed_js}
