from xml.sax.handler import property_declaration_handler
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import numpy as np


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
pot_arr = np.array([0,0,0,0])
ldr_arr = np.array([0,0,0,0])
pot_value = 0
ldr_value = 0

#initalize GPIO board
charge_pin = 17
pot_pin = 22
LDR_pin = 19
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


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


def read_pot():
	count = 0
	#discharge capacitor
	GPIO.setup(charge_pin, GPIO.IN)
	GPIO.setup(pot_pin, GPIO.OUT)
	GPIO.output(pot_pin, GPIO.LOW)
	time.sleep(0.01)

	#charge capacitor
	GPIO.setup(pot_pin, GPIO.IN)
	GPIO.setup(charge_pin, GPIO.OUT)
	GPIO.output(charge_pin, GPIO.HIGH)

	#Count until capacitor is charged
	count = 0
	while (GPIO.input(pot_pin) == GPIO.LOW):
        	count = count + 1
	return count


def read_LDR():
	#set LDR charger to low and allow time for capacitor to discharge
	GPIO.setup(LDR_pin, GPIO.OUT)
	GPIO.output(LDR_pin, GPIO.LOW)
	time.sleep(0.01)

	#charge capacitor
	GPIO.setup(LDR_pin, GPIO.IN)
	#   print("checking LDR...")
	#Count until capacitor is charged
	count = 0
	while (GPIO.input(LDR_pin) == GPIO.LOW):
	        count = count + 1
	return count

def sig_difference(new_val, old_val, threshold):
	return np.abs(new_val - old_val) > threshold

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

	#define threshold for publishing values
	threshold = 100
	print("starting loop")
	while True:
		"""
		@BRENDAN
		Add sampling / scaling here
		Place publish messages below where needed if sample is
		outside of threshold or should we do this on msg rcv?
		"""
		#take moving average of pot & ldr values
		time.sleep(0.05)
		for i in range(0,3):
			pot_arr[i] = pot_arr[i+1]
			ldr_arr[i] = ldr_arr[i+1]
		pot_arr[3] = read_pot()
		ldr_arr[3] = read_LDR()
		pot_value = np.average(pot_arr)
		ldr_value = np.average(ldr_arr)
		if sig_difference(pot_value, pot_last_value, threshold) or sig_difference(ldr_value, ldr_last_value, threshold):
			mqttClient.publish(TOPIC_LIGHTSENSOR, pot_value, 2, True)
			mqttClient.publish(TOPIC_THRESHOLD, ldr_value, 2, True)
			#Debug statments: uncomment to observe LDR and pot values being uploaded
			#print("updated!")
			#print("LDR: " + str(ldr_value))
			#print("pot: " + str(pot_value))


if __name__ == '__main__':
    main()
