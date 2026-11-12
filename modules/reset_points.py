"""
Reset Points Module
Handles clearing any selected ROI coordinates.
"""
from modules.state import app_state


def reset_points():
    """
    Reset selected ROI points and clear the polygon.
    """
    app_state.coordinates.clear()
    print("Points reset successfully")

