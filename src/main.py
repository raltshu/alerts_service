from flask import Flask
from handlers.alerts_proxy import AlertView

app = Flask(__name__)


AlertView.register(app, route_base='/alerts')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5001)
    # load_diamonds_to_db()
    pass

