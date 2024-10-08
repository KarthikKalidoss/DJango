from faker import Faker
import csv

# Initialize Faker instance
fake = Faker()

# Create dummy data for 50 mobile products
mobile_products_data = []
for i in range(50):
    mobile_products_data.append({
        "category": "Mobile Phones",
        "name": fake.company() + f" Model X{i+1}",
        "vendor": fake.company(),
        "product_image": fake.image_url(width=640, height=480),
        "quantity": fake.random_int(min=10, max=100),
        "original_price": round(fake.random_number(digits=5, fix_len=False) / 100, 2),
        "selling_price": round(fake.random_number(digits=5, fix_len=False) / 100, 2),
        "description": fake.text(max_nb_chars=200),
        "status": fake.boolean(chance_of_getting_true=50),  # 50% chance to be True or False
        "trending": fake.boolean(chance_of_getting_true=20),  # 20% chance to be True (trending)
        "created_at": fake.date_time_this_year(),
    })

# Define the CSV file path for mobile products
mobile_csv_file_path = 'faker_mobile_products_data.csv'

# Write the mobile products data to a CSV file
with open(mobile_csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=mobile_products_data[0].keys())
    writer.writeheader()
    writer.writerows(mobile_products_data)

mobile_csv_file_path
