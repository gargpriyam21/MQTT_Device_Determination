# MQTT_Device_Determination

The main objective of the the project is to get the hands-on experience with MQTT.
In the project we have implemented a complete IoT environment where there are 5 devices each one with different use cases as explained below:

### Device 1. Raspberry Pi A 

This device will serve as both the publisher and the subscriber. An ADC connects an LDR and a potentiometer to your Raspberry Pi A. The LDR will be used to detect the quantity of light falling on it and to switch an LED on and off dependent on the amount of light falling on it. The potentiometer will be used to adjust the threshold at which the LED will illuminate. 

This device will sample the LDR and potentiometer readings every 100 milliseconds. It will compare the LDR and potentiometer values to the most recent values of the LDR and potentiometer, respectively.

The device will broadcast the LDR values to the topic "lightSensor" and the potentiometer values to the subject "threshold" to the broker running on Laptop #1.

### Device 2. Raspberry Pi B

This device will only be subscribers. The Raspberry Pi B is wired with three LEDs: LED1, LED2, and LED3. This device will be linked to the broker and will subscribe to the topics "LightStatus," "Status/RaspberryPiA," and "Status/RaspberryPiC." This device will illuminate the LEDs LED1, LED2, and LED3 based on the values received from the subjects "LightStatus", "Status/RaspberryPiA", and "Status/RaspberryPiC".

### Device 3. Raspberry Pi C

This device will be the publisher as well as the subscriber. This device will be linked to the broker as well, and it will be subscribed to the subjects "lightSensor" and "threshold." When it gets a message from the broker with the subjects "lightSensor" and/or "threshold," it compares the LDR value to the threshold and returns a binary result: "TurnOn" if "lightSensor" value >= "threshold" value, else "TurnOff." 

The Raspberry Pi C then compares the outcome to the choice it sent to the broker before. The device will broadcast the choice made by the broker on Laptop #1 to the "LightStatus" topic.

### Device 4. Laptop #2

This device will only be available to subscribers. This device will be subscribed to all of the following topics: "lightSensor", "threshold", "LightStatus", "Status/RaspberryPiA", and "Status/RaspberryPiC" and should show the messages sent by the broker on these topics as well as the timestamps.

### Device 5. Laptop #1

This device will operate as the broker for the MQTT protocol, handling communication and message transmission from one device to another.

All the MQTT devices are using QoS2 and will be sending the last will message on the graceful and disgraceful disconnect.

## Motivation
You could keep track of when each electrical/electronic gadget in your home was turned on and off if you implemented such a system. Furthermore, we know the typical power usage of most electrical gadgets. So, using your laptop or smartphone, you could run some data analysis to identify which gadget utilized how much power each day. 

This research might assist you in determining which sources are contributing the most to your home's power usage and, as a result, taking the most money out of your wallet. If we apply it to a smart building, the electricity savings might be enormous.

If we apply it to a smart building, the energy savings might be enormous. Going a step further, we might employ machine learning techniques to automate the process of recognizing high power consumption devices and suitably lowering their use without the need for human interaction.

# Setup
## Environment
- Python 3.7.3

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt v1.6.1
- numpy v1.19.5
- mosquitto 
- RPi.GPIO

```
pip install paho-mqtt
pip install RPi.GPIO
brew install mosquitto
```
### Hardware

- Raspberry PI A,B (We have used Raspberry Pi 3B model)
- 3 LEDS
- 5 Resistors
  - 2 1kOhm Resistors
  - 3 230 Ohm Resistors
- 1 Photoresistor (LDR)
- 1 500 kOhm Potentiometer
- Jumper Wires
- BreadBoard
- 1 220 nF capacitor
- 1 1 uF capacitor
- Keyboard, mouse & display (not mandatory)

For our implementation, we didn’t use an ADC. Instead we measured the time it took for capacitors to either charge or discharge by monitoring how long it takes for the raspberry pi input pins to change from high to low or vice versa. This works since the charge time for a capacitor in an RC circuit is dependent on the resistance, and the higher the resistance the longer it will take for the capacitor to charge.

We developed a sensing hat for the Pi that attaches directly to the GPIO pins. This was done to keep the implementation light weight and reduce the risk of wires coming loose over time.

## Procedure
For the execution of each code file, the  a detailed README.md file explaining how to execute the code is available in the respective folder of that device.

Laptop #1 : [Laptop #1](./Laptop1)

Laptop #2 : [Laptop #2](./Laptop2)

Raspberry Pi A : [Raspberry Pi A](./RaspberryPiA)

Raspberry Pi B : [Raspberry Pi B](./RaspberryPiB)

Raspberry Pi C : [Raspberry Pi C](./RaspberryPiC)

### Recommended Order to run the devices
Step 1: Run the Broker on Laptop 1

Step 2: Run the Laptop 2 code from its file location

Step 3: Run the Raspberry Pi B code from its file location

Step 4: Run the Raspberry Pi C code from its file location

Step 5: Run the Raspberry Pi A code from its file location