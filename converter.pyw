import tkinter as tk
from tkinter import messagebox
import sys

def sex(reallyrich, retardcr):
    rc = reallyrich / retardcr
    return rc

def convert():
    reallyrich_str = reallyrich1_entry.get().replace(",", "")
    try:
        reallyrich = float(reallyrich_str)
        if reallyrich < 0:
            messagebox.showerror("Error", "Please enter a valid number.")
        elif reallyrich == 0:
            messagebox.showinfo("Information", "hell naw")
        elif reallyrich > 0:
            rc = sex(reallyrich, retardcr)
            formatted_reallyrich = reallyrich_str if '.' in reallyrich_str else f"{int(reallyrich)}"
            fvariable_label.config(text=f"{formatted_reallyrich} dollars is {rc:.5f} Retarded Coin")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

retardcr = 142069

root = tk.Tk()
root.title("discord.gg/fastflags")
root.geometry("340x100")
root.resizable(False, False)

if "--resize" in sys.argv:
    root.resizable(True, True)
else:
    root.resizable(False, False)

root.geometry("340x100")

reallyrich1_label = tk.Label(root, text="Enter the amount:")
reallyrich1_label.pack()
reallyrich1_entry = tk.Entry(root)
reallyrich1_entry.pack()

music_button = tk.Button(root, text="Convert", command=convert)
music_button.pack()

fvariable_label = tk.Label(root, text="")
fvariable_label.pack()

root.mainloop()
