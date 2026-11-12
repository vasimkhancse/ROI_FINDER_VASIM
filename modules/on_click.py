"""
Mouse Event Handler Module
Tracks mouse clicks on the video feed to record ROI boundary points.
"""
from modules.state import app_state


def on_click(event):
    """
    Handle mouse click events on the live video stream label.
    Collects up to 4 points to form a polygon. If 4 points already exist,
    starts a new polygon.
    """
    # After four points, start a new polygon
    if len(app_state.coordinates) == 4:
        app_state.coordinates.clear()

    app_state.coordinates.append([event.x, event.y])

    print(f"P{len(app_state.coordinates)} selected: {[event.x, event.y]}")

    if len(app_state.coordinates) == 4:
        print("Polygon completed! Press C to print coordinates.")

