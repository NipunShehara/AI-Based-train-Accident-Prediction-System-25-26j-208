# 🚆 AI-Based Train Accident Prediction System in Sri Lanka

> Project ID – 25-26J-208  
> B.Sc. (Hons) Information Technology – SLIIT  
> _AI-powered safety ecosystem for Sri Lankan railways_

---

## 🎯 Executive Summary

This project designs an **end-to-end AI safety ecosystem** for Sri Lankan railways.  
The system combines:

- **Accident risk prediction** from historical data  
- **Level-crossing obstacle & gate automation**  
- **Real-time track damage detection**  
- **Long-range accident prediction for “blind spots”**

By integrating **machine learning, IoT sensors, embedded systems and computer vision**,  
the solution aims to **reduce accidents, save lives and minimize economic loss** in the
Sri Lankan railway network.

---

## 🧩 System Modules (Group Work Allocation)

### 1️⃣ Long-Range Train Detection & Level-Crossing Safety  
**Owner (Group Leader): Fernando W.P.N.S – IT22325778**

- AI-based train detection using long-range cameras  
- Speed & ETA prediction for approaching trains  
- Automatic barrier control and warning lights/sirens  
- Mobile app / dashboard to show crossing status in real time  

---

### 2️⃣ Obstacle Detection & Intelligent Automated Safety System (IASS)  
**Owner: Ekanayaka E.M.L.M – IT22897558**

- Obstacle detection at level crossings using:
  - Real-Time Cameras (RTC)
  - IoT sensors (ultrasonic / infrared / LiDAR where applicable)
- Deep-learning model (e.g. YOLOv5/YOLOv8) for vehicle & pedestrian detection  
- Sensor fusion + PLC logic to:
  - Delay gate closing if an obstacle is detected
  - Send alerts via **Mobile Alert Platform (MAP)** to drivers and control centres  

---

### 3️⃣ Real-Time Railway Track Damage Detection  
**Owner: Vithanachchi N.Y – IT22285560**

- Low-cost **vibration (SW-420)** and **acoustic sensors** on tracks  
- Arduino-based data acquisition and anomaly detection  
- GSM module to notify control centres and train drivers if:
  - Cracks
  - Loose joints
  - Misalignment  
  are detected
- Designed to be **cheap, scalable and suitable for rural lines**

---

### 4️⃣ AI-Based Train-Mounted Safety Monitoring System   
**Owner: Pramodya W.S.C – IT22026170**

Collection of:
  - Real-time GPS data (speed, location)
  - IMU sensor data (acceleration, tilt, roll, yaw)
  - Track geometry information (curves, gradients)
  - Operational parameters (braking patterns, speed limits)
    
Machine-learning models (Decision Tree, Random Forest, etc.) to:
  - Detect overspeeding on curves
  - Identify abnormal tilt angles and harsh braking events
  - Classify train operating conditions into Safe, Warning, and Dangerous levels

Risk scores are sent to the main system to:
  - Provide immediate audio-visual warnings to train operators
  - Log incidents for post-trip safety analysis
  - Support preventive safety actions and operational decision-making for Sri Lanka Railways


---

## 🧠 Technologies Used

**Core Technologies**

- Programming: `Python`, `C/C++` (for Arduino / embedded)
- Frameworks: `TensorFlow` / `PyTorch`, `scikit-learn`
- Computer Vision: `OpenCV`, CNN-based object detection (e.g. YOLO)
- Embedded / IoT: `Arduino UNO`, sensors (SW-420, microphones, ultrasonic, etc.)
- Communication: `GSM`, `MQTT`, REST APIs
- Data: CSV/relational DB for accident and sensor data
- Tools: Jupyter Notebook, Google Colab, GitHub

  ## 🛠️ Installation & Dependencies

This project requires **Python 3.x** and the following libraries to run the Object Detection module:

* **OpenCV**: Used for real-time computer vision and image processing.
* **NumPy**: Used for mathematical operations on frame arrays.
* **Time**: Standard library for handling frame delays and camera stabilization.

### **How to Install**
Run the following command in your terminal or command prompt:
```bash
pip install opencv-python numpy

---

## 🏗️ High-Level Architecture
![System Architecture](architecture_diagram.png)

1. **Data & Sensing Layer**
   - Track sensors (vibration + sound)
   - Road-rail level-crossing sensors & cameras
   - Railway operational and accident databases

2. **Edge Processing Layer**
   - Embedded microcontrollers (Arduino) for local threshold detection  
   - Edge devices (e.g. Raspberry Pi / Jetson) for computer vision models

3. **AI & Analytics Layer**
   - ML models for:
     - Accident risk prediction
     - Obstacle detection
     - Track anomaly detection
   - Risk scoring and alert generation

4. **Application & Interface Layer**
   - Web / mobile dashboards for:
     - Control-room operators
     - Maintenance engineers
   - Mobile alerts to train drivers and relevant officers

5. **Integration & Communication Layer**
   - APIs / message queues to connect modules
   - Logs and monitoring for later analysis

---

## 🔍 How the System Works (End-to-End Flow)

1. **Sense**
   - Sensors and cameras continuously monitor tracks, crossings and operating conditions.

2. **Detect**
   - Local algorithms detect anomalies:
     - Obstacles at crossings
     - Track vibration/sound patterns
     - Historical risk on specific segments

3. **Predict**
   - AI models calculate:
     - Probability of an accident
     - Time-to-collision (for trains near crossings)
     - Risk level of each track segment

4. **Alert & Act**
   - Automatic actions:
     - Close/open barriers
     - Trigger lights and sirens
   - Notifications:
     - SMS / app alerts to train drivers and control centres

5. **Learn & Improve**
   - New incidents and sensor readings are stored
   - Models are retrained to improve accuracy over time

---

## 📈 Key Expected Outcomes

- Reduction of collisions at level crossings  
- Early detection of track defects before derailments  
- Better identification of **blind spots** in the network  
- Data-driven decisions for:
  - Maintenance scheduling
  - Speed restrictions
  - Infrastructure investment
- A prototype that is:
  - **Cost-effective**
  - **Scalable**
  - Suitable for **Sri Lankan** railway conditions

---

## 🚀 Future Enhancements

- Integration with **national railway control systems** (SLR)  
- Cloud-based analytics dashboard with live maps  
- Use of **satellite imagery** and **drones** for track inspection  
- More advanced models (LSTM / GNNs) for spatio-temporal risk prediction  
- Public API for researchers and policy-makers

---

## 👥 Group Details

| Name                | Student ID  | Email                           | GitHub Username | Role        |
|---------------------|------------|---------------------------------|-----------------|------------|
| Fernando W.P.N.S    | IT22325778 | it22325778@my.sliit.lk         | Nipun Shehara  | ⭐ Leader   |
| Ekanayaka E.M.L.M   | IT22897558 | it22897558@my.sliit.lk         |LashanMEkanayaka   | 👨‍💻 Member |
| Vithanachchi N.Y    | IT22285560 | it22285560@my.sliit.lk         | it22285560   | 👩‍💻 Member |
| Pramodya W.S.C      | IT22026170 | it22026170@my.sliit.lk         | it22026170chathuri   | 👨‍💻 Member |

> 🔁 _Update the GitHub usernames and emails if they are different._

---

## 🌍 Vision Statement

> “To build an intelligent, affordable and scalable safety framework that  
> transforms Sri Lankan railways into a **data-driven, accident-aware** transport  
> system, protecting human life, wildlife and national assets.”

---

## 🏆 Tagline

**RailSafeSL – Predicting Danger, Protecting Lives.**
