import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

cap = None
coordinates = []
running = False

video_window = None
video_label = None


# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()
root.title("CCTV Connection")
root.geometry("600x200")
root.resizable(False, False)

tk.Label(
    root,
    text="Enter RTSP URL",
    font=("Arial", 12, "bold")
).pack(pady=10)

url_entry = tk.Entry(
    root,
    width=75,
    font=("Arial", 10)
)
url_entry.pack(pady=5)


# ==============================
# CONNECT CAMERA
# ==============================

def connect_camera():
    '''
    Connect to RTSP camera and display live video
    '''

    global cap, running
    global video_window, video_label

    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning(
            "Warning",
            "Please enter RTSP URL"
        )
        return

    if cap is not None:
        cap.release()
        cap = None

    test_cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

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

    cap = test_cap
    coordinates.clear()
    running = True

    video_window = tk.Toplevel(root)
    video_window.title("CCTV Live Video")
    video_window.geometry("850x550")

    video_label = tk.Label(video_window, bg="black")
    video_label.pack(pady=10)

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

    update_frame()

def handle_key(event):
    '''
    Handle key events
    '''

    global coordinates

    key = event.keysym.lower()

    # Press C - Print coordinates
    if key == "c":

        if len(coordinates) == 4:
            print("Coordinates:", coordinates)
        else:
            print("Please select 4 points first!")

    # Press R - Reset coordinates
    elif key == "r":

        coordinates.clear()
        print("Coordinates removed successfully!")

    # Press Q - Close current video window
    elif key == "q":

        print("Closing CCTV window...")
        close_video_window()

# ==============================
# SELECT POINTS
# ==============================

def on_click(event):
    '''
    Handle mouse click events
    '''

    global coordinates

    # After four points, start a new polygon
    if len(coordinates) == 4:
        coordinates.clear()

    coordinates.append([event.x, event.y])

    print(f"P{len(coordinates)} selected: {[event.x, event.y]}")

    if len(coordinates) == 4:
        print("Polygon completed! Press C to print coordinates.")


# ==============================
# DISPLAY LIVE VIDEO
# ==============================

def update_frame():
    '''
    Update live video frame
    '''

    if not running or cap is None:
        return

    ret, frame = cap.read()

    if ret:

        frame = cv2.resize(frame, (800, 450))

        # Draw selected points
        for i, (x, y) in enumerate(coordinates):

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
        for i in range(1, len(coordinates)):

            p1 = tuple(coordinates[i - 1])
            p2 = tuple(coordinates[i])

            cv2.line(
                frame,
                p1,
                p2,
                (0, 255, 255),
                2
            )

        # Close polygon after P4
        if len(coordinates) == 4:

            cv2.line(
                frame,
                tuple(coordinates[3]),
                tuple(coordinates[0]),
                (0, 255, 255),
                2
            )

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)

        video_label.configure(image=photo)
        video_label.image = photo

    if running and video_window is not None:
        video_window.after(30, update_frame)


# ==============================
# RESET POINTS
# ==============================

def reset_points():
    '''
    Reset selected points
    '''

    coordinates.clear()
    print("Points reset successfully")


# ==============================
# CLOSE VIDEO WINDOW
# ==============================

def close_video_window():
    '''
    Close current video window
    '''

    global cap, running
    global video_window, video_label

    running = False

    if cap is not None:
        cap.release()
        cap = None

    if video_window is not None:
        video_window.destroy()
        video_window = None

    video_label = None
    coordinates.clear()


# ==============================
# CLOSE APPLICATION
# ==============================

def close_app():
    '''
    Close application
    '''
    close_video_window()
    root.destroy()


tk.Button(
    root,
    text="Connect",
    command=connect_camera,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=15)

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
