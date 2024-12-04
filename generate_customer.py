import csv
from faker import Faker

# Initialize Faker
faker = Faker()

# CSV file name
file_name = "customers_data.csv"

# Columns for the CSV file
columns = ["customer_name", "country"]

# Generate 1000 customer records
data = [
    {"customer_name": faker.name(), "country": faker.country()}
    for _ in range(1000)
]

# Write data to the CSV file
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{file_name}' generated successfully!")
