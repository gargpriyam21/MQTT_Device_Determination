# MQTT_Device_Determination - MQTT Broker (Laptop # 1)
## Environment
- macOS Monterey Version 12.2.1 (intel)
- Python 3.7.3

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt
- mosquitto

## Procedure
### Setup broker to accept external connections
- Open the mosquitto config file located at /usr/local/etc/mosquitto.conf
  - Change `listener` to `listener 1883`
  - change `allow_anonymous` to `allow_anonymous true`
- Expose the the laptop ip address and port for connecting external devices on different networks.

Run the ***broker*** by executing the below command on a new terminal window
```
/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
```
