from flask_classful import FlaskView, route
from flask import request, Response
import os
import requests

dataservice = os.environ['dataservice_endpoint']
CRITICAL = 'CRITICAL'
INFO = 'INFO'
WARNING ='WARNING'
ERROR = 'ERROR'

TRAIN_MODEL ='TRAIN_MODEL'
MODEL_SCORE ='MODEL_SCORE'

class BasicAlert:

    def __init__(self, alert_seviriry, alert_type, alert_text) -> None:
        self.alert_sevirity = alert_seviriry
        self.alert_type = alert_type
        self.alert_text = alert_text

    def to_json(self):
        return {'alert_sevirity':self.alert_sevirity,
                'alert_type':self.alert_type,
                'alert_text':self.alert_text}

    def dispatch_to_db(self):
        response = requests.post(url=f"{dataservice}/data/alert", json=self.to_json())
        return response


class AlertView(FlaskView):

    def index(self):
        return "Hello"
    
   
    @route('/train_model_complete', methods=['POST'])
    def train_model_started(self):
        model_metrics = request.get_json()
        alert = BasicAlert(INFO,TRAIN_MODEL,f'Train model completed {model_metrics}')
        return alert.dispatch_to_db().text

    @route('/train_model_begin', methods=['POST'])
    def train_model_begin(self):
        data = request.get_json()
        alert = BasicAlert(INFO,TRAIN_MODEL,'Train model started')
        return alert.dispatch_to_db().text

    @route('/calc_score_complete', methods=['POST'])
    def train_model_started(self):
        model_metrics = request.get_json()
        alert = BasicAlert(INFO,MODEL_SCORE,f'Model Score completed {model_metrics}')
        return alert.dispatch_to_db().text

    @route('/calc_score_begin', methods=['POST'])
    def train_model_begin(self):
        data = request.get_json()
        alert = BasicAlert(INFO,MODEL_SCORE,'Begin model score calculation')
        return alert.dispatch_to_db().text
