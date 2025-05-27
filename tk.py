import tkinter as tk
from tkinter import ttk
import threading
import time
import random


# Function to simulate a long task (e.g., downloading a file)
def download_file(progress_bar, label):
    # Simulating the download process (10 seconds)
    for i in range(1, 11):
        time.sleep(1)  # Simulating a time delay for download
        progress_bar["value"] = i * 10  # Update progress bar
        label.config(text=f"Downloading... {i * 10}%")  # Update status text
        root.update_idletasks()  # Ensure the UI remains responsive

    label.config(text="Download Complete!")  # Final message


# Function to run the download in a separate thread
def start_download(progress_bar, label):
    download_thread = threading.Thread(target=download_file, args=(progress_bar, label))
    download_thread.daemon = True  # Allows the thread to close when the app closes
    download_thread.start()  # Start the download thread


# Setting up the GUI window
root = tk.Tk()
root.title("File Downloader")

# Creating a progress bar widget
progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
progress_bar.grid(row=0, column=0, padx=10, pady=10)

# Label to show download progress
label = tk.Label(root, text="Ready to Download")
label.grid(row=1, column=0, padx=10, pady=10)

# Start Button
start_button = tk.Button(
    root, text="Start Download", command=lambda: start_download(progress_bar, label)
)
start_button.grid(row=2, column=0, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
