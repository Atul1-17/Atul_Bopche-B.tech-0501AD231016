import json

student = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 90},
    {"name": "Rohan", "marks": 78},
]

with open("report.json", "w") as f:
    json.dump(student, f)

try:
    with open("report.json", "r") as f:
        data = json.load(f)

    for student in data:
        if student["marks"] > 75:
            print(student["name"], "-", student["marks"])

except FileNotFoundError:
    print("File not found")