# MQTT_Device_Determination - MQTT Subscriber Only (Laptop # 2)
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

## Procedure
Initially update the `BROKER_IP_ADDRESS` and `PORT`in the code file (*Laptop2.py*) to the IP_ADDRESS and PORT of device where the Broker is currently running. If the broker is on the same device update the value of BROKER_IP_ADDRESS to **'localhost'** and PORT to **'1883'**

Run the ***Laptop # 2 (this will only be subscriber)*** code by executing the below command on a new terminal window
```
python3 laptop2.py
```

The detail logs will be saved in the `LogFile.csv` file in such format:

```
TimeStamp,Device,Topic,Message Received
```

also the LED1 status will be printing in the format 

```
{TIMESTAMP} + ": LED 1 is now " + {Status}
```