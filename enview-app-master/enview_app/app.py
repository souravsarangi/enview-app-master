from flask import Flask, request
from enview_app.alerts_service import AlertService
from enview_app.landing_page_service import greet, get_ip
import os

app = Flask(__name__)
alert_service = AlertService()

DEPLOY = os.environ.get('DEPLOY')


@app.route('/')
def main():
    try:
        if DEPLOY == 'heroku':
            ip = request.headers['X-Forwarded-For']
        else:
            ip = get_ip(app)

        return greet(ip, app)
    except Exception as e:
        return {'error': 'Encountered error fetching climate for ip:' + str(e)}


@app.route('/event', methods=['POST'])
def event():
    request_form = request.form
    return alert_service.add_event(app, request_form)

@app.route("/alert/<alert_id>", methods=['GET'])
def alert(alert_id):
    return alert_service.get_alert_for_id(app, alert_id)

@app.route('/alerts', methods=['GET'])
def alerts():
    return alert_service.get_alerts(app)

@app.route('/vehicle', methods=['GET'])
def vehicle():
    return alert_service.get_vehicle_details(app)


if __name__ == '__main__':
    app.run()
