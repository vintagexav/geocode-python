# ran with FLASK_APP=src/main.py FLASK_ENV=development flask run --port 8080
from .setup import setup
app = setup('config/dev.cfg')
