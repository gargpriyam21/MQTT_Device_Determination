from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt

# Constants
BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
KEEPALIVE = 60

TOPIC_LIGHTSENSOR = "lightSensor"
TOPIC_THRESHOLD = "threshold"
TOPIC_STATUS = "Status/RaspberryPiA"

SUCCESS_CODE = 0

STATUS_CONNECT_MSG = "online"
STATUS_DISCONNECT_MSG = "offline"

# Variables for pot and ldr data
pot_last_value = 0
ldr_last_value = 0

# Callbacks
def mqtt_connect(client, data, flags, rc):
    if rc == SUCCESS_CODE:
        client.publish(TOPIC_STATUS, STATUS_CONNECT_MSG, 2, True)
        print(f"Connected")
    else:
        print(f"Failed connection. Code {rc}")

def mqtt_disconnect(client, data, rc):
    if rc == SUCCESS_CODE:
        client.publish(TOPIC_STATUS, STATUS_DISCONNECT_MSG, 2, True)
        print("Graceful disconnect successful")
    else:
        print(f"Forced disconnect. Code {rc}")

def mqtt_message_rcv(client, data, message):
    _topic = message.topic
    
    if _topic == TOPIC_THRESHOLD:
        pot_last_value = float(message.payload.decode("utf-8"))

    elif _topic == TOPIC_LIGHTSENSOR:
        ldr_last_value = float(message.payload.decode("utf-8"))

# main
def main():
    
    # Create client
    mqttClient = mqtt.Client("RPiA")
    
    # Define callbacks
    mqttClient.on_connect = mqtt_connect
    mqttClient.on_message = mqtt_message_rcv
    mqttClient.on_disconnect = mqtt_disconnect

    # Lastwill msg
    mqttClient.will_set(TOPIC_STATUS, STATUS_DISCONNECT_MSG, 0, True)

    # Connect to broker
    mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
    mqttClient.loop_start()   

    # Subscribe for last value
    mqttClient.subscribe(TOPIC_LIGHTSENSOR)
    mqttClient.subscribe(TOPIC_THRESHOLD)

    while True:
        """
        @BRENDAN
        Add sampling / scaling here
        Place publish messages below where needed if sample is
        outside of threshold or should we do this on msg rcv?
        """
        #mqttClient.publish(TOPIC_LIGHTSENSOR, pot_last_value, 2, True)
        #mqttClient.publish(TOPIC_THRESHOLD, ldr_last_value, 2, True)


if __name__ == '__main__':
    main()