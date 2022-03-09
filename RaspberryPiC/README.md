# IoT_ASN3_G11 - MQTT publisher as well as subscriber (Raspberry Pi C)

This repository is created for the sole purpose of uploading codes related to the Assignment 3 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt
- mosquitto

### Hardware
Given the inflated prices of Raspberry Pi these days, we had decided to use a laptop to replace Raspberry Pi C, Apple Macbook Pro with macOS Monterey Version 12.2.1 was used.

## Procedure
Initially update the `BROKER_IP_ADDRESS` in the code file (*RPiC.py*) to the IP_ADDRESS of device where the Broker is currently running. If the broker is on the same device update the value to **'localhost'**
Run the ***Raspberry Pi C (this will be publisher as well as subscriber)*** code by executing the below command on the Raspberry Pi
```
python3 RPiC.py
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