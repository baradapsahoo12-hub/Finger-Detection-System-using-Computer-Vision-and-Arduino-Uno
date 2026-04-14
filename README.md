# Finger-Detection-System-using-Computer-Vision-and-Arduino-Uno
Finger detection system using computer vision and Arduino Uno for real-time gesture recognition and hardware control.
# ✋ Finger Detection System  
Using Computer Vision & Arduino Uno

---

## 🚀 Overview

This project detects **hand gestures (finger count)** in real-time using computer vision and uses an **Arduino Uno** to control hardware based on the detected gesture.

The system processes video input, identifies the number of fingers shown, and sends commands to Arduino to perform actions such as controlling LEDs or other devices.

---

## 🎯 Objective

To build a real-time **gesture-based control system** using computer vision and hardware integration.

---

## ⚙️ How It Works

1. Webcam captures real-time video  
2. Hand region is detected using computer vision  
3. Fingers are counted using contour/convex hull analysis  
4. Based on finger count:
   - A signal is sent to Arduino  
5. Arduino performs actions such as:
   - Turning LEDs ON/OFF  
   - Controlling devices  

---

## 🧠 Technologies Used

- Python !! Supports only version 3.10 or less !!
- OpenCV (Computer Vision)  
- NumPy  
- Arduino Uno  
- Serial Communication (Python ↔ Arduino)  

---

## 📁 Project Structure


Finger-Detection-System/
│
├── finger_detection.py # Python code
├── arduino_code.ino # Arduino code
├── README.md


---

## ▶️ How to Run

### 🔹 Step 1: Install dependencies

```bash
pip install opencv-python mediapipe pyserial

```
🔹 Step 2: Upload Arduino Code
Open arduino_code.ino in Arduino IDE
Select correct COM port
Upload to Arduino Uno
🔹 Step 3: Run Python Script
python finger_detection.py
🎥 Demo Video

👉 Watch the demo here:
[https://drive.google.com/file/d/10gFJWcxmcgwXL8rO6SDrvymvLwN8tkbN/view?usp=sharing]

⚠️ Important Notes
Ensure proper lighting conditions
Background should be simple for better detection
Arduino must be connected and COM port configured correctly
💡 Features
Real-time finger detection
Gesture-based hardware control
Simple and fast processing
Arduino integration
