# Arduino-Raspbian-serial
Codes to serial communication arduino and raspberry
### After Inizializating in Raspberry programming and in arduino programming.
        Its possible to connect both embembed systems by serial comunnication. 
And its not neccesary connect the raspberry pi to a monitor with keyboard and mouse you only need to create two archives.
### The first one is 
        ssh 
        without extenssion and code inside; this archive only enable the ssh protoccol of the raspberry.
### The second is wpa_supplicant.conf and the code is:
        # /etc/wpa_supplicant/wpa_supplicant.conf                                                                                                 ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev                                                                                   update_config=1                                                                                                                           network={                                                                                                                                 ssid="SSID name"                                                                                                                           psk="wi-fi  password"                                                                                                                     key_mgmt=WPA-PSK                                                                                                                           }

#### And both archives save in the sd card of the raspbian system of your raspberry.

# NOTE: you can create multiple networks configuration in the supplicant archive.
