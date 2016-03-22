import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##################
# configurations #
##################

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from sil_fhir_server.data_types.complex import (
    complex_dt, period, quantity, address, age, annotation, attachment,
    codeableconcept, coding, contactpoint, count, distance, duration,
    humanname, identifier, money, period, range, ratio,
    sampleddata, signature, timing

)
# from sil_fhir_server import test

###########
# helpers #
###########


##########
# routes #
##########

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
