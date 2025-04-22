import tkinter as tk
import requests

def fetch_data(endpoint):
    try:
        response = requests.get(f"http://127.0.0.1:8000{endpoint}")
        if response.status_code == 200:
            output_label.config(text=response.json())
        else:
            output_label.config(text=f"Error: {response.status_code}")
    except Exception as e:
        output_label.config(text=f"Error: {e}")

# Set up the GUI window
root = tk.Tk()
root.title("FastAPI GUI Integration")

# Buttons for API endpoints
btn_root = tk.Button(root, text="Call /", command=lambda: fetch_data("/"))
btn_cinthiya = tk.Button(root, text="Call /cinthiya", command=lambda: fetch_data("/cinthiyae"))

btn_root.pack(pady=10)
btn_cinthiya.pack(pady=10)

# Label to display API response
output_label = tk.Label(root, text="", wraplength=300, justify="left")
output_label.pack(pady=20)

root.mainloop()
