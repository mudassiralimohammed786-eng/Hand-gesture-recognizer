# Hand Gesture Recognition AI (Web & Desktop)

Real-time hand gesture recognition system with both an ultra-fast web application and a desktop OpenCV window.

## Features
- **Modern Web Application**: Runs directly in any web browser at 60 FPS using GPU/WebAssembly acceleration.
- **Python OpenCV Desktop App**: Direct desktop window tracking.
- **Supported Gestures**:
  - Open Palm ✋
  - Fist ✊
  - Point ☝️
  - Peace ✌️
  - Thumbs Up 👍
  - Rock On 🤘
  - Custom finger patterns

## How to Run the Website

### Option 1: One-Click Launcher
Double-click [`run_website.bat`](run_website.bat). It starts the web server and automatically opens your browser at `http://localhost:5000`.

### Option 2: From Terminal
```bash
.venv\Scripts\python app.py
```
Then visit [http://localhost:5000](http://localhost:5000).

---

## How to Run Desktop OpenCV Window
Double-click [`run.bat`](run.bat) or run:
```bash
.venv\Scripts\python main.py
```
Press `q` or `Esc` to quit.
