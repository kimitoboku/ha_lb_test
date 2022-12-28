import time

from socket import gethostname
from flask import Flask

app = Flask(__name__)
i = 0
def get_hit_count():
    global i
    i = i + 1
    return i

@app.route('/')
def hello():
    count = get_hit_count()
    hostname = gethostname()
    return '{} times in {}.\n'.format(count, hostname)
