# IoT_ASN3_G11 - MQTT publisher as well as subscriber (Raspberry Pi A)

This repository is created for the sole purpose of uploading codes related to the Assignment 3 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

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

The circuit diagram for this implementation can be seen in the file "Pi A diagram labeled.png".

##Pinout
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

- Update BROKER_IP_ADDRESS and PORT in the RPiA.py file to the IP address and port of the intended device running the Broker. If running on the same device, use address 'localhost'
- To run from file location: `python3 RPiA.py`


# Instructor
- Dr. Muhammad Shahzad (mshahza@ncsu.edu )

# Teaching Assistants
- Hassan Ali Khan (hakhan@ncsu.edu)

# Team
- Priyam Garg (pgarg6@ncsu.edu)
- Divyang Doshi	(ddoshi2@ncsu.edu)
- Brendan Driscoll (bhdrisco@ncsu.edu)
- Jordan Boerger (jwboerge@ncsu.edu)
- Vishal Veera Reddy (vveerar2@ncsu.edu)
