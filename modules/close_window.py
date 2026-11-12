"""
Window and Application Closure Module
Handles releasing video stream resources and destroying GUI windows cleanly.
"""
from modules.state import app_state


def close_video_window():
    """
    Close the current CCTV live video window, release the camera capture,
    and reset coordinates.
    """
    app_state.running = False

    if app_state.cap is not None:
        app_state.cap.release()
        app_state.cap = None

    if app_state.video_window is not None:
        app_state.video_window.destroy()
        app_state.video_window = None

    app_state.video_label = None
    app_state.coordinates.clear()


def close_app():
    """
    Gracefully shut down the live video stream (if open) and close the main application.
    """
    close_video_window()
    if app_state.root is not None:
        app_state.root.destroy()

