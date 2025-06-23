# ESP32-CAM Eye Detection using OpenCV (run on PC, sends command wirelessly)

import cv2
import requests  # HTTP requests to ESP32

# === CONFIG ===
ESP32_CONTROL_IP = "http://192.168.1.50/control"  # Replace with your ESP32's IP
EYE_POSITION_Y_TARGET = 240  # Reference Y level (tweak as needed)

# Load Haar Cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start camera
cap = cv2.VideoCapture(0)
last_command = "STOP"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    command = "STOP"
    for (x, y, w, h) in eyes:
        center_y = y + h // 2
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.line(frame, (0, EYE_POSITION_Y_TARGET), (frame.shape[1], EYE_POSITION_Y_TARGET), (0, 0, 255), 2)

        if center_y < EYE_POSITION_Y_TARGET - 20:
            command = "UP"
        elif center_y > EYE_POSITION_Y_TARGET + 20:
            command = "DOWN"
        else:
            command = "STOP"
        break  # Use only the first detected eye

    if command != last_command:
        print(f"Sending command: {command}")
        try:
            requests.get(f"{ESP32_CONTROL_IP}?dir={command.lower()}")
        except:
            print("Failed to send command")
        last_command = command

    cv2.imshow('Eye Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
