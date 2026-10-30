import os
import sys
import warnings
import webbrowser
from threading import Timer

# Suppress TensorFlow and Protobuf warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings("ignore")

import cv2
import mediapipe as mp
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

# Initialize MediaPipe for backend stream mode
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils

TIP_IDS = [4, 8, 12, 16, 20]

def fingers_up(lm):
    fingers = []
    fingers.append(1 if lm[TIP_IDS[0]].x < lm[TIP_IDS[0] - 1].x else 0)
    for i in range(1, 5):
        fingers.append(1 if lm[TIP_IDS[i]].y < lm[TIP_IDS[i] - 2].y else 0)
    return fingers

def gesture(f):
    total = sum(f)
    if total == 0: return "Fist", "✊"
    if total == 5: return "Open Palm", "✋"
    if f == [0, 1, 0, 0, 0]: return "Point", "☝️"
    if f == [0, 1, 1, 0, 0]: return "Peace", "✌️"
    if f == [1, 0, 0, 0, 0]: return "Thumbs Up/Side", "👍"
    if f == [0, 1, 0, 0, 1]: return "Rock On", "🤘"
    if f == [1, 1, 0, 0, 1]: return "I Love You", "🤟"
    if f == [0, 1, 1, 1, 0]: return "Three", "3️⃣"
    if f == [0, 1, 1, 1, 1]: return "Four", "4️⃣"
    return f"Custom {f}", "🖐️"

current_gesture_data = {
    "gesture": "None",
    "emoji": "👋",
    "fingers": [0, 0, 0, 0, 0],
    "active": False
}

def generate_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Backend Camera Error: Could not open webcam.")
        return

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = hands.process(rgb)
            
            if res.multi_hand_landmarks:
                for hand in res.multi_hand_landmarks:
                    draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                    f = fingers_up(hand.landmark)
                    g_name, g_emoji = gesture(f)
                    current_gesture_data["gesture"] = g_name
                    current_gesture_data["emoji"] = g_emoji
                    current_gesture_data["fingers"] = f
                    current_gesture_data["active"] = True
                    cv2.putText(frame, f"{g_name}", (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 120), 2)
            else:
                current_gesture_data["active"] = False

            ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            if not ret:
                continue
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    finally:
        cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
@app.route('/download/report')
def download_report():
    from flask import send_from_directory
    return send_from_directory('.', 'INDUSTRIAL_TRAINING_PROJECT_REPORT_MD_MUDASSIR_ALI.docx', as_attachment=True)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/status')
def api_status():
    return jsonify({
        "status": "online",
        "backend": "MediaPipe + OpenCV",
        "current_gesture": current_gesture_data
    })

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    print("=" * 60)
    print("Hand Gesture Recognition Web Server Starting...")
    print("Web App URL: http://127.0.0.1:5000")
    print("=" * 60)
    Timer(1.5, open_browser).start()
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)

