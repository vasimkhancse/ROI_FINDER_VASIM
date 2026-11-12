"""
Keyboard Event Handler Module
Processes keyboard shortcuts (C, R, Q) in the live video window.
"""
from modules.state import app_state
from modules.close_window import close_video_window


def handle_key(event):
    """
    Handle key events:
      - 'c': Print current 4 coordinates to console
      - 'r': Reset/clear selected coordinates
      - 'q': Close the video window
    """
    key = event.keysym.lower()

    # Press C - Print coordinates
    if key == "c":
        if len(app_state.coordinates) == 4:
            print("Coordinates:", app_state.coordinates)
        else:
            print("Please select 4 points first!")

    # Press R - Reset coordinates
    elif key == "r":
        app_state.coordinates.clear()
        print("Coordinates removed successfully!")

    # Press Q - Close current video window
    elif key == "q":
        print("Closing CCTV window...")
        close_video_window()

