import tkinter as tk
from PIL import Image, ImageTk
from app import listen, handle_command

# Function to start listening
def start_listening():
    command = listen()
    if command:
        stop = handle_command(command)
        if stop:
            window.quit()

# Create the main window
window = tk.Tk()
window.title("AI Voice Assistant")
window.geometry("700x500")
window.configure(bg="#1F2833")  # dark them

# Load and display logo
logo_path = r"C:\Users\Arunehh\Desktop\voiceassistant\image4.jpg"  # Replace with your correct path

try:
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(window, image=logo_photo, bg="#1F2833")
    logo_label.image = logo_photo  # Keep reference
    logo_label.pack(pady=(20, 10))
    window.iconphoto(True, logo_photo)
except Exception as e:
    print(f"Logo loading error: {e}")

# Main Title
title_label = tk.Label(
    window,
    text="AI Voice Assistant",
    font=("Arial Rounded MT Bold", 24, "bold"),
    bg="#1F2833",
    fg="#66FCF1"
)
title_label.pack(pady=10)

# Instruction Label
instruction = tk.Label(
    window,
    text="Click the button below to talk",
    font=("Segoe UI", 12),
    bg="#1F2833",
    fg="#C5C6C7"
)
instruction.pack(pady=5)

# Button Style
def on_enter(e):
    listen_button['bg'] = "#45A29E"

def on_leave(e):
    listen_button['bg'] = "#66FCF1"

listen_button = tk.Button(
    window,
    text="Start Listening 🎙️",
    command=start_listening,
    font=("Segoe UI", 14, "bold"),
    bg="#66FCF1",
    fg="#0B0C10",
    padx=20,
    pady=10,
    bd=0,
    relief="flat",
    activebackground="#45A29E",
    activeforeground="#0B0C10",
    cursor="hand2"
)

listen_button.bind("<Enter>", on_enter)
listen_button.bind("<Leave>", on_leave)
listen_button.pack(pady=25)

# Footer Label
footer = tk.Label(
    window,
    text="Created by Poornima 💻",
    font=("Courier New", 10),
    bg="#1F2833",
    fg="#C5C6C7"
)
footer.pack(side="bottom", pady=20)

# Run the GUI
window.mainloop()

