# IoT_ASN3_G11 - MQTT Subscriber Only (Raspberry Pi B)

This repository is created for the sole purpose of uploading codes related to the Assignment 3 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3
- Raspberry PI OS
- PAHO MQTT

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt
- mosquitto

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

Connect the jumper Wire 2 from 37th pin to the breadboard. This will serve as a output pin for led 1.

Connect the jumper Wire 3 from 35th pin to the breadboard. This will serve as a output pin for led 2.

Connect the jumper Wire 4 from 33rd pin to the breadboard. This will serve as a output pin for led 3.

Connect the 3 resistors in series with the above jumper wires respectively.

Connect one end of the LEDS in series with each resistor and jumper wires.

Ground the other ends

### Software run for Raspeberry PI B

Initially update the `BROKER_IP_ADDRESS` in the code file (*RPiB.py*) to the IP_ADDRESS of device where the Broker is currently running. If the broker is on the same device update the value to **'localhost'**
Run the ***Raspberry Pi B (this will only be subscriber)*** code by executing the below command on the Raspberry Pi

```
python3 RPiB.py
```

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
