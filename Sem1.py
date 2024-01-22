import tkinter as tk

# Function to calculate CGPA
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

    for i in range(8):
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
window.title("2nd Sem CGPA Calculator")

# Define subject codes and credits
subject_codes = [
    "AD3251",
    "AD3271",
    "BE3251",
    "GE3251",
    "GE3271",
    "HS3251",
    "MA3251",
    "PH3256"
]

subject_credits = [3,2,3,4,2,2,4,3]

grade_labels = []
grade_entries = []

for i in range(8):
    grade_label = tk.Label(window, text=f"{subject_codes[i]} Grade:")
    grade_labels.append(grade_label)
    grade_entry = tk.Entry(window)
    grade_entries.append(grade_entry)

calculate_button = tk.Button(window, text="Calculate CGPA", command=calculate_cgpa)

# Pack GUI elements
for i in range(8):
    grade_labels[i].pack()
    grade_entries[i].pack()

calculate_button.pack()

# Start the GUI main loop
window.mainloop()

#I have planned to make this using Gradio
