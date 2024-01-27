import tkinter as tk


def calculate_cgpa():
    # Define the grade points for each grade
    grade_points = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'U': 0  # Add more grades if needed
    }

    total_credits = 0
    total_weighted_grade_points = 0

    for i in range(9):
        subject_code = subject_codes[i]
        grade = grade_entries[i].get()

        if grade in grade_points:
            grade_point = grade_points[grade]
            credits = subject_credits[i]  # Retrieve credits for the subject
            weighted_grade_points = grade_point * credits
            total_credits += credits
            total_weighted_grade_points += weighted_grade_points
        else:
            result_label.config(text="Invalid grade")
            return

    # Calculate CGPA
    if total_credits > 0:
        cgpa = total_weighted_grade_points / total_credits
        display_cgpa_result(cgpa)

# Function to display CGPA result in a new window
def display_cgpa_result(cgpa):
    result_window = tk.Toplevel(window)
    result_window.title("CGPA Result")

    result_label = tk.Label(result_window, text=f"CGPA: {cgpa:.2f}", fg="green", font=("Arial", 30, "bold"))
    result_label.pack()

# Create a GUI window
window = tk.Tk()
window.title("3rd Sem CGPA Calculator")

# Define subject codes and credits
subject_codes = [
    "AD3301",
    "AD3311",
    "AD3351",
    "AD3381",
    "AD3391",
    "AL3391",
    "CS3351",
    "GE3361",
    "MA3354",
]

subject_credits = [4, 1.5, 4, 1.5, 3, 3, 4, 1, 4]

grade_labels = []
grade_entries = []

for i in range(9):
    grade_label = tk.Label(window, text=f"{subject_codes[i]} Grade:")
    grade_labels.append(grade_label)
    grade_entry = tk.Entry(window)
    grade_entries.append(grade_entry)

calculate_button = tk.Button(window, text="Calculate CGPA", command=calculate_cgpa)

# Pack GUI elements
for i in range(9):
    grade_labels[i].pack()
    grade_entries[i].pack()

calculate_button.pack()

# Start the GUI main loop
window.mainloop()
