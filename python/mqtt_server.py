import paho.mqtt.client as mqtt
import json
import uuid
from datetime import datetime
from random import uniform
import time
import math

# Define constants
MQTT_BROKER = "localhost" # "192.168.0.121"  # Change this to your MQTT broker address
MQTT_PORT = 1883
VEHICLE_ID = "vehicle/1234/status"  # Change this to the desired vehicle ID

N_TILES_Y = 12
N_TILES_X = 13
TILE_LENGTH_MM = 600
TILE_WIDTH_MM = 600


# Define function to generate mock data
def generate_mock_data(dt):
    radius = 1
    x = 5 + math.sin(dt)*radius
    y = 5 + math.cos(dt)*radius

    data = {
        "type": "status_vehicle",
        "data": {
            "id": str(12),
            "name": "My Vehicle",
            "timestamp": datetime.now().isoformat(),
            "coordinates": {
                "x": x,
                "y": y,
                "yaw": uniform(0, 360), # grad vs rad?
                "x_abs": uniform(0, N_TILES_X * TILE_LENGTH_MM),
                "y_abs": uniform(0, N_TILES_Y * TILE_WIDTH_MM)
            }
        }
    }
    return json.dumps(data)

# Define callback function to handle MQTT connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# Define MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT)

# Publish mock data every 1 seconds
while True:
    print("Publishing mock data...")
    client.publish(VEHICLE_ID, generate_mock_data(time.time()))
    print("Done...")
    time.sleep(1)