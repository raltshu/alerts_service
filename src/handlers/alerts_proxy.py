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
                'alert_text':self.alert_type}

    def dispatch_to_db(self):
        response = requests.post(url=f"{dataservice}/alert", json=self.to_json())
        return response


class AlertView(FlaskView):

    def index(self):
        #TODO: Data service get first 20 lines for display
        return "Hello"
    
    @route('/train_model_started', methods=['POST'])
    def train_model_started(self):
        alert = BasicAlert(INFO,TRAIN_MODEL,'Train model started')
        return alert.dispatch_to_db()
    
    @route('/train_model_complete', methods=['POST'])
    def train_model_started(self):
        model_metrics = request.get_json()
        alert = BasicAlert(INFO,TRAIN_MODEL,f'Train model completed {model_metrics}')
        return alert.dispatch_to_db()
