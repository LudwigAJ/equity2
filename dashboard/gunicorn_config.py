import multiprocessing
import os

# how many workers
workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))
# how many threads
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
# how long until timeout
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
# address to bind to
bind = os.environ.get('GUNICORN_BIND', '158.220.82.151:80')
#
forwarded_allow_ips = '*'
#
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
#
wsgi_app = 'app:server'
#
accesslog = '-'
#
loglevel = 'info'