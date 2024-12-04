import csv
from faker import Faker

# Initialize Faker
faker = Faker()

# CSV file name
file_name = "students_data.csv"

# Columns for the CSV file
columns = ["roll_no", "name", "age"]

# Generate 300 student records
data = [
    {"roll_no": 1000 + i, "name": faker.name(), "age": 20 + (i % 5)}
    for i in range(1, 301)
]

# Write data to the CSV file
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{file_name}' generated successfully!")
