import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd


def create_table(frame):
    # Create Treeview Frame
    tree_frame = tk.Frame(frame)
    tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Create Treeview Scrollbar
    scrollbar = ttk.Scrollbar(tree_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create Treeview
    tree = ttk.Treeview(tree_frame, yscrollcommand=scrollbar.set)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Configure Scrollbar
    scrollbar.config(command=tree.yview)

    # Configure Treeview
    tree.config(columns=headers, show="headings")
    for col, header in enumerate(headers):
        tree.column(col, width=100, anchor="center")
        tree.heading(col, text=header)

    return tree


def update_table(tree, data):
    # Clear existing data
    tree.delete(*tree.get_children())

    # Add new data
    for row in data:
        tree.insert("", tk.END, values=row)


def open_csv_file():
    # Open file dialog to select CSV file
    file_path = askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Read CSV file
    data = pd.read_csv(file_path)

    # Update Treeview with new data
    update_table(tree, data.values.tolist())

def search_player():
    search_value = search_entry.get()
    if search_value == "":
        update_table(data)
    else:
        filtered_data = []
        for player in data:
            if search_value.lower() in player['Name'].lower():
                filtered_data.append(player)
        update_table(filtered_data)



def grade_player(row):
    # Grade player based on Overall rating
    if row["Overall"] >= 90:
        return "A+"
    elif row["Overall"] >= 80:
        return "A"
    elif row["Overall"] >= 70:
        return "B"
    elif row["Overall"] >= 60:
        return "C"
    else:
        return "D"


# Create main window
root = tk.Tk()
root.title("Football GM Helper")

# Create Frame
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Create Treeview Headers
headers = ["Name", "Team", "Position", "Overall", "Grade"]

# Create Treeview
tree = create_table(frame)

# Create Open File Button
open_file_button = tk.Button(root, text="Open CSV File", command=open_csv_file)
open_file_button.pack(pady=10)

# Create Search Frame
search_frame = tk.Frame(root)
search_frame.pack()

# Create Search Label
search_label = tk.Label(search_frame, text="Search:")
search_label.pack(side=tk.LEFT)

# Create Search Entry
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

# Create Search Button
search_button = tk.Button(search_frame, text="Search", command=search_player)
search_button.pack(side=tk.LEFT)

# Load initial data
data = pd.read_csv("PlayerRatings.csv")
update_table(tree, data.values.tolist())

root.mainloop()
