import tkinter as tk
import socket
import threading

# Function to receive temperature data from the server
def receive_temperature():
    while True:
        temperature = client_socket.recv(1024).decode()
        if not temperature:
            break
        temperature_label.config(text=f"Temperature from Server: {temperature}")

# Function to connect to the server
def connect_to_server():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('169.254.187.42', 8080))  # Replace with your server's IP and port
        threading.Thread(target=receive_temperature, daemon=True).start()
    except Exception as e:
        print("Error connecting to server:", e)

# GUI Setup
root = tk.Tk()
root.title("Temperature Display")
root.geometry("400x200")  # Adjust the dimensions here

temperature_label = tk.Label(root, text="Waiting for temperature data...", font=("Helvetica", 14))
temperature_label.pack(pady=20)

connect_button = tk.Button(root, text="Connect to Server", command=connect_to_server, font=("Helvetica", 12))
connect_button.pack()

root.mainloop()
