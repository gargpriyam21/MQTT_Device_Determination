import os
import sys
import time
from datetime import datetime
import statistics
import collections
from collections import defaultdict
from paho.mqtt import client as mqtt

# BROKER IP: Need to change if the broker is changed
BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
KEEPALIVE = 200

MQTT_SUBSCRIBE_TOPICS = [("ncsu/iot/G11/lightSensor",2), ("ncsu/iot/G11/threshold",2), ("ncsu/iot/G11/LightStatus",2)]
MQTT_PUBLISH_TOPICS = [("ncsu/iot/G11/LightStatus",2), ("ncsu/iot/G11/Status/RaspberryPiC",2)]

OFF = "TurnOff"
ON = "TurnOn"

THRESHOLD = None
LDR_VALUE = None
PREVIOUS_LIGHTSTATUS = "None"
LIGHTSTATUS = OFF

LAST_WILL_MESSAGE = "offline"

def on_connect(client, userdata, flags, rc):
    topic = MQTT_PUBLISH_TOPICS[1][0]
    qos = MQTT_PUBLISH_TOPICS[1][1]
    client.publish(topic = topic, payload = "online", qos = qos, retain = True)
    print("Connected to the Broker with result code "+str(rc))

def on_disconnect(client, userdata, flags, rc):
    topic = MQTT_PUBLISH_TOPICS[1][0]
    qos = MQTT_PUBLISH_TOPICS[1][1]
    client.publish(topic = topic, payload = "offline", qos = qos, retain = True)
    print("Disconnected to the Broker with result code "+str(rc))

def on_message(client, userdata, message):
    global LIGHTSTATUS, PREVIOUS_LIGHTSTATUS, THRESHOLD, LDR_VALUE

    TOPIC = message.topic
    QOS = message.qos

    if TOPIC == MQTT_SUBSCRIBE_TOPICS[0][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        LDR_VALUE = int(MESSAGE)

    elif TOPIC == MQTT_SUBSCRIBE_TOPICS[1][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        THRESHOLD = int(MESSAGE)

        if THRESHOLD is not None and LDR_VALUE is not None:
            calculate_lightstatus(client)

    elif TOPIC == MQTT_SUBSCRIBE_TOPICS[2][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        PREVIOUS_LIGHTSTATUS = MESSAGE
    
def calculate_lightstatus(client):

    if LDR_VALUE >= THRESHOLD:
        LIGHTSTATUS = ON
    else:
        LIGHTSTATUS = OFF
    
    if LIGHTSTATUS != PREVIOUS_LIGHTSTATUS:
        topic = MQTT_PUBLISH_TOPICS[0][0]
        qos = MQTT_PUBLISH_TOPICS[0][1]
        client.publish(topic = topic, payload = LIGHTSTATUS, qos = qos, retain = True)

def run():
    
    client = mqtt.Client("RPiC",clean_session=False)
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.will_set(topic = MQTT_PUBLISH_TOPICS[1][0], payload = LAST_WILL_MESSAGE, qos = MQTT_PUBLISH_TOPICS[1][1], retain = True)

    client.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)

    client.loop_start()

    client.subscribe(MQTT_SUBSCRIBE_TOPICS)

    while True:
        continue

if __name__ == '__main__':
    run()