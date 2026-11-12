"""
ROI Finder Modules Package
Provides modular functions for camera connection, frame rendering,
ROI selection, and event handling.
"""
from .state import app_state
from .connect_camera import connect_camera
from .update_frame import update_frame
from .on_click import on_click
from .handle_key import handle_key
from .reset_points import reset_points
from .close_window import close_video_window, close_app

__all__ = [
    "app_state",
    "connect_camera",
    "update_frame",
    "on_click",
    "handle_key",
    "reset_points",
    "close_video_window",
    "close_app",
]

