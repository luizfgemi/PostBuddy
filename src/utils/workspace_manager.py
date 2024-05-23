import json
from tkinter import filedialog, messagebox

def save_workspace(environment_variables):
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(environment_variables, file)
        messagebox.showinfo("Save Workspace", "Workspace saved successfully!")

def load_workspace():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}
