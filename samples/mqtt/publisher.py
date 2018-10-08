import paho.mqtt.client as paho
import time


def getTemperature():
    # in a real-world application this function would read the temperature from a Sensor
    temperature = 120
    return temperature


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    # mid is the messageId
    print("mid: " + str(mid))


# Instancing a MQTT client
client = paho.Client()

# Specify Callback Functions
client.on_publish = on_publish
client.on_connect = on_connect

# Initiating the connection
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    # This is an endless loop that will read data from the sensor every 10 seconds and sends it to the broker
    temperature = getTemperature()
    (rc, mid) = client.publish("uno/isqa8380/george-royce/temperature", str(temperature), qos=1)
    time.sleep(10)
