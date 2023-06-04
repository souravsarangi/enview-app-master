import collections

from sortedcontainers import SortedDict
from enview_app.util import get_uuid, get_time_object


class Vehicle:
    """
    Each vehicle has a unique UUID and maintains its events stack and alerts generated.
    We keep only past 5 events and once alert is generated all events are flushed out.
    Alerts can be accessed using alert_id which is uniquely generated using utils get_uuid()
    """

    def __init__(self):
        self.id = get_uuid()
        self.events = collections.deque()
        self.alertMap = SortedDict()
        self.alerts = {}

    def __str__(self):
        return f"Vehicle ID is {self.id} and events in past 5 mins are {self.company}, alerts are {self.alerts}"

    def add_alert(self, datetime_obj):
        alert_uuid = get_uuid()
        time_difference_minutes = 10.0
        if len(self.alertMap) != 0:
            time_difference = datetime_obj - self.alertMap.keys()[-1]
            time_difference_minutes = time_difference.total_seconds() / 60
        if time_difference_minutes >= 5.0:
            self.alertMap[datetime_obj] = alert_uuid
            self.alerts[alert_uuid] = datetime_obj

    def check_alert(self, app, datetime_obj) -> bool:
        count_events = 0
        if len(self.events) >= 5:
            for item in self.events:
                time_difference = datetime_obj - item['time']
                time_difference_minutes = time_difference.total_seconds() / 60.0
                if item['is_driving_safe'] is False and time_difference_minutes <= 5.5:
                    count_events += 1
            app.logger.info('count of unsafe events in last 5 mins: %s for vehicle ID: %s',
                            time_difference_minutes, self.id)
            if count_events >= 3:
                return True
        return False

    def add_event(self, app, timestamp, is_driving_safe):
        datetime_obj = get_time_object(timestamp)
        is_driving_safe = is_driving_safe == 'true'
        if len(self.events) == 0 or (len(self.events) != 0 and datetime_obj > self.events[-1]['time']):
            event = {'time': datetime_obj, 'is_driving_safe': is_driving_safe}
            self.events.append(event)
            app.logger.info('event %s ,added for vehicle with ID %s',
                            event, self.id)
        if self.check_alert(app, datetime_obj) is True:
            self.add_alert(datetime_obj)
            self.events.clear()
        app.logger.info('event queue size is: %s , for vehicle with ID %s',
                        len(self.events), self.id)
        if len(self.events) > 5:
            self.events.popleft()

    def get_alerts(self):
        return self.alerts

    def get_alert(self, alert_id) -> dict:
        if alert_id in self.alerts:
            return {'timestamp': self.alerts[alert_id], 'alert_id': alert_id}
        return {}
