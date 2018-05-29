from Publisher import Publisher
from Subscriber import Subscriber

publisher = Publisher()
subscriber = Subscriber()
subscriber.subscriberName = "Hello World"
publisher.add(subscriber)
publisher.publish("Hello from Publisher")
publisher.filter_publish("Hello World", "Hello From Filter Publisher")
