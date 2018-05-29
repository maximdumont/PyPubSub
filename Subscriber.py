class Subscriber(object):
    DEFAULT_SUBSCRIBER_NAME_VALUE = "No Value"

    def __init__(self, subscriberName=DEFAULT_SUBSCRIBER_NAME_VALUE):
        self.subscriberName = subscriberName

    @property
    def name(self):
        return self.subscriberName

    @name.setter
    def name(self, value):
        self.subscriberName = value

    def notify(self, output):
        print("Subscriber Name,", self.subscriberName)
        print(output)
