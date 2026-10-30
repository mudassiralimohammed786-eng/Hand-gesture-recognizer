import os
import warnings

# Suppress TensorFlow and Protobuf warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings("ignore")

import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

TIP_IDS = [4, 8, 12, 16, 20]

def fingers_up(lm):
    fingers = []
    fingers.append(1 if lm[TIP_IDS[0]].x < lm[TIP_IDS[0]-1].x else 0)
    for i in range(1, 5):
        fingers.append(1 if lm[TIP_IDS[i]].y < lm[TIP_IDS[i]-2].y else 0)
    return fingers

def gesture(f):
    total = sum(f)
    if total == 0: return "Fist"
    if total == 5: return "Open Palm"
    if f == [0, 1, 0, 0, 0]: return "Point"
    if f == [0, 1, 1, 0, 0]: return "Peace"
    if f == [1, 0, 0, 0, 0]: return "Thumbs Up/Side"
    return f"Custom {f}"

# Try DirectShow first for fast initialization on Windows, fall back to default
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access webcam. Please check if your camera is connected and not in use by another application.")
    exit(1)

print("Starting Hand Gesture Recognition. Press 'q' or 'Esc' in the window to quit.", flush=True)

last_gesture = None

while True:
    ok, frame = cap.read()
    if not ok:
        print("Warning: Failed to read frame from camera.", flush=True)
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    if res.multi_hand_landmarks:
        for hand in res.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            f = fingers_up(hand.landmark)
            g = gesture(f)
            if g != last_gesture:
                print(f"[Live Gesture] Detected: {g}", flush=True)
                last_gesture = g
            cv2.putText(frame, g, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Hand Gesture Recognition", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
