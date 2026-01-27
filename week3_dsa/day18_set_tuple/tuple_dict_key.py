# TASK 4: Using tuple as dictionary key

# Dictionary to store student marks
marks = {
    ("Vinayak", "Maths"): 85,
    ("Vinayak", "Physics"): 78,
    ("Anu", "Maths"): 90
}

print("Student Marks:")
for key, value in marks.items():
    print(key, ":", value)

# Access specific value
print("\nVinayak Maths marks:", marks[("Vinayak", "Maths")])
