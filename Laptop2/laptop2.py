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
MQTT_TOPICS = [("ncsu/iot/G11/lightSensor",2), ("ncsu/iot/G11/threshold",2), ("ncsu/iot/G11/LightStatus",2), ("ncsu/iot/G11/Status/RaspberryPiA",2), ("ncsu/iot/G11/Status/RaspberryPiC",2)]

def on_connect(client, userdata, flags, rc):
    print("Connected to the Broker with result code "+str(rc))

def on_message(client, userdata, message):
    TOPIC = message.topic
    QOS = message.qos
    DEVICE = None

    TIMESTAMP = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
    MESSAGE_SENT = str(message.payload.decode("utf-8"))
    BUFFER = ""

    if TOPIC == MQTT_TOPICS[0][0]:
        DEVICE = "Raspberry Pi A"
        BUFFER = "LDR Value"
    elif TOPIC == MQTT_TOPICS[1][0]:
        DEVICE = "Raspberry Pi A"
        BUFFER = "Threshold"
    elif TOPIC == MQTT_TOPICS[2][0]:
        DEVICE = "Raspberry Pi C"
        BUFFER = "Light Status"
    elif TOPIC == MQTT_TOPICS[3][0]:
        DEVICE = "Raspberry Pi A"
        BUFFER = "RaspPi A Status"
    elif TOPIC == MQTT_TOPICS[4][0]:
        DEVICE = "Raspberry Pi C" 
        BUFFER = "RaspPi C Status"

    print(TIMESTAMP + ": Received Message - '" + BUFFER + " : " + MESSAGE_SENT + "' from Device '" + DEVICE + "'")

def run():
    
    subscriber = mqtt.Client("Laptop2")
    
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message

    subscriber.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)

    subscriber.loop_start()

    subscriber.subscribe(MQTT_TOPICS)

    while True:
        continue


if __name__ == '__main__':
    run()