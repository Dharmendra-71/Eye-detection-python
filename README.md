# Eye-detection-python
Eye-controlled interface using OpenCV and ESP32-CAM. This project tracks eye movement using a webcam and sends directional commands (UP, DOWN, or STOP) to an ESP32-CAM over Wi-Fi.

eye_control.py.py # Main Python script to run eye detection and send commands

csharp
Copy
Edit

## 🔌 Circuit & ESP32 Setup

Make sure your ESP32 is running a web server that listens for commands via URL parameters, like:

http://<ESP32_IP>/control?dir=up
http://<ESP32_IP>/control?dir=down
http://<ESP32_IP>/control?dir=stop

bash
Copy
Edit

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eye-controlled-esp32.git
   cd eye-controlled-esp32
Install dependencies:

bash
Copy
Edit
pip install opencv-python requests
Update your ESP32 IP address in the script:

python
Copy
Edit
ESP32_CONTROL_IP = "http://<your-esp32-ip>/control"
Run the script:

bash
Copy
Edit
python eye_control.py.py
Press q to quit.

🧠 How It Works
The camera captures video in real-time.

Haar cascades detect eyes.

The system calculates the center Y-coordinate of the first detected eye.

If the eye moves up or down beyond a threshold, a corresponding command is sent to the ESP32.

📌 Notes
Only the first detected eye is used for control to reduce noise.

Adjust the EYE_POSITION_Y_TARGET and threshold (±20) as needed for your environment.

📜 License
This project is open-source and available under the MIT License.

🤝 Contributions
Feel free to fork the repo, improve it, and send pull requests!

👤 Author
Made with ❤️ by Dharmendra
