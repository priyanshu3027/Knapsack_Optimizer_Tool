🧮 Fractional Knapsack Problem Solver (GUI)
This is a Python-based GUI application that solves the Fractional Knapsack Problem using a greedy algorithm. Users can input item values and weights, specify the knapsack capacity, and receive the optimal item selection (including fractions where applicable) along with a visual bar chart representation.

🚀 Features
Accepts dynamic user input for item values, weights, and knapsack capacity.

Solves the fractional knapsack problem using a greedy strategy.

Displays the maximum achievable value.

Shows item fractions selected in a clear and easy-to-understand format.

Provides a matplotlib visualization of item inclusion.

🖥️ GUI Preview
A simple, user-friendly interface built with Tkinter:

Input fields for values, weights, and capacity

A button to trigger the solver

A text box to show results

A bar chart displaying which items were selected

📦 Requirements
Make sure you have Python installed. Then install the required libraries:

bash
Copy
Edit
pip install matplotlib
🧠 How It Works
Items are sorted by value-to-weight ratio.

The knapsack is filled greedily by selecting items with the highest ratio first.

If a full item can’t fit, a fraction of it is included.

The algorithm stops when the knapsack is full.

📝 How to Use
Run the script:

bash
Copy
Edit
python knapsack_gui.py
In the GUI:

Enter item values (e.g., 60 100 120)

Enter corresponding weights (e.g., 10 20 30)

Enter the capacity of the knapsack (e.g., 50)

Click the "Solve" button

View the result:

Text output showing the max value and items included

A bar chart indicating item fractions included in the knapsack

📊 Example
Input:

Values: 60 100 120

Weights: 10 20 30

Capacity: 50

Output:

Maximum Value: 240.0

Items Taken:

(60, 10, 1.0)

(100, 20, 1.0)

(120, 30, 0.67)

A chart will display the inclusion percentage of each item.

📁 File Structure
bash
Copy
Edit
.
├── knapsack_gui.py      # Main application script
└── README.md            # This readme file
🛠️ To-Do / Enhancements (Optional)
Export results to CSV or PDF

Add input validation for non-numeric characters

Support for saving the visualization
