import paho.mqtt.client as paho


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print("Message Received:")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    # the subscriber could have here more logic to use the data ..


# Instancing MQTT client
client = paho.Client()

# Defining Callback Functions
client.on_subscribe = on_subscribe
client.on_message = on_message

# Connect to Broker
client.connect("broker.mqttdashboard.com", 1883)

# We are subscribing to the topic 8380 and all subtopics (the # sign tells the broker we are interested in subtopics too)
client.subscribe("uno/isqa8380/george-royce/#", qos=1)

# Lets program running
client.loop_forever()
