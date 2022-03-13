import paho.mqtt.client as mqtt

#mqttClient = mqtt.Client("makerio_mqtt")
#mqttClient.connect("test.mosquitto.org", 1883)
#mqttClient.publish("topic", "message")
#mqttClient.subscribe("topic")

# Constants
BROKER_IP_ADDRESS = 'localhost'
PORT = 1883
KEEPALIVE = 200

LIGHTSENSOR_TOPIC = "lightSensor"
THRESHOLD_TOPIC = "threshold"
STATUS_TOPIC = "Status/RaspberryPiA"

SUCCESS_CODE = 0

STATUS_CONNECT_MSG = "online"
STATUS_DISCONNECT_MSG = "offline"

#Callbacks
def mqtt_connect(client, data, flags, rc):
    if rc == SUCCESS_CODE:
        client.publish(STATUS_TOPIC, STATUS_CONNECT_MSG)
        print(f"Connected")
    else:
        print(f"Failed connection. Code {rc}")

def mqtt_disconnect(client, data, rc):
    if rc == SUCCESS_CODE:
        client.publish(STATUS_TOPIC, STATUS_DISCONNECT_MSG)
        print("Graceful disconnect successful")
    else:
        print(f"Forced disconnect. Code {rc}")

def mqtt_message_rcv(client, data, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic + message)

def main():
    
    # Create client
    mqttClient = mqtt.Client("RPiA")
    
    # Define callbacks
    mqttClient.on_connect = mqtt_connect
    mqttClient.on_message = mqtt_message_rcv
    mqttClient.on_disconnect = mqtt_disconnect

    # Lastwill msg
    mqttClient.will_set(STATUS_TOPIC, STATUS_DISCONNECT_MSG, 0, True)

    mqttClient.connect(host = BROKER_IP_ADDRESS, port = PORT, keepalive = KEEPALIVE)
    mqttClient.loop_start()   

    #mqttClient.subscribe(MQTT_TOPICS)

    while True:
        continue


if __name__ == '__main__':
    main()