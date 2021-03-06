# Thanks to: https://techtutorialsx.com/2017/04/14/python-publishing-messages-to-mqtt-topic/
"""Publish a Topic to MQTT Broker"""

import paho.mqtt.client as mqttClient
import paho.mqtt.client as paho
import time
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to broker')
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print('Connection failed')
 
Connected = False   #global variable for the state of the connection

# After you successfully the publisher and subscribe code, 
# try to create your own MQTT broker by create an account at cloudmqtt.com
broker_address= 'mqtt.eclipse.org'
port = 1883 # do not type string, but change to integer

client = mqttClient.Client()               #create new instance
#client.username_pw_set(username, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True: 
        #value = input('Enter the message:')
        client.publish('myhome/Wahyu170010115/kitchen')
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()