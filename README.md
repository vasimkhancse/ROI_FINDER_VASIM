# 🎯 ROI Finder (CCTV RTSP Region of Interest)

An interactive desktop application built with **Python**, **OpenCV**, and **Tkinter** to connect to RTSP CCTV camera feeds, view live video streams, and select 4-point Region of Interest (ROI) polygons with real-time visual overlays and terminal coordinate extraction.

---

## 📌 Features

- **Live RTSP Streaming:** Connect to any IP camera, CCTV NVR/DVR stream, or video feed using RTSP protocol.
- **Interactive 4-Point Selection:** Click anywhere on the live video stream to mark 4 boundary points (`P1`, `P2`, `P3`, `P4`).
- **Visual Polygon Overlay:**
  - Highlights selected vertices with labeled green circles (`P1`, `P2`, `P3`, `P4`).
  - Automatically draws yellow boundary lines between consecutive points.
  - Automatically completes and closes the polygon once the 4th point is placed.
- **Keyboard Shortcuts:**
  - `C`: Print the formatted coordinate list to the terminal.
  - `R`: Clear and reset selected points.
  - `Q`: Close the live video window.
- **Modular Architecture:** Clean separation of concerns with each function separated into its own dedicated file for readability and maintainability.
- **Graceful Resource Cleanup:** Safely releases camera streams and GUI window resources on window closure or application exit.

---

## 📁 Project Structure

```text
ROI_FINDER_VASIM/
├── main.py                  # Application entry point & main connection UI
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation and usage guide
├── .gitignore               # Git ignore rules
└── modules/                 # Modular function files
    ├── __init__.py          # Package initialization & exports
    ├── state.py             # Shared application state (singleton AppState)
    ├── connect_camera.py    # Camera connection & live window initialization
    ├── update_frame.py      # Video frame reading & polygon drawing loop
    ├── on_click.py          # Mouse click handler (point selection)
    ├── handle_key.py        # Keyboard shortcut handlers (C, R, Q)
    ├── reset_points.py      # Logic to clear selected points
    └── close_window.py      # Window closing & application exit cleanup
```

---

## 🧩 Module Breakdown

Each major function from the original monolithic file is now separated into an easy-to-read, single-purpose module:

| Module File | Primary Function | Description |
| :--- | :--- | :--- |
| `main.py` | `main()` | Launches the main RTSP URL input window. |
| `modules/state.py` | `AppState` | Centralized state container holding camera capture, coordinates, and window references. |
| `modules/connect_camera.py` | `connect_camera()` | Validates RTSP URL, verifies stream with OpenCV FFMPEG, and opens the live video window. |
| `modules/update_frame.py` | `update_frame()` | Reads frames at 30ms intervals, resizes to 800×450, draws points/lines, and updates the Tkinter canvas. |
| `modules/on_click.py` | `on_click(event)` | Captures mouse click coordinates `[x, y]` and manages the 4-point list. |
| `modules/handle_key.py` | `handle_key(event)` | Processes hotkeys (`C`, `R`, `Q`) during live viewing. |
| `modules/reset_points.py` | `reset_points()` | Clears current coordinates to start fresh. |
| `modules/close_window.py` | `close_video_window()`, `close_app()` | Releases `cv2.VideoCapture` and closes windows safely. |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher installed on your system.

### 2. Clone or Navigate to the Project
```bash
cd C:\Users\jegth\Music\ROI_FINDER_VASIM
```

### 3. (Optional) Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note for Linux users:** If `tkinter` is not installed on your system, install it via:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🚀 How to Run

Run the application using:

```bash
python main.py
```

---

## 📖 Step-by-Step Usage Guide

1. **Launch the Application:** Run `python main.py`. A window titled **"CCTV Connection"** will appear.
2. **Enter RTSP URL:** Type or paste your camera's RTSP stream URL into the input field:
   ```text
   rtsp://username:password@192.168.1.100:554/stream1
   ```
   *(Note: You can also enter `0` to test using your local webcam)*.
3. **Connect:** Click the green **"Connect"** button.
4. **Mark Points:** A live video window opens. Click 4 points in sequence (e.g., clockwise or counter-clockwise) to define your region of interest:
   - Click 1: Marks `P1`
   - Click 2: Marks `P2` and draws line `P1 -> P2`
   - Click 3: Marks `P3` and draws line `P2 -> P3`
   - Click 4: Marks `P4`, draws line `P3 -> P4`, and automatically closes `P4 -> P1`
5. **Print Coordinates:** Press `C` on your keyboard. The exact coordinates will be printed in your console.
6. **Reset / Redraw:**
   - Press `R` or click the **"Reset Points"** button to clear the points and start over.
   - Clicking again after 4 points automatically starts a new polygon.
7. **Exit:** Press `Q` or close the window to stop the stream.

---

## ⌨️ Controls & Shortcuts

| Action | Control | Description |
| :--- | :--- | :--- |
| **Mark Point** | `Left Mouse Click` | Select vertex on the video frame. |
| **Print Coordinates** | Key `C` | Prints coordinates list to terminal (requires 4 points). |
| **Reset Points** | Key `R` | Clears all marked points. |
| **Reset Button** | UI Button `Reset Points` | Clears all marked points via UI. |
| **Close Video** | Key `Q` | Closes the active CCTV live stream window. |
| **Exit Application** | Window `X` | Closes stream and quits the application cleanly. |

---

## 📋 Example Output

When 4 points are selected and you press `C`:

```text
P1 selected: [142, 98]
P2 selected: [654, 105]
P3 selected: [710, 395]
P4 selected: [120, 388]
Polygon completed! Press C to print coordinates.
Coordinates: [[142, 98], [654, 105], [710, 395], [120, 388]]
```

You can directly copy these coordinates into your computer vision models, YOLO tracking pipelines, or perimeter security scripts.

---

## 🛠️ Troubleshooting

- **"Invalid RTSP URL or camera unavailable":**
  - Verify that the IP address, port, and credentials in the RTSP URL are correct.
  - Verify network connectivity (e.g., ping the camera's IP).
  - Test the RTSP URL in a media player like VLC to verify the stream is broadcasting.
- **Latency or frame drops:**
  - The live feed is displayed with a 30ms refresh interval and resized to 800×450 for optimal performance. Ensure the camera bitrate and resolution are supported by your local network.
