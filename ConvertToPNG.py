import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from PIL import Image
import os
import webbrowser

def convert_to_png(image_path):
    # Open the WEBP image
    img = Image.open(image_path)

    # Ask the user to specify the save path for the PNG file
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        # Save the image as a PNG file
        img.save(save_path, "PNG")
        # Update the result label with the success message
        label_result.config(text=f"Conversion complete: {os.path.basename(save_path)}")
    else:
        # Update the result label with the cancellation message
        label_result.config(text="Conversion cancelled")

def open_file_dialog():
    # Open a file dialog to let the user select a WEBP file
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if file_path:
        # Convert the selected file to PNG
        convert_to_png(file_path)

def show_about():
    # Display information about the program and open a GitHub link
    messagebox.showinfo("About ChangeToPNG", "ConvertToPNG Version 20240110.5\n"
                                              "Convert your WEBP images to PNG format easily.\n\n"
                                              "GitHub: https://github.com/diligencefrozen/ConvertToPNG")
    webbrowser.open("https://github.com/diligencefrozen/ConvertToPNG")

# Initialize the Tkinter window
root = tk.Tk()
root.title("ConvertToPNG")  # Set the window title

# Title icon settings: Automatically load the icon from the same directory as the script
script_dir = os.path.dirname(os.path.realpath(__file__))
icon_path = os.path.join(script_dir, "ConvertToPNG.ico")
root.iconbitmap(icon_path)  # Set the window icon

# Set the window size
root.geometry("300x200")

# Create a frame for layout
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Welcome message label
label_welcome = tk.Label(frame, text="Hello, User!\nUpload a WEBP file and \nI will convert it to PNG for you.", pady=10)
label_welcome.pack()

# Button to select an image
button_select = tk.Button(frame, text="Select a WEBP image", command=open_file_dialog)
button_select.pack()

# Label to show the result
label_result = tk.Label(frame, text="")
label_result.pack()

# Create a menu bar
menu = Menu(root)
root.config(menu=menu)

# Add a "File" menu with an "About" command
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="About", command=show_about)

# Run the Tkinter event loop
root.mainloop()
