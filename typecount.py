import tkinter as tk
from tkinter import font
from pynput import keyboard, mouse
import screeninfo

# Create the main window
root = tk.Tk()
root.title("Number Display")

# Remove window border and background
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="black")

# Get screen width and height
screen = screeninfo.get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

# Initial number
number = 0

# Create a label to display the number with white text
label = tk.Label(root, text=str(number), font=("Helvetica", 28), fg="white", bg="black")
label.pack(expand=True)

# Measure the width of the text and adjust window size accordingly
def adjust_window_size():
    text_width = font.Font(font=("Helvetica", 28)).measure(str(number))
    window_width = max(text_width + 20, 200)  # Add some padding
    window_height = 50
    x_position = (screen_width - window_width) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+0")

# Initial adjustment of window size
adjust_window_size()

def update_number():
    global number
    number += 1  # Increment the number
    label.config(text=str(number))  # Update the label with the new number
    adjust_window_size()  # Adjust window size based on new number

def on_press(key):
    update_number()

def on_move(x, y):
    x_position = root.winfo_x()
    y_position = root.winfo_y()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    # Check if the cursor is within the window's area
    if x_position <= x <= x_position + window_width and y_position <= y <= y_position + window_height:
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window

# Set up the global key listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Set up the global mouse listener
mouse_listener = mouse.Listener(on_move=on_move)
mouse_listener.start()

# Run the Tkinter event loop
root.mainloop()
