import cv2
import mediapipe as mp
import serial
import time

# Arduino serial port (CHANGE COM PORT)
arduino = serial.Serial('COM13', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_finger_states(hand_landmarks):
    fingers = []

    # Thumb (compare x)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (compare y)
    tips = [8, 12, 16, 20]
    dips = [6, 10, 14, 18]

    for tip, dip in zip(tips, dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            finger_states = get_finger_states(handLms)

            # Convert list to string like "10101"
            data = ''.join(map(str, finger_states))
            arduino.write(data.encode())

            print("Fingers:", data)

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()