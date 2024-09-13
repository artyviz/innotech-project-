# innotech-project-
# Sign Language Robot Assistant 🤖✋

![Sign Language Robot](https://placeholder.com/robot-image.png)

A Raspberry Pi-based robot designed to recognize sign language, speak, and serve as a helpful everyday assistant. This robot can detect hand gestures, interpret sign language, and respond in natural speech. It also allows for online searches and conversation, making it an ideal friendly companion.

---

## 📋 Features

- **Sign Language Detection**: Using a camera and machine learning, the robot detects and interprets sign language gestures.
- **Text-to-Speech**: It converts text to human-like speech and responds verbally.
- **Voice Assistant**: Capable of understanding spoken commands and engaging in conversation.
- **Online Search**: Fetches relevant information from the web based on user queries.
- **Friendly Assistant**: Works like a smart assistant, answering questions and carrying out tasks.

---



---

## 🛠️ Components

- **Raspberry Pi 4**: The brain of the robot.
- **Camera Module**: For capturing hand gestures and recognizing sign language.
- **Speakers & Microphone**: To enable the robot to speak and listen to voice commands.
- **Motors/Sensors** (Optional): For movement and additional interactivity.

---

## 🔧 Getting Started

### 1. Hardware Setup
- Install the Raspberry Pi OS and connect the **camera**, **speakers**, and **microphone**.
- Optionally, set up any additional sensors or motors if you'd like your robot to move.

### 2. Software Setup
- Clone the repository:
  ```bash
  git clone https://github.com/your-username/sign-language-robot.git
  cd sign-language-robot

### Install required dependencies:

sudo apt-get update
sudo apt-get install python3-opencv python3-speechrecognition python3-pyaudio
pip install tensorflow keras gtts google-api-python-client mediapipe

### 3. Run the Sign Language Detector
Start the gesture recognition module:
python gesture_recognition.py

### 4. Text-to-Speech Integration
Add speech responses by modifying the speech.py:
python speech.py

🧠 How It Works
Hand Gesture Recognition
Using MediaPipe and OpenCV, the robot captures real-time hand movements and identifies the specific sign language gestures.


Machine Learning Model
A custom-trained TensorFlow model is used to classify different hand gestures and interpret them as sign language commands.

Text-to-Speech
The robot converts the interpreted gesture to speech using Google TTS, allowing it to speak the meaning of the sign.

🌍 Web Search & Voice Assistant
The robot can perform searches online using Google’s Custom Search API. It can take user queries via voice commands, search the web, and respond accordingly.


🚀 Future Enhancements
Emotion Detection: Integrating facial recognition for detecting emotions and responding with empathy.
Custom Gestures: Allowing users to train the robot with new gestures.
Movement Capabilities: Adding more hardware to allow the robot to move and interact with objects.
🛠️ Technologies Used
Python: Main programming language for the robot.
OpenCV: For real-time hand gesture recognition.
TensorFlow: Machine learning library for gesture classification.
Google TTS: Text-to-speech library for verbal responses.
Google Search API: For performing web searches.
🤝 Contributions
Feel free to submit pull requests or raise issues if you'd like to contribute to this project!

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
