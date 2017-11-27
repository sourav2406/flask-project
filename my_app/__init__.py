from flask import Flask
import my_app.config

app = Flask(__name__)
app.config.from_object('my_app.config.DevelopmentConfig')

import my_app.view
