import tkinter as tk
from tkinter import messagebox

def calculate_stock_rating():
    PE = float(pe_entry.get())
    PB = float(pb_entry.get())
    current_ratio = float(current_ratio_entry.get())
    debt_to_equity = float(debt_to_equity_entry.get())
    nifty_50 = nifty_50_var.get()

    x = 0
    if PE <= 32 and PE >= 18:
        x += 1
    if PB > 2:
        x += 1
    if current_ratio > 1:
        x += 1
    if debt_to_equity >= 2:
        x += 1
    if nifty_50:
        x += 1

    if x == 5:
        result_label.config(text="This Stock Could be a great performer.")
    elif x == 4:
        result_label.config(text="This Stock could perform well.")
    elif x == 3:
        result_label.config(text="This Stock can do well but may contain some risk.")
    elif x == 2:
        result_label.config(text="This Stock may not perform well.")
    elif x == 1:
        result_label.config(text="This Stock is too risky.")
    elif x == 0:
        result_label.config(text="You may ignore this stock for value investing.")

def check_intrensic_value():
    intrensic_value = intrensic_value_var.get()
    if intrensic_value == 1:
        intrensic_frame.pack()
    else:
        intrensic_frame.pack_forget()
        result_label.config(text="This Stock is not for value investment.")

# Create the main window
window = tk.Tk()
window.title("Stock Analysis")

# Create a frame for intrinsic value input

window.geometry("500x250")
window.minsize("500","250")
window.maxsize("500","250")

intrensic_frame = tk.Frame(window)

# Create a label and radio buttons for intrinsic value
intrensic_label = tk.Label(window, text="Is the intrinsic value less than the price of the share?")
intrensic_label.pack()
intrensic_value_var = tk.IntVar()
intrensic_yes_radio = tk.Radiobutton(window, text="Yes", variable=intrensic_value_var, value=1, command=check_intrensic_value)
intrensic_no_radio = tk.Radiobutton(window, text="No", variable=intrensic_value_var, value=0, command=check_intrensic_value)
intrensic_yes_radio.pack()
intrensic_no_radio.pack()

# Create entry widgets for stock ratios
pe_label = tk.Label(intrensic_frame, text="PE Ratio:")
pb_label = tk.Label(intrensic_frame, text="PB Ratio:")
current_ratio_label = tk.Label(intrensic_frame, text="Current Ratio:")
debt_to_equity_label = tk.Label(intrensic_frame, text="Debt To Equity Ratio:")
nifty_50_label = tk.Label(intrensic_frame, text="Is the company in Nifty 50?")

pe_entry = tk.Entry(intrensic_frame)
pb_entry = tk.Entry(intrensic_frame)
current_ratio_entry = tk.Entry(intrensic_frame)
debt_to_equity_entry = tk.Entry(intrensic_frame)
nifty_50_var = tk.BooleanVar()
nifty_50_checkbox = tk.Checkbutton(intrensic_frame, text="Yes", variable=nifty_50_var)

pe_label.grid(row=0, column=0)
pb_label.grid(row=1, column=0)
current_ratio_label.grid(row=2, column=0)
debt_to_equity_label.grid(row=3, column=0)
nifty_50_label.grid(row=4, column=0)

pe_entry.grid(row=0, column=1)
pb_entry.grid(row=1, column=1)
current_ratio_entry.grid(row=2, column=1)
debt_to_equity_entry.grid(row=3, column=1)
nifty_50_checkbox.grid(row=4, column=1)

# Create a button to calculate the stock rating
calculate_button = tk.Button(intrensic_frame, text="Calculate Stock Rating", command=calculate_stock_rating)
calculate_button.grid(row=5, columnspan=2)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
