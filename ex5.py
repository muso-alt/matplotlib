import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class DataFrameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DataFrame GUI")

        self.label = tk.Label(root, text="DataFrame", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=300, bg="white")
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Load DataFrame", command=self.load_dataframe)
        self.load_button.pack(pady=10)

        self.text = tk.Text(root, width=50, height=10)
        self.text.pack(pady=10, padx=10)

        self.sort_var = tk.BooleanVar()
        self.sort_check = tk.Checkbutton(root, text="Sort DataFrame", variable=self.sort_var)
        self.sort_check.pack()

    def load_dataframe(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                if self.sort_var.get():
                    df.sort_values(by=df.columns[0], inplace=True)
                self.display_dataframe(df)
            except Exception as e:
                messagebox.showerror("Error", f"Unable to load DataFrame: {e}")

    def display_dataframe(self, df):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, df)


if __name__ == "__main__":
    root = tk.Tk()
    app = DataFrameGUI(root)
    root.mainloop()
