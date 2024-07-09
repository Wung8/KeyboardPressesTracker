import tkinter as tk
from tkinter import font
from pynput import keyboard, mouse
import screeninfo

file = 'number.txt'

# Load the number from the file
def load_number():
    try:
        with open(file, "r") as f:
            return int(f.read())
    except:
        return 0

# Save the number to the file
def save_number(number):
    with open(file, "w") as f:
        f.write(str(number))

# Initial number
number = load_number()

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
    save_number(number)  # Save the updated number to the file

pressed_keys = set()

def on_key_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        update_number()

def on_key_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def on_click(x, y, button, pressed):
    if pressed:
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
keyboard_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
keyboard_listener.start()

# Set up the global mouse listener
mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)
mouse_listener.start()

# Run the Tkinter event loop
root.mainloop()
