# MQTT_Device_Determination - MQTT publisher as well as subscriber (Raspberry Pi C)
## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt

```
pip install paho-mqtt
pip install RPi.GPIO
pip install numpy
```

### Hardware
Given the inflated prices of Raspberry Pi these days, we had decided to use a laptop to replace Raspberry Pi C, Apple Macbook Pro with macOS Monterey Version 12.2.1 was used.

## Procedure
Initially update the `BROKER_IP_ADDRESS` and `PORT`in the code file (*Laptop2.py*) to the IP_ADDRESS and PORT of device where the Broker is currently running. If the broker is on the same device update the value of BROKER_IP_ADDRESS to **'localhost'** and PORT to **'1883'**

Run the ***Raspberry Pi C (this will be publisher as well as subscriber)*** code by executing the below command on the Raspberry Pi
```
python3 RPiC.py
```