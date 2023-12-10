cd ~/equity2
source venv/bin/activate
cd ~/equity2/dashboard
gunicorn --config gunicorn_config.py