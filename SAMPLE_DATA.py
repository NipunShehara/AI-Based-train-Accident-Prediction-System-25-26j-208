import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "idea8/train_mount_device/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker successfully!")
    else:
        print(f"❌ Failed to connect, return code {rc}")

def generate_random_data():
    """Generate random train data"""
    data = {
        "device_id": "TrainMonitor_12345",
        "latitude": round(6.0 + random.uniform(0, 1), 6),  # Random lat around Sri Lanka
        "longitude": round(80.0 + random.uniform(0, 1), 6),  # Random lon around Sri Lanka
        "roll": random.randint(-10, 10),  # Roll angle in degrees
        "pitch": random.randint(-10, 10),  # Pitch angle in degrees
        "speed": random.randint(0, 120),  # Speed in km/h
        "satellites": random.randint(6, 12),  # Number of satellites
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    return data

def main():
    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    
    # Connect to broker
    print(f"🔌 Connecting to MQTT broker: {MQTT_BROKER}:{MQTT_PORT}")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    
    time.sleep(2)  # Wait for connection
    
    print(f"📡 Publishing data to topic: {MQTT_TOPIC}")
    print("Press Ctrl+C to stop\n")
    
    try:
        counter = 1
        while True:
            # Generate and publish data
            data = generate_random_data()
            message = json.dumps(data)
            
            result = client.publish(MQTT_TOPIC, message)
            
            if result.rc == 0:
                print(f"✅ Message {counter} published:")
                print(f"   Roll: {data['roll']}°, Pitch: {data['pitch']}°, Speed: {data['speed']} km/h")
                print(f"   Location: {data['latitude']}, {data['longitude']}\n")
            else:
                print(f"❌ Failed to publish message {counter}")
            
            counter += 1
            time.sleep(2)  # Send data every 2 seconds
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping publisher...")
        client.loop_stop()
        client.disconnect()
        print("👋 Disconnected from MQTT broker")

if __name__ == "__main__":
    main()