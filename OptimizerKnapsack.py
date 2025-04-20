import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

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

def show_plot(all_items, selected_items):
    labels = [f"Item {i+1}" for i in range(len(all_items))]

    selected_set = {(val, wt) for val, wt, _ in selected_items}

    fractions = []
    colors = []
    for item in all_items:
        if item in selected_set:
            frac = next(frac for val, wt, frac in selected_items if val == item[0] and wt == item[1])
            fractions.append(frac)
            colors.append("skyblue")
        else:
            fractions.append(0)
            colors.append("lightgray")

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, fractions, color=colors)
    plt.xlabel("Items")
    plt.ylabel("Fraction Included")
    plt.title("Item Inclusion in Knapsack")
    plt.ylim(0, 1.1)
    plt.grid(axis='y')

    # Legend for color explanation
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='skyblue', label='Selected'),
        Patch(facecolor='lightgray', label='Not Selected')
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.show()

def solve():
    try:
        values = list(map(int, entry_values.get().split()))
        weights = list(map(int, entry_weights.get().split()))
        capacity = float(entry_capacity.get())

        if len(values) != len(weights):
            messagebox.showerror("Input Error", "Values and Weights must have the same length.")
            return
        if any(v <= 0 for v in values) or any(w <= 0 for w in weights) or capacity <= 0:
            messagebox.showerror("Input Error", "Values, Weights, and Capacity must be greater than 0.")
            return

        max_value, selected_items = fractional_knapsack(values, weights, capacity)

        result_text = f"Maximum Value: {round(max_value, 2)}\n\nItems taken (value, weight, fraction):\n"
        for val, wt, frac in selected_items:
            result_text += f"Value: {val}, Weight: {wt}, Fraction: {frac}\n"

        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, result_text)
        result_textbox.config(state=tk.DISABLED)

        all_items = list(zip(values, weights))
        show_plot(all_items, selected_items)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers only.")

# GUI Setup
root = tk.Tk()
root.title("Fractional Knapsack Problem Solver")
root.geometry("600x500")

tk.Label(root, text="Enter Values (space-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_values = tk.Entry(root, width=50)
entry_values.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Weights (space-separated):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_weights = tk.Entry(root, width=50)
entry_weights.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Knapsack Capacity:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_capacity = tk.Entry(root, width=25)
entry_capacity.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Button(root, text="Solve", command=solve, bg="green", fg="white", width=20).grid(row=3, column=0, columnspan=2, pady=15)

result_textbox = tk.Text(root, width=65, height=12, wrap="word", font=("Arial", 11), fg="blue")
result_textbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_textbox.config(state=tk.DISABLED)

root.mainloop()
