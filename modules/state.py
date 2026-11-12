"""
Application State Management
Stores shared runtime state across modules for GUI components,
video capture, and ROI coordinates.
"""
from typing import List, Optional
import cv2
import tkinter as tk


class AppState:
    """
    Central shared state across all modules.
    Ensures all functions operate on the same data and GUI references.
    """
    def __init__(self):
        # Root window & input widgets
        self.root: Optional[tk.Tk] = None
        self.url_entry: Optional[tk.Entry] = None

        # OpenCV Video Capture
        self.cap: Optional[cv2.VideoCapture] = None

        # Coordinates for 4-point polygon: list of [x, y]
        self.coordinates: List[List[int]] = []

        # Video stream status
        self.running: bool = False

        # Live video Toplevel window & label
        self.video_window: Optional[tk.Toplevel] = None
        self.video_label: Optional[tk.Label] = None


# Global singleton instance used across all modules
app_state = AppState()

