"""
Camera Connection Module
Connects to an RTSP video stream and initializes the live video window.
"""
import cv2
import tkinter as tk
from tkinter import messagebox
from modules.state import app_state
from modules.on_click import on_click
from modules.handle_key import handle_key
from modules.reset_points import reset_points
from modules.close_window import close_video_window
from modules.update_frame import update_frame


def connect_camera():
    """
    Connect to RTSP camera stream and display live video in a new window.
    Binds mouse clicks for ROI selection and keyboard controls.
    """
    if app_state.url_entry is None:
        return

    url = app_state.url_entry.get().strip()

    if not url:
        messagebox.showwarning(
            "Warning",
            "Please enter RTSP URL"
        )
        return

    # Release existing capture if already open
    if app_state.cap is not None:
        app_state.cap.release()
        app_state.cap = None

    # Connect to RTSP feed (supports numeric camera indices or video paths/URLs)
    source = int(url) if url.isdigit() else url
    test_cap = cv2.VideoCapture(source, cv2.CAP_FFMPEG)

    if not test_cap.isOpened():
        test_cap.release()
        messagebox.showerror(
            "Connection Error",
            "Invalid RTSP URL or camera unavailable"
        )
        return

    ret, frame = test_cap.read()

    if not ret:
        test_cap.release()
        messagebox.showerror(
            "Connection Error",
            "Unable to receive video"
        )
        return

    app_state.cap = test_cap
    app_state.coordinates.clear()
    app_state.running = True

    # Create live video window
    video_window = tk.Toplevel(app_state.root)
    video_window.title("CCTV Live Video")
    video_window.geometry("850x550")

    video_label = tk.Label(video_window, bg="black")
    video_label.pack(pady=10)

    # Bind events
    video_label.bind("<Button-1>", on_click)
    video_window.bind("<Key>", handle_key)
    video_window.focus_force()

    tk.Button(
        video_window,
        text="Reset Points",
        command=reset_points
    ).pack(pady=5)

    video_window.protocol(
        "WM_DELETE_WINDOW",
        close_video_window
    )

    app_state.video_window = video_window
    app_state.video_label = video_label

    update_frame()

