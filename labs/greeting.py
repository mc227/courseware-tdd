"""
greeting.py
"""
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def display_gif(gif_path):
    """function or method docstring"""
    root = tk.Tk()
    root.title("GIF Display")

    # Load the GIF using PIL
    gif = Image.open(gif_path)
    gif_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif)]

    # Create a label to display the GIF
    label = tk.Label(root)
    label.pack()

    def update_frame(frame_num):
        # Update the label with the current frame
        label.config(image=gif_frames[frame_num])
        root.after(100, update_frame, (frame_num + 1) % len(gif_frames))

    # Start updating frames
    update_frame(0)

    root.mainloop()

def greet(name):
    """
    insert function docstring
    """
    return "Oh Hi, " + name

def main():
    """function or method docstring"""
    print(greet("Mark"))

    # Add GIF display functionality
    gif_path = "OhHiMark.gif"  # Replace with the path to your GIF
    display_gif(gif_path)

if __name__ == "__main__":
    main()

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
