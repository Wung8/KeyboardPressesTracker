import tkinter as tk
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

# Window dimensions
window_width = 200
window_height = 100

# Calculate position to center window at the top of the screen
x_position = (screen_width - window_width) // 2
y_position = 0

# Set window geometry
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Initial number
number = 0

# Create a label to display the number with white text
label = tk.Label(root, text=str(number), font=("Helvetica", 48), fg="white", bg="black")
label.pack(expand=True)

def update_number():
    global number
    number += 1  # Increment the number
    label.config(text=str(number))  # Update the label with the new number

def on_press(key):
    update_number()

def on_move(x, y):
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
