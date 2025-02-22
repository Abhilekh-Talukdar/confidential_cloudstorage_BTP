import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class FileCoderApp:
    def __init__(self, master):
        self.master = master
        master.title("File Encoder/Decoder")

        self.input_file_path = tk.StringVar()
        self.operation_type = tk.StringVar(value="encode") # Default to encode

        # --- Input File Frame ---
        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Input File:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.input_entry = tk.Entry(input_frame, textvariable=self.input_file_path, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)
        self.browse_button = tk.Button(input_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        # --- Operation Type Frame ---
        operation_frame = tk.Frame(master)
        operation_frame.pack(pady=5)

        tk.Radiobutton(operation_frame, text="Encode", variable=self.operation_type, value="encode").pack(side=tk.LEFT)
        tk.Radiobutton(operation_frame, text="Decode", variable=self.operation_type, value="decode").pack(side=tk.LEFT)

        # --- Action Buttons Frame ---
        action_frame = tk.Frame(master)
        action_frame.pack(pady=10)

        self.encode_button = tk.Button(action_frame, text="Encode File", command=self.encode_file)
        self.encode_button.pack(side=tk.LEFT, padx=10)
        self.decode_button = tk.Button(action_frame, text="Decode File", command=self.decode_file)
        self.decode_button.pack(side=tk.LEFT, padx=10)

        # --- Status Output Frame ---
        status_frame = tk.Frame(master)
        status_frame.pack(pady=10)

        tk.Label(status_frame, text="Status:").pack(side=tk.LEFT, anchor="nw")
        self.status_text = tk.Text(status_frame, height=5, width=60, state=tk.DISABLED) # Disabled for display only
        self.status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.status_scrollbar = tk.Scrollbar(status_frame, command=self.status_text.yview)
        self.status_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.status_text.config(yscrollcommand=self.status_scrollbar.set)

        self.clear_button = tk.Button(status_frame, text="Clear Status", command=self.clear_status)
        self.clear_button.pack(side=tk.BOTTOM, anchor="se", pady=5)


    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
        if filename:
            self.input_file_path.set(filename)

    def encode_file(self):
        input_file = self.input_file_path.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return

        if not os.path.exists(input_file):
            messagebox.showerror("Error", "Input file not found.")
            return

        self.update_status("Encoding in progress...")
        try:
            process_result = subprocess.run(['python', 'encode.py', input_file], capture_output=True, text=True)
            if process_result.returncode == 0:
                output_message = process_result.stdout.strip() # Get output from encode.py
                self.update_status(f"Encoding successful.\n{output_message}")
            else:
                error_message = process_result.stderr.strip() # Get error output from encode.py
                self.update_status(f"Encoding failed.\nError: {error_message}")
                messagebox.showerror("Encoding Error", f"Encoding process failed. See status for details.")
        except Exception as e:
            self.update_status(f"Error executing encode.py: {e}")
            messagebox.showerror("Application Error", f"An error occurred while running encode.py: {e}")

    def decode_file(self):
        input_file = self.input_file_path.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return

        if not os.path.exists(input_file):
            messagebox.showerror("Error", "Input file not found.")
            return

        self.update_status("Decoding in progress...")
        try:
            process_result = subprocess.run(['python', 'decode.py', input_file], capture_output=True, text=True)
            if process_result.returncode == 0:
                output_message = process_result.stdout.strip() # Get output from decode.py
                self.update_status(f"Decoding successful.\n{output_message}")
            else:
                error_message = process_result.stderr.strip() # Get error output from decode.py
                self.update_status(f"Decoding failed.\nError: {error_message}")
                messagebox.showerror("Decoding Error", f"Decoding process failed. See status for details.")
        except Exception as e:
            self.update_status(f"Error executing decode.py: {e}")
            messagebox.showerror("Application Error", f"An error occurred while running decode.py: {e}")


    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL) # Enable text widget to modify
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.config(state=tk.DISABLED) # Disable again to prevent direct editing
        self.status_text.see(tk.END) # Scroll to the bottom

    def clear_status(self):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END) # Clear all text
        self.status_text.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()
    app = FileCoderApp(root)
    root.mainloop()