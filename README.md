# IoT_ASN3_G11

This repository is created for the sole purpose of uploading codes related to the Assignment 3 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

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
