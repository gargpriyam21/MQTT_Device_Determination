# MQTT_Device_Determination - MQTT Subscriber Only (Raspberry Pi B)
## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3
- Raspberry PI OS

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt
- RPi.GPIO

```
pip install paho-mqtt
pip install RPi.GPIO
pip install numpy
```

### Hardware
- Raspberry PI B
- 3 LEDS
- 3 Resistors
- 4 Jumper Wires
- BreadBoard
- Keyboard, mouse & display (not mandatory)


## Procedure
### Hardware setup for Raspeberry PI B

Connect the raspberry pi to a power source and connect the keyboard,mouse and display if required.

Connect the jumper Wire 1 from ground pin to the breadboard. This will serve as a ground.

Connect the jumper Wire 2 from 37th pin to the breadboard. This will serve as a output pin for LED 1.

Connect the jumper Wire 3 from 35th pin to the breadboard. This will serve as a output pin for LED 2.

Connect the jumper Wire 4 from 33rd pin to the breadboard. This will serve as a output pin for LED 3.

Connect the 3 resistors in series with the above jumper wires respectively.

Connect one end of the LEDS in series with each resistor and jumper wires.

Ground the other ends

The circuit diagram for this implementation can be seen in the file "Raspberry Pi B Schematics.png".

### Software run for Raspeberry PI B

Initially update the `BROKER_IP_ADDRESS` and `PORT`in the code file (*Laptop2.py*) to the IP_ADDRESS and PORT of device where the Broker is currently running. If the broker is on the same device update the value of BROKER_IP_ADDRESS to **'localhost'** and PORT to **'1883'**

Run the ***Raspberry Pi B (this will only be subscriber)*** code by executing the below command on the Raspberry Pi

```
python3 RPiB.py
```
