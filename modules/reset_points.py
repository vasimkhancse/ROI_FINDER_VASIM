"""
Reset Points Module
Handles clearing any selected ROI coordinates and area.
"""
from modules.state import app_state


def reset_points():
    """
    Reset selected ROI points and area.
    """
    app_state.coordinates.clear()
    app_state.area = None
    print("Points reset successfully")

