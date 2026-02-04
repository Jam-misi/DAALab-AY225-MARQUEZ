import os
import csv
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# Sorting Algorithms (Cancelable + Order)
# ==========================

def should_swap(a, b, ascending):
    return a > b if ascending else a < b

def bubble_sort(data, key_index, ascending, cancel_flag):
    n = len(data)
    for i in range(n):
        if cancel_flag():
            return None
        for j in range(0, n - i - 1):
            if should_swap(data[j][key_index], data[j + 1][key_index], ascending):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def insertion_sort(data, key_index, ascending, cancel_flag):
    for i in range(1, len(data)):
        if cancel_flag():
            return None
        key_item = data[i]
        j = i - 1
        while j >= 0 and should_swap(data[j][key_index], key_item[key_index], ascending):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
    return data

def merge_sort(data, key_index, ascending, cancel_flag):
    if cancel_flag():
        return None
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid], key_index, ascending, cancel_flag)
    right = merge_sort(data[mid:], key_index, ascending, cancel_flag)

    if left is None or right is None:
        return None

    return merge(left, right, key_index, ascending, cancel_flag)

def merge(left, right, key_index, ascending, cancel_flag):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if cancel_flag():
            return None
        if should_swap(right[j][key_index], left[i][key_index], ascending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ==========================
# GUI Application
# ==========================

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Efficiency")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e1e2e")

        self.cancel_requested = False
        self.status_animating = False

        self.configure_style()
        self.create_widgets()

    # --------------------------
    # Styling
    # --------------------------

    def configure_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#1e1e2e")
        style.configure("TLabel", background="#1e1e2e", foreground="#ffffff", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

        style.configure("TButton",
                        background="#5a4fcf",
                        foreground="white",
                        font=("Segoe UI", 10),
                        padding=6)

        style.map("TButton",
                  background=[("active", "#7b6dff")])

        style.configure("TCombobox", padding=4)
        style.configure("TEntry", padding=4)

        style.configure("Horizontal.TProgressbar",
                        troughcolor="#2e2e42",
                        background="#7b6dff")

    # --------------------------
    # Widgets
    # --------------------------

    def create_widgets(self):
        header = ttk.Label(self.root, text="Sorting Algorithm Tool",
                           style="Header.TLabel")
        header.pack(pady=10)

        frame = ttk.Frame(self.root, padding=15)
        frame.pack(fill="x", padx=20)

        ttk.Label(frame, text="Sorting Algorithm").grid(row=0, column=0, sticky="w")
        self.algorithm = ttk.Combobox(frame, values=["Bubble Sort", "Insertion Sort", "Merge Sort"])
        self.algorithm.current(2)
        self.algorithm.grid(row=0, column=1, padx=10)

        ttk.Label(frame, text="Sort Column").grid(row=1, column=0, sticky="w")
        self.column = ttk.Combobox(frame, values=["ID", "FirstName", "LastName"])
        self.column.current(0)
        self.column.grid(row=1, column=1, padx=10)

        ttk.Label(frame, text="Sort Order").grid(row=2, column=0, sticky="w")
        self.order = ttk.Combobox(frame, values=["Ascending", "Descending"])
        self.order.current(0)
        self.order.grid(row=2, column=1, padx=10)

        ttk.Label(frame, text="Number of Rows (N)").grid(row=3, column=0, sticky="w")
        self.rows_entry = ttk.Entry(frame)
        self.rows_entry.insert(0, "10000")
        self.rows_entry.grid(row=3, column=1, padx=10)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.run_button = ttk.Button(btn_frame, text="▶ Run Sort", command=self.start_sort)
        self.run_button.grid(row=0, column=0, padx=10)

        self.cancel_button = ttk.Button(btn_frame, text="■ Cancel", command=self.cancel_sort)
        self.cancel_button.grid(row=0, column=1, padx=10)

        self.progress = ttk.Progressbar(self.root, mode="indeterminate")
        self.progress.pack(fill="x", padx=30, pady=5)

        self.status_label = ttk.Label(self.root, text="Idle")
        self.status_label.pack()

        self.output = tk.Text(self.root, height=18, bg="#2e2e42",
                              fg="white", font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=20, pady=10)

    # --------------------------
    # Animation
    # --------------------------

    def animate_status(self):
        if not self.status_animating:
            return
        current = self.status_label.cget("text")
        self.status_label.config(text=current + ".")
        if len(current) > 12:
            self.status_label.config(text="Running")
        self.root.after(500, self.animate_status)

    # --------------------------
    # Control Logic
    # --------------------------

    def cancel_sort(self):
        self.cancel_requested = True
        self.status_label.config(text="Cancelled")
        self.output.insert(tk.END, "\n⚠ Sorting cancelled by user.\n")

    def start_sort(self):
        algo = self.algorithm.get()
        n = int(self.rows_entry.get())

        if algo in ["Bubble Sort", "Insertion Sort"] and n > 20000:
            if not messagebox.askyesno(
                "Warning",
                "O(n²) algorithm selected.\nThis may take a long time.\nContinue?"
            ):
                return

        self.cancel_requested = False
        self.status_animating = True
        self.status_label.config(text="Running")
        self.animate_status()

        self.output.delete("1.0", tk.END)
        self.progress.start()

        threading.Thread(target=self.run_sort, daemon=True).start()

    def run_sort(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, "generated_data.csv")

        try:
            load_start = time.perf_counter()
            data = []

            with open(csv_path, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for i, row in enumerate(reader):
                    if i >= int(self.rows_entry.get()):
                        break
                    data.append([int(row[0]), row[1], row[2]])

            load_time = time.perf_counter() - load_start

            col_index = {"ID": 0, "FirstName": 1, "LastName": 2}[self.column.get()]
            ascending = self.order.get() == "Ascending"
            cancel_flag = lambda: self.cancel_requested

            sort_start = time.perf_counter()

            if self.algorithm.get() == "Bubble Sort":
                result = bubble_sort(data, col_index, ascending, cancel_flag)
            elif self.algorithm.get() == "Insertion Sort":
                result = insertion_sort(data, col_index, ascending, cancel_flag)
            else:
                result = merge_sort(data, col_index, ascending, cancel_flag)

            if result is None:
                return

            sort_time = time.perf_counter() - sort_start
            self.display_results(result, load_time, sort_time)

        finally:
            self.status_animating = False
            self.progress.stop()
            self.status_label.config(text="Completed")

    def display_results(self, data, load_time, sort_time):
        self.output.insert(tk.END, f"File Load Time : {load_time:.4f} seconds\n")
        self.output.insert(tk.END, f"Sorting Time   : {sort_time:.4f} seconds\n")
        self.output.insert(tk.END, f"Total Time     : {load_time + sort_time:.4f} seconds\n\n")
        
        limit = min(100, len(data))
        self.output.insert(tk.END, "First 100 Sorted Records\n")
        self.output.insert(tk.END, "-" * 60 + "\n")

        for row in data[:100]:
            self.output.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}\n")

# ==========================
# Run App
# ==========================

if __name__ == "__main__":
    root = tk.Tk()
    SortingApp(root)
    root.mainloop()
