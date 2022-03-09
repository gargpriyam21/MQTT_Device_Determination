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
MQTT_TOPICS = [("ncsu/iot/G11/LightStatus",2), ("ncsu/iot/G11/Status/RaspberryPiA",2), ("ncsu/iot/G11/Status/RaspberryPiC",2)]

OFF = 0
ON = 1

LED1 = OFF
LED2 = OFF
LED3 = OFF

def on_connect(client, userdata, flags, rc):
    print("Connected to the Broker with result code "+str(rc))

def on_message(client, userdata, message):
    global LED1, LED2, LED3
    TOPIC = message.topic
    QOS = message.qos

    if TOPIC == MQTT_TOPICS[0][0]:
        MESSAGE_SENT = str(message.payload.decode("utf-8"))
        if MESSAGE_SENT.lower() == "turnoff":
            LED1 = OFF
        elif MESSAGE_SENT.lower() == "turnon":
            LED1 = ON
    elif TOPIC == MQTT_TOPICS[1][0]:
        MESSAGE_SENT = str(message.payload.decode("utf-8"))
        if MESSAGE_SENT.lower() == "offline":
            LED2 = OFF
        elif MESSAGE_SENT.lower() == "online":
            LED2 = ON
    elif TOPIC == MQTT_TOPICS[2][0]:
        MESSAGE_SENT = str(message.payload.decode("utf-8"))
        if MESSAGE_SENT.lower() == "offline":
            LED3 = OFF
            LED1 = OFF
        elif MESSAGE_SENT.lower() == "online":
            LED3 = ON
    
    BlinkLEDS()

def BlinkLEDS():
    """
    # @VISHAL VEERA READY
    Please complete this part of the Raspberry pi
    Blink the LED's accordingly to the values of LED1, LED2 and LED3
    """
    # print("LED LightStatus: " + str(LED1))
    # print("LED2 RPiA: " + str(LED2))
    # print("LED3 RPiC: " + str(LED3))
    # print("\n" + "-"*50 + "\n")
    pass


def run():
    
    subscriber = mqtt.Client("RPiB")
    
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message

    subscriber.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)

    subscriber.loop_start()

    subscriber.subscribe(MQTT_TOPICS)

    while True:
        continue


if __name__ == '__main__':
    run()