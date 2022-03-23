import os
import sys
import time
from datetime import datetime
import statistics
import collections
from collections import defaultdict
from paho.mqtt import client as mqtt

# BROKER IP: Need to change if the broker is changed
BROKER_IP_ADDRESS = '107.13.179.1'
PORT = 3276
KEEPALIVE = 60
MQTT_TOPICS = [("ncsu/iot/G11/lightSensor",2), ("ncsu/iot/G11/threshold",2), ("ncsu/iot/G11/LightStatus",2), ("ncsu/iot/G11/Status/RaspberryPiA",2), ("ncsu/iot/G11/Status/RaspberryPiC",2)]

FILENAME = 'LogFile.csv'

def appendFile(content):
    file = open(FILENAME, "a")
    file.write(content + "\n")
    file.close()

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
        BUFFER = "Threshold Value"
    elif TOPIC == MQTT_TOPICS[2][0]:
        DEVICE = "Raspberry Pi C"
        BUFFER = "Light Status"

        print("\n" + TIMESTAMP + ": LED 1 is now " + MESSAGE_SENT + "\n")

    elif TOPIC == MQTT_TOPICS[3][0]:
        DEVICE = "Raspberry Pi A"
        BUFFER = "Raspberry A Status"
    elif TOPIC == MQTT_TOPICS[4][0]:
        DEVICE = "Raspberry Pi C" 
        BUFFER = "Raspberry C Status"

    content = TIMESTAMP + "," + DEVICE + ',' + BUFFER + ',' + MESSAGE_SENT
    appendFile(content)
    # print(TIMESTAMP + ": Received Message - '" + BUFFER + " : " + MESSAGE_SENT + "' from Device '" + DEVICE + "'")

def run():

    file = open(FILENAME, "w")
    file.write("TimeStamp,Device,Topic,Message Received" + "\n")
    file.close()
    
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