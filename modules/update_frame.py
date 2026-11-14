"""
Frame Update and Rendering Module
Reads incoming video frames, draws points and rectangle overlays,
and renders the live frame onto the Tkinter video label.
"""
import cv2
from PIL import Image, ImageTk
from modules.state import app_state


def update_frame():
    """
    Read the next frame from the camera, render ROI points and rectangle lines,
    and update the Tkinter video label. Schedules the next frame update after 30ms.
    """
    if not app_state.running or app_state.cap is None:
        return

    ret, frame = app_state.cap.read()

    if ret:
        frame = cv2.resize(frame, (800, 450))

        # Draw selected points
        for i, (x, y) in enumerate(app_state.coordinates):
            cv2.circle(
                frame,
                (x, y),
                6,
                (0, 255, 0),
                -1
            )

            cv2.putText(
                frame,
                f"P{i+1}",
                (x + 10, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        # Draw lines between consecutive points
        for i in range(1, len(app_state.coordinates)):
            p1 = tuple(app_state.coordinates[i - 1])
            p2 = tuple(app_state.coordinates[i])

            cv2.line(
                frame,
                p1,
                p2,
                (0, 255, 255),
                2
            )

        # Close rectangle after P4 (line from P4 back to P1)
        if len(app_state.coordinates) == 4:
            cv2.line(
                frame,
                tuple(app_state.coordinates[3]),
                tuple(app_state.coordinates[0]),
                (0, 255, 255),
                2
            )

            # Display area on frame in px2
            if app_state.area is not None:
                cv2.putText(
                    frame,
                    f"Area: {app_state.area} px2",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.75,
                    (0, 255, 255),
                    2
                )

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)

        if app_state.video_label is not None:
            app_state.video_label.configure(image=photo)
            app_state.video_label.image = photo

    if app_state.running and app_state.video_window is not None:
        app_state.video_window.after(30, update_frame)

