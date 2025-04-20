import tkinter as tk
from tkinter import messagebox

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = sorted(
        [(values[i], weights[i], values[i] / weights[i]) for i in range(n)],
        key=lambda x: x[2],
        reverse=True
    )

    total_value = 0.0
    fractions = []

    for value, weight, ratio in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            fractions.append((value, weight, 1.0))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            fractions.append((value, weight, round(fraction, 2)))
            break

    return total_value, fractions

def solve():
    try:
        values = list(map(int, entry_values.get().split()))
        weights = list(map(int, entry_weights.get().split()))
        capacity = float(entry_capacity.get())

        if len(values) != len(weights):
            messagebox.showerror("Input Error", "Values and Weights must have the same length.")
            return

        max_value, selected_items = fractional_knapsack(values, weights, capacity)

        result_text = f"Maximum Value: {round(max_value, 2)}\n\nItems taken (value, weight, fraction):\n"
        for val, wt, frac in selected_items:
            result_text += f"Value: {val}, Weight: {wt}, Fraction: {frac}\n"

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Fractional Knapsack Problem Solver")

tk.Label(root, text="Enter Values (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_values = tk.Entry(root, width=40)
entry_values.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Weights (space-separated):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_weights = tk.Entry(root, width=40)
entry_weights.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Knapsack Capacity:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_capacity = tk.Entry(root, width=20)
entry_capacity.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Button(root, text="Solve", command=solve, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Arial", 11), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()