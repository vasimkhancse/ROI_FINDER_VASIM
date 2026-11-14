"""
Mouse Event Handler Module
Tracks mouse clicks on the video feed to record ROI boundary points.
"""
from modules.state import app_state
from modules.calculate_area import calculate_area


def on_click(event):
    """
    Handle mouse click events on the live video stream label.
    Collects 4 points to form a rectangle.
    """
    # After four points, start a new rectangle
    if len(app_state.coordinates) == 4:
        app_state.coordinates.clear()
        app_state.area = None

    app_state.coordinates.append([event.x, event.y])

    print(f"P{len(app_state.coordinates)}: {[event.x, event.y]}")

    if len(app_state.coordinates) == 4:
        area, width, height = calculate_area(app_state.coordinates)
        app_state.area = area
        print(f"Rectangle completed! Press c to print coordinates and area ")

