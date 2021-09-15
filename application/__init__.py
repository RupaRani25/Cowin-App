from flask import Flask, app
app = Flask(__name__)

from application import routes
