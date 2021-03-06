# MQTT_Device_Determination - MQTT publisher as well as subscriber (Raspberry Pi A)

## Environment
- Python 3.7.3
- RaspberryPi OS
- Paho MQTT

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt 1.6.1
- mosquitto
- RPi.GPIO
- numpy

### Hardware
- Raspberry Pi 3B
- 1 photoresistor
- 1 500 kOhm Potentiometer
- 1 220 nF capacitor
- 1 1 uF capacitor
- 2 1 kOhm resistors

For our implementation, we didn’t use an ADC. Instead we measured the time it took for capacitors to either charge or discharge by monitoring how long it takes for the raspberry pi input pins to change from high to low or vice versa. This works since the charge time for a capacitor in an RC circuit is dependent on the resistance, and the higher the resistance the longer it will take for the capacitor to charge.

We developed a sensing hat for the Pi that attaches directly to the GPIO pins. This was done to keep the implementation light weight and reduce the risk of wires coming loose over time.

The circuit diagram for this implementation can be seen in the file "Raspberry Pi A Schematics.png".

## Pinout

GPIO 17: Charge Pin, this pin is used to charge the capacitor in the potentiometer circuit

GPIO 22: Potentiometer Pin, this pin monitors the status of the capacitor in the potentiometer circuit to see if it is HIGH or LOW

GPIO 19: LDR Pin, this pin is dual purpose. It both discharges the capacitor in the LDR circuit and monitors the status of the capacitor to see if it is HIGH or LOW.

## Procedure
### Software
- Install python3
- Install required packages

```
pip install paho-mqtt
pip install RPi.GPIO
pip install numpy
```

Initially update the `BROKER_IP_ADDRESS` and `PORT`in the code file (*Laptop2.py*) to the IP_ADDRESS and PORT of device where the Broker is currently running. If the broker is on the same device update the value of BROKER_IP_ADDRESS to **'localhost'** and PORT to **'1883'**

- To run from file location: 

```
python3 RPiA.py
```