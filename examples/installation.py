import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import threading

# Get the folder of this installer
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to install dependencies with a progress bar
def install_dependencies(progress_bar):
    try:
        dependencies = ["numpy", "pyglet"]
        total = len(dependencies)

        for i, dep in enumerate(dependencies, start=1):
            progress_bar['value'] = (i-1)/total*100
            root.update_idletasks()
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

        progress_bar['value'] = 100
        root.update_idletasks()
        messagebox.showinfo("Success", "Dependencies installed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to install dependencies:\n{e}")

# Run installation in a separate thread to keep GUI responsive
def run_installation():
    threading.Thread(target=install_dependencies, args=(progress,)).start()

# Function to detect demos in the folder
def detect_demos():
    demos = []
    for file in os.listdir(SCRIPT_DIR):
        if file.endswith(".py") and file.lower() != "installer.py":
            demos.append(file)
    return demos

# Function to run a selected demo
def run_demo(demo_file):
    demo_path = os.path.join(SCRIPT_DIR, demo_file)
    if os.path.exists(demo_path):
        subprocess.Popen([sys.executable, demo_path], cwd=SCRIPT_DIR)
    else:
        messagebox.showerror("Error", f"{demo_file} not found!")

# Tkinter GUI
root = tk.Tk()
root.title("X++ API Installer & Launcher")
root.geometry("450x350")

tk.Label(root, text="Welcome to X++ API Installer", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Install dependencies and run demos easily.", font=("Arial", 10)).pack(pady=5)

# Install button + progress bar
install_btn = tk.Button(root, text="Install Dependencies", command=run_installation, width=35, height=2)
install_btn.pack(pady=10)

progress = ttk.Progressbar(root, orient='horizontal', length=350, mode='determinate')
progress.pack(pady=5)

# List detected demos
tk.Label(root, text="Available Demos:", font=("Arial", 12)).pack(pady=10)
demo_frame = tk.Frame(root)
demo_frame.pack()

demos = detect_demos()
for demo_file in demos:
    btn = tk.Button(demo_frame, text=demo_file.replace(".py",""), width=30, height=2,
                    command=lambda f=demo_file: run_demo(f))
    btn.pack(pady=3)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.quit, width=35, height=2)
exit_btn.pack(pady=10)

root.mainloop()
