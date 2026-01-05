import paho.mqtt.client as mqtt
import json

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "idea8/train_mount_device/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker successfully!")
        client.subscribe(MQTT_TOPIC)
        print(f"📡 Subscribed to topic: {MQTT_TOPIC}")
        print("🎧 Waiting for messages...\n")
    else:
        print(f"❌ Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Parse the JSON message
        data = json.loads(msg.payload.decode())
        
        print("=" * 60)
        print(f"📩 NEW MESSAGE RECEIVED")
        print("=" * 60)
        print(f"🆔 Device ID:    {data.get('device_id', 'N/A')}")
        print(f"📐 Roll:         {data.get('roll', 'N/A')}°")
        print(f"📏 Pitch:        {data.get('pitch', 'N/A')}°")
        print(f"🚀 Speed:        {data.get('speed', 'N/A')} km/h")
        print(f"🌍 Latitude:     {data.get('latitude', 'N/A')}")
        print(f"🌍 Longitude:    {data.get('longitude', 'N/A')}")
        print(f"🛰️  Satellites:   {data.get('satellites', 'N/A')}")
        print(f"⏰ Timestamp:    {data.get('timestamp', 'N/A')}")
        print("=" * 60)
        print()
        
    except json.JSONDecodeError:
        print(f"⚠️  Received non-JSON message: {msg.payload.decode()}\n")
    except Exception as e:
        print(f"❌ Error processing message: {e}\n")

def main():
    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Connect to broker
    print(f"🔌 Connecting to MQTT broker: {MQTT_BROKER}:{MQTT_PORT}")
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    print("Press Ctrl+C to stop\n")
    
    try:
        # Start listening (blocking call)
        client.loop_forever()
    except KeyboardInterrupt:
        print("\n🛑 Stopping subscriber...")
        client.disconnect()
        print("👋 Disconnected from MQTT broker")

if __name__ == "__main__":
    main()