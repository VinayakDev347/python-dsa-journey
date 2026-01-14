
# Dictionary

student = {
    "name": "Vinayak",
    "age": 24,
    "course": "MCA"
}

print(student)
print(student["name"])

# Add value to dict
student["collage"] = "Bharathiyar University collage"

print(student)

# Loop through Dict
for key,value in student.items():
    print(key , ":", value)