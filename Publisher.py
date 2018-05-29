class Publisher:
    def __init__(self):
        self.subscribers = []

    def add(self, subscriber):
        self.subscribers.append(subscriber)

    def remove(self, subsriber):
        self.subscribers.remove(subsriber)

    def publish(self, output):
        for subscriber in self.subscribers:
            subscriber.notify(output)

    def filter_publish(self, filterCommand, output):
        for subscriber in [subscriber for subscriber in self.subscribers if subscriber.subscriberName == filterCommand]:
            subscriber.notify(output)
