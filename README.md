# Flask example for PKG Deploy


RPM builds with:
* Python3.6 / pip
* Flask
* Gunicorn
* Nginx
* Systemd


_Note: This is just an example. The settings, requirements, layout etc are
not done using best practices and are not production ready._


## Local setup
```
python3.6 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

FLASK_APP=app.py flask run --host 0.0.0.0:5000
```
