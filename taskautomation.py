import os
import shutil
import re
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox


class TaskAutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Automation Tool")
        self.root.geometry("650x450")



        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10), padding=6, width=25)
        self.style.configure("TLabel", font=("Helvetica", 10))
        self.style.configure("Header.TLabel", font=("Helvetica", 14, "bold"))

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = ttk.Label(self.root, text="Select a Task", style="Header.TLabel")
        title_label.pack(pady=20)

        # Buttons for Tasks
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        ttk.Button(self.btn_frame, text="Move .jpg Files", command=self.show_move_jpg).pack(pady=5)
        ttk.Button(self.btn_frame, text="Extract Emails", command=self.show_extract_emails).pack(pady=5)
        ttk.Button(self.btn_frame, text="Scrape Webpage Title", command=self.show_scrape_title).pack(pady=5)

        # Area for Inputs
        self.input_area = ttk.Frame(self.root)
        self.input_area.pack(pady=10)

        # Output Text Box
        self.output_text = tk.Text(self.root, height=8, width=75, wrap='word', state='disabled', bg="#f4f4f4", fg="#333")
        self.output_text.pack(pady=10)

    def clear_input_area(self):
        for widget in self.input_area.winfo_children():
            widget.destroy()

    def log_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state='disabled')
        self.output_text.see(tk.END)

    # --- Task 1: Move JPG Files ---
    def show_move_jpg(self):
        self.clear_input_area()
        ttk.Label(self.input_area, text="Source Folder:").grid(row=0, column=0, sticky="w", pady=5)
        src_entry = ttk.Entry(self.input_area, width=50)
        src_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.input_area, text="Browse", command=lambda: src_entry.insert(0, filedialog.askdirectory())).grid(row=0, column=2, padx=5)

        ttk.Label(self.input_area, text="Destination Folder:").grid(row=1, column=0, sticky="w", pady=5)
        dst_entry = ttk.Entry(self.input_area, width=50)
        dst_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.input_area, text="Browse", command=lambda: dst_entry.insert(0, filedialog.askdirectory())).grid(row=1, column=2, padx=5)

        ttk.Button(self.input_area, text="Run Task", command=lambda: self.run_move_jpg(src_entry.get(), dst_entry.get())).grid(row=2, column=1, pady=10)

    def run_move_jpg(self, source, destination):
        if not os.path.exists(source):
            self.log_output("❌ Source folder does not exist.")
            return

        if not os.path.exists(destination):
            os.makedirs(destination)

        count = 0
        for filename in os.listdir(source):
            if filename.lower().endswith('.jpg'):
                src_path = os.path.join(source, filename)
                dst_path = os.path.join(destination, filename)
                shutil.move(src_path, dst_path)
                self.log_output(f"Moved: {filename}")
                count += 1

        self.log_output(f"✅ Moved {count} .jpg files.")

    # --- Task 2: Extract Emails ---
    def show_extract_emails(self):
        self.clear_input_area()
        ttk.Label(self.input_area, text="Input Text File:").grid(row=0, column=0, sticky="w", pady=5)
        in_entry = ttk.Entry(self.input_area, width=50)
        in_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.input_area, text="Browse", command=lambda: in_entry.insert(0, filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")]))).grid(row=0, column=2, padx=5)

        ttk.Label(self.input_area, text="Output Email File:").grid(row=1, column=0, sticky="w", pady=5)
        out_entry = ttk.Entry(self.input_area, width=50)
        out_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.input_area, text="Save As", command=lambda: out_entry.insert(0, filedialog.asksaveasfilename(defaultextension=".txt"))).grid(row=1, column=2, padx=5)

        ttk.Button(self.input_area, text="Run Task", command=lambda: self.run_extract_emails(in_entry.get(), out_entry.get())).grid(row=2, column=1, pady=10)

    def run_extract_emails(self, input_file, output_file):
        if not os.path.exists(input_file):
            self.log_output("❌ Input file does not exist.")
            return

        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()

            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

            with open(output_file, 'w', encoding='utf-8') as f:
                for email in emails:
                    f.write(email + '\n')

            self.log_output(f"✅ Extracted and saved {len(emails)} email(s).")
        except Exception as e:
            self.log_output(f"❌ Error extracting emails: {e}")

    # --- Task 3: Scrape Website Title ---
    def show_scrape_title(self):
        self.clear_input_area()
        ttk.Label(self.input_area, text="URL:").grid(row=0, column=0, sticky="w", pady=5)
        url_entry = ttk.Entry(self.input_area, width=50)
        url_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.input_area, text="Save Title To:").grid(row=1, column=0, sticky="w", pady=5)
        file_entry = ttk.Entry(self.input_area, width=50)
        file_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.input_area, text="Save As", command=lambda: file_entry.insert(0, filedialog.asksaveasfilename(defaultextension=".txt"))).grid(row=1, column=2, padx=5)

        ttk.Button(self.input_area, text="Run Task", command=lambda: self.run_scrape_title(url_entry.get(), file_entry.get())).grid(row=2, column=1, pady=10)

    def run_scrape_title(self, url, output_file):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No Title Found"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(title)

            self.log_output(f"✅ Page title saved: '{title}'")
        except Exception as e:
            self.log_output(f"❌ Error fetching or parsing page: {e}")


root = ThemedTk(theme="arc")  
app = TaskAutomationGUI(root)
root.mainloop()