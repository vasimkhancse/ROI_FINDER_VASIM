"""
ROI Finder Application
Entry point for the RTSP Camera Region of Interest (ROI) Finder.
"""
import tkinter as tk
from modules.state import app_state
from modules.connect_camera import connect_camera
from modules.close_window import close_app


def main():
    """
    Initialize and run the main CCTV connection window.
    """
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

    # Save references into shared state
    app_state.root = root
    app_state.url_entry = url_entry

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


if __name__ == "__main__":
    main()
