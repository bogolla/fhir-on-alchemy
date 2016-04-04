import os

from flask import request
from flask.ext.api import FlaskAPI
from flask.ext.sqlalchemy import SQLAlchemy

##################
# configurations #
##################
from sqlalchemy import create_engine

from sil_fhir_server.data_types.complex.pg_composite import register_composites

app = FlaskAPI(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

e = create_engine(os.environ['DATABASE_URL'])
connection = e.connect()
# api = FlaskAPI(app)

from  sil_fhir_server import test

from sil_fhir_server.data_types.complex import (
    complex_dt, period, quantity, address, age, annotation, attachment,
    codeableconcept, coding, contactpoint, count, distance, duration,
    humanname, identifier, money, period, range, ratio,
    sampleddata, signature, timing
)

from sil_fhir_server.models import (
    element, elementdefinition, meta, resource, extension, domainresource, backboneelement,
    narrative, account, appointment, appointmentresponse, auditevent, basic,
    binary, bodysite, bundle, careplan, claim, claimresponse,
    clinicalimpression, communication, communicationrequest,
    composition, conceptmap, condition, conformance, contract,
    coverage, dataelement, detectedissue, device, devicecomponent,
    devicemetric, deviceuserequest, deviceusestatement,
    diagnosticorder, diagnosticreport, documentmanifest,
    documentreference, eligibilityrequest, eligibilityresponse,
    encounter, enrollmentrequest, enrollmentresponse, episodeofcare,
    explanationofbenefit, flag, goal, group, healthcareservice,
    imagingobjectselection, imagingstudy, immunization,
    immunizationrecommendation, list, location, media, medication,
    medicationadministration, medicationdispense, namingsystem,
    nutritionorder, observation, operationdefinition,
    operationoutcome, order, orderresponse, organization,
    patient, paymentnotice, person, practitioner, procedure,
    procedurerequest, processrequest, processresponse, provenance,
    reference, referralrequest, relatedperson, riskassessment,
    schedule, slot, specimen, structuredefinition, subscription, substance,
    supplydelivery, supplyrequest, valueset, visionprescription
)

register_composites(connection)
###########
# helpers #
###########


##########
# routes #
##########

@app.route('/')
def hello():
    return "Hello World!"
#
#
# @app.route("/patients", methods=['GET', 'POST'])
# def patients_list():
#     """
#     List or create notes.
#     """
#     if request.method == 'POST':
#         note = str(request.data.get('text', ''))
#         idx = max(notes.keys()) + 1
#         notes[idx] = note
#         return note_repr(idx), status.HTTP_201_CREATED
#
#     # request.method == 'GET'
#     return [note_repr(idx) for idx in sorted(notes.keys())]
#
#
# @app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
# def patients_detail(key):
#     """
#     Retrieve, update or delete note instances.
#     """
#     if request.method == 'PUT':
#         note = str(request.data.get('text', ''))
#         notes[key] = note
#         return note_repr(key)
#
#     elif request.method == 'DELETE':
#         notes.pop(key, None)
#         return '', status.HTTP_204_NO_CONTENT
#
#     # request.method == 'GET'
#     if key not in notes:
#         raise exceptions.NotFound()
#     return note_repr(key)


if __name__ == '__main__':
    app.run(debug=True)
