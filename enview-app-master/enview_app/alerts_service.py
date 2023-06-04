import requests
import requests_cache

from enview_app.vehicle_service import Vehicle

FLUSH_PERIOD = 10 * 60  # 10 minutes in seconds
requests_cache.install_cache(expire_after=FLUSH_PERIOD)


class AlertService:
    def __init__(self):
        """
        Currently Alert Service is handling events and alerts for a single vehicle.
        It can easily be extended to handle multiple vehicles using list.
        It also provides additional functionality to get all alerts and vehicle details.
        All error handling is done here but is intended to be moved closer to source.
        """
        self.vehicle = Vehicle()

    def add_event(self, app, request_form) -> dict:
        timestamp = request_form.get("timestamp")
        is_driving_safe = request_form.get("is_driving_safe")
        try:
            self.vehicle.add_event(app, timestamp, is_driving_safe)
            app.logger.info('events queue is now: %s ,for vehicle with ID %s',
                            self.vehicle.events, self.vehicle.id)
            return {'error': False}
        except Exception as e:
            app.logger.error('error: %s, while adding event with timestamp %s for vehicle ID %s',
                             e, timestamp, self.vehicle.id)
            return {'error': str(e)}

    def get_alerts(self, app) -> dict:
        try:
            return self.vehicle.get_alerts()
        except Exception as e:
            app.logger.error('error: %s getting alerts for vehicle ID %s',
                             e, self.vehicle.id)
            return {'error': str(e)}

    def get_vehicle_details(self, app) -> dict:
        try:
            return {'vehicle_details': str(vars(self.vehicle))}
        except Exception as e:
            app.logger.error('error: %s, while fetching vehicle details of vehicle ID %s',
                             e, self.vehicle.id)
            return {'error': str(e)}

    def get_alert_for_id(self, app, alert_id) -> dict:
        try:
            return self.vehicle.get_alert(alert_id)
        except Exception as e:
            app.logger.error('error %s getting alerts for vehicle ID %s',
                             e, self.vehicle.id)
            return {'error': str(e)}
