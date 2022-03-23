import os
import sys
import time
from datetime import datetime
import statistics
import collections
from collections import defaultdict
from collections import deque
from paho.mqtt import client as mqtt

# BROKER IP: Need to change if the broker is changed
BROKER_IP_ADDRESS = '107.13.179.1'
PORT = 3276
KEEPALIVE = 60

MQTT_SUBSCRIBE_TOPICS = [("ncsu/iot/G11/lightSensor",2), ("ncsu/iot/G11/threshold",2), ("ncsu/iot/G11/LightStatus",2)]
MQTT_PUBLISH_TOPICS = [("ncsu/iot/G11/LightStatus",2), ("ncsu/iot/G11/Status/RaspberryPiC",2)]

OFF = "TurnOff"
ON = "TurnOn"

THRESHOLD = None
LDR_VALUE = None
PREVIOUS_LIGHTSTATUS = "None"
LIGHTSTATUS = OFF

LAST_WILL_MESSAGE = "offline"

LDR_Q = deque()
POTEN_Q = deque()
PREV_SET = True

def on_connect(client, userdata, flags, rc):
    topic = MQTT_PUBLISH_TOPICS[1][0]
    qos = MQTT_PUBLISH_TOPICS[1][1]
    client.publish(topic = topic, payload = "online", qos = qos, retain = True)
    print("Connected to the Broker with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    topic = MQTT_PUBLISH_TOPICS[1][0]
    qos = MQTT_PUBLISH_TOPICS[1][1]
    client.publish(topic = topic, payload = "offline", qos = qos, retain = True)
    print("Disconnected to the Broker with result code "+str(rc))

def on_message(client, userdata, message):
    global LIGHTSTATUS, PREVIOUS_LIGHTSTATUS, THRESHOLD, LDR_VALUE, LDR_Q, POTEN_Q, PREV_SET

    TOPIC = message.topic
    QOS = message.qos

    if TOPIC == MQTT_SUBSCRIBE_TOPICS[0][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        # LDR_VALUE = float(MESSAGE)
        LDR_Q.append(float(MESSAGE))

    elif TOPIC == MQTT_SUBSCRIBE_TOPICS[1][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        # THRESHOLD = float(MESSAGE)
        POTEN_Q.append(float(MESSAGE))

    elif TOPIC == MQTT_SUBSCRIBE_TOPICS[2][0]:
        MESSAGE = str(message.payload.decode("utf-8"))
        PREVIOUS_LIGHTSTATUS = MESSAGE
        PREV_SET = True

    if LDR_Q and POTEN_Q and len(LDR_Q) == len(POTEN_Q) and PREV_SET:
        calculate_lightstatus(client)

def calculate_lightstatus(client):

    global LIGHTSTATUS, PREVIOUS_LIGHTSTATUS, THRESHOLD, LDR_VALUE, LDR_Q, POTEN_Q, PREV_SET

    ONE_PUBLISHED = False
    while LDR_Q and POTEN_Q:
        # print("LDR")
        # print(LDR_Q)

        # print("Poten")
        # print(POTEN_Q)

        # print("Light Status = " + LIGHTSTATUS)
        # print("Prev Light Status = " + PREVIOUS_LIGHTSTATUS)

        # print("*"*50)

        LDR_VALUE = LDR_Q.popleft()
        THRESHOLD = POTEN_Q.popleft()
        if LDR_VALUE >= THRESHOLD:
            LIGHTSTATUS = ON
        else:
            LIGHTSTATUS = OFF
        
        if LIGHTSTATUS != PREVIOUS_LIGHTSTATUS:
            topic = MQTT_PUBLISH_TOPICS[0][0]
            qos = MQTT_PUBLISH_TOPICS[0][1]
            ONE_PUBLISHED = True
            client.publish(topic = topic, payload = LIGHTSTATUS, qos = qos, retain = True)
            print("Published Message '" + LIGHTSTATUS + "' to the Broker")
            break

    if ONE_PUBLISHED:
        PREV_SET = False

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
