#!/usr/bin/env python3
"""
Pakistan Sales Data Generator
Generates realistic sales data for Pakistani markets in a fully normalized OLTP database structure
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import csv
import os

class PakistanSalesDataGenerator:
    def __init__(self):
        # Pakistani provinces and major cities
        self.provinces = {
            'Punjab': ['Lahore', 'Faisalabad', 'Rawalpindi', 'Multan', 'Gujranwala', 'Sialkot', 'Bahawalpur', 'Sargodha'],
            'Sindh': ['Karachi', 'Hyderabad', 'Sukkur', 'Larkana', 'Nawabshah', 'Mirpur Khas', 'Jacobabad'],
            'Khyber Pakhtunkhwa': ['Peshawar', 'Mardan', 'Abbottabad', 'Swat', 'Nowshera', 'Charsadda', 'Mansehra'],
            'Balochistan': ['Quetta', 'Turbat', 'Khuzdar', 'Chaman', 'Zhob', 'Gwadar'],
            'Gilgit-Baltistan': ['Gilgit', 'Skardu', 'Chilas', 'Astore'],
            'Azad Kashmir': ['Muzaffarabad', 'Mirpur', 'Kotli', 'Rawalakot']
        }
        
        # Pakistani names (common first and last names)
        self.first_names = [
            'Ahmed', 'Ali', 'Hassan', 'Hussein', 'Muhammad', 'Usman', 'Umar', 'Bilal', 'Hamza', 'Zain',
            'Fatima', 'Aisha', 'Maryam', 'Zara', 'Hania', 'Sana', 'Ayesha', 'Noor', 'Mariam', 'Zoya',
            'Abdullah', 'Ibrahim', 'Yusuf', 'Haris', 'Rayyan', 'Arham', 'Zayan', 'Ayan', 'Amaan', 'Shahzad',
            'Amina', 'Khadija', 'Sumaya', 'Hafsa', 'Jannat', 'Mahnoor', 'Alina', 'Sadia', 'Nida', 'Rabia'
        ]
        
        self.last_names = [
            'Khan', 'Ali', 'Hussain', 'Ahmed', 'Malik', 'Raza', 'Hassan', 'Abbas', 'Rizvi', 'Zaidi',
            'Shah', 'Qureshi', 'Hashmi', 'Jafri', 'Naqvi', 'Rizwan', 'Siddiqui', 'Farooq', 'Khalid', 'Saleem',
            'Rehman', 'Iqbal', 'Akhtar', 'Nadeem', 'Rashid', 'Tariq', 'Waseem', 'Naeem', 'Saeed', 'Zahid'
        ]
        
        # Product categories and brands relevant to Pakistan
        self.product_categories = {
            1: {'name': 'Electronics', 'brands': ['Samsung', 'Huawei', 'Oppo', 'Vivo', 'Infinix', 'Tecno', 'QMobile']},
            2: {'name': 'Textiles', 'brands': ['Gul Ahmed', 'Khaadi', 'Alkaram', 'Chen One', 'Bonanza', 'Sapphire']},
            3: {'name': 'Food & Beverages', 'brands': ['Nestle', 'Unilever', 'Engro', 'Shan Foods', 'National Foods', 'Mitchells']},
            4: {'name': 'Automotive', 'brands': ['Suzuki', 'Toyota', 'Honda', 'Daihatsu', 'Nissan', 'Mitsubishi']},
            5: {'name': 'Home & Garden', 'brands': ['IKEA', 'Habitt', 'Interwood', 'Chenab', 'Furniture Mall']},
            6: {'name': 'Beauty & Personal Care', 'brands': ['L\'Oreal', 'Garnier', 'Fair & Lovely', 'Clean & Clear', 'Ponds']},
            7: {'name': 'Sports & Fitness', 'brands': ['Nike', 'Adidas', 'Puma', 'Reebok', 'Under Armour']},
            8: {'name': 'Books & Stationery', 'brands': ['Oxford', 'Pelikan', 'Dollar', 'Pilot', 'Staedtler']}
        }
        
        # Store types and names
        self.store_types = ['Retail', 'Supermarket', 'Department Store', 'Specialty Store', 'Outlet', 'Mall']
        
        # Payment methods common in Pakistan
        self.payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Mobile Banking', 'Bank Transfer', 'EasyPaisa', 'JazzCash']
        
        # Shipping methods
        self.shipping_methods = ['Standard', 'Express', 'Same Day', 'Pickup', 'Courier']
        
        # Order statuses
        self.order_statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']
        
        # Customer segments
        self.customer_segments = ['Premium', 'Regular', 'Occasional', 'VIP']
        
        # Education levels
        self.education_levels = ['Primary', 'Secondary', 'Higher Secondary', 'Bachelor', 'Master', 'PhD', 'Other']
        
        # Marital statuses
        self.marital_statuses = ['Single', 'Married', 'Divorced', 'Widowed']
        
        # Genders
        self.genders = ['M', 'F', 'Other']

    def generate_customers(self, num_customers=1000):
        """Generate customer data"""
        customers = []
        
        for i in range(1, num_customers + 1):
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])}"
            phone = f"+92-{random.randint(300, 349)}-{random.randint(1000000, 9999999)}"
            
            # Generate realistic birth date (18-80 years old)
            birth_year = random.randint(1944, 2006)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28)  # Using 28 to avoid month/day issues
            date_of_birth = datetime(birth_year, birth_month, birth_day).date()
            
            # Generate registration date (within last 5 years)
            registration_date = datetime.now().date() - timedelta(days=random.randint(0, 1825))
            
            # Generate annual income based on segment
            segment = random.choices(self.customer_segments, weights=[0.1, 0.6, 0.25, 0.05])[0]
            if segment == 'Premium':
                annual_income = random.randint(1500000, 5000000)  # 1.5M - 5M PKR
            elif segment == 'VIP':
                annual_income = random.randint(5000000, 15000000)  # 5M - 15M PKR
            elif segment == 'Regular':
                annual_income = random.randint(500000, 1500000)   # 500K - 1.5M PKR
            else:  # Occasional
                annual_income = random.randint(200000, 800000)    # 200K - 800K PKR
            
            customers.append({
                'CUSTOMER_ID': i,
                'FIRST_NAME': first_name,
                'LAST_NAME': last_name,
                'EMAIL': email,
                'PHONE': phone,
                'DATE_OF_BIRTH': date_of_birth,
                'GENDER': random.choice(self.genders),
                'MARITAL_STATUS': random.choice(self.marital_statuses),
                'EDUCATION_LEVEL': random.choice(self.education_levels),
                'ANNUAL_INCOME': annual_income,
                'CUSTOMER_SEGMENT': segment,
                'REGISTRATION_DATE': registration_date,
                'IS_ACTIVE': random.choice([True, True, True, False])  # 75% active
            })
        
        return customers

    def generate_customer_addresses(self, customers):
        """Generate customer addresses"""
        addresses = []
        address_id = 1
        
        for customer in customers:
            # Each customer gets 1-2 addresses
            num_addresses = random.choices([1, 2], weights=[0.8, 0.2])[0]
            
            for i in range(num_addresses):
                province = random.choice(list(self.provinces.keys()))
                city = random.choice(self.provinces[province])
                
                # Generate realistic street addresses
                street_numbers = [f"{random.randint(1, 999)}", f"Block {random.choice(['A', 'B', 'C', 'D', 'E'])}", f"House {random.randint(1, 999)}"]
                street_names = [
                    'Main Boulevard', 'Park Road', 'Mall Road', 'College Road', 'University Road',
                    'Industrial Area', 'Defence Housing', 'Gulberg', 'Model Town', 'Johar Town',
                    'Bahria Town', 'DHA', 'Clifton', 'Saddar', 'Cantt'
                ]
                
                street_address = f"{random.choice(street_numbers)} {random.choice(street_names)}"
                postal_code = f"{random.randint(10000, 99999)}"
                
                addresses.append({
                    'ADDRESS_ID': address_id,
                    'CUSTOMER_ID': customer['CUSTOMER_ID'],
                    'ADDRESS_TYPE': 'Primary' if i == 0 else 'Secondary',
                    'STREET_ADDRESS': street_address,
                    'CITY': city,
                    'PROVINCE': province,
                    'POSTAL_CODE': postal_code,
                    'COUNTRY': 'Pakistan',
                    'IS_DEFAULT': i == 0
                })
                address_id += 1
        
        return addresses

    def generate_product_categories(self):
        """Generate product categories"""
        categories = []
        
        for cat_id, cat_info in self.product_categories.items():
            categories.append({
                'CATEGORY_ID': cat_id,
                'CATEGORY_NAME': cat_info['name'],
                'DESCRIPTION': f"Products in {cat_info['name']} category",
                'PARENT_CATEGORY_ID': None,  # No hierarchy for now
                'IS_ACTIVE': True
            })
        
        return categories

    def generate_products(self, num_products=500):
        """Generate product data"""
        products = []
        
        for i in range(1, num_products + 1):
            category_id = random.choice(list(self.product_categories.keys()))
            category_info = self.product_categories[category_id]
            brand = random.choice(category_info['brands'])
            
            # Generate product name based on category and brand
            if category_id == 1:  # Electronics
                product_names = ['Smartphone', 'Laptop', 'Tablet', 'TV', 'Headphones', 'Camera', 'Speaker', 'Charger']
                product_name = f"{brand} {random.choice(product_names)} {random.randint(1, 20)}"
            elif category_id == 2:  # Textiles
                product_names = ['Shirt', 'Pants', 'Dress', 'Suit', 'Kurta', 'Shalwar', 'Dupatta', 'Scarf']
                product_name = f"{brand} {random.choice(product_names)}"
            elif category_id == 3:  # Food
                product_names = ['Rice', 'Oil', 'Tea', 'Biscuits', 'Chocolate', 'Juice', 'Milk', 'Bread']
                product_name = f"{brand} {random.choice(product_names)}"
            else:
                product_name = f"{brand} Product {i}"
            
            # Generate realistic pricing
            base_price = random.randint(500, 50000)
            unit_cost = base_price * random.uniform(0.6, 0.8)
            unit_price = base_price
            msrp = base_price * random.uniform(1.1, 1.3)
            
            # Generate weight and dimensions for physical products
            weight_kg = random.uniform(0.1, 10.0) if category_id not in [3, 7, 8] else random.uniform(0.01, 2.0)
            dimensions = f"{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(1, 50)} cm"
            
            products.append({
                'PRODUCT_ID': i,
                'PRODUCT_NAME': product_name,
                'CATEGORY_ID': category_id,
                'BRAND': brand,
                'MODEL': f"Model-{random.randint(1000, 9999)}",
                'DESCRIPTION': f"High quality {product_name.lower()} from {brand}",
                'UNIT_COST': round(unit_cost, 2),
                'UNIT_PRICE': round(unit_price, 2),
                'MSRP': round(msrp, 2),
                'WEIGHT_KG': round(weight_kg, 2),
                'DIMENSIONS_CM': dimensions,
                'IS_ACTIVE': random.choice([True, True, True, False])  # 75% active
            })
        
        return products

    def generate_stores(self, num_stores=50):
        """Generate store data"""
        stores = []
        
        for i in range(1, num_stores + 1):
            province = random.choice(list(self.provinces.keys()))
            city = random.choice(self.provinces[province])
            
            store_name = f"{random.choice(['Mega', 'Super', 'Prime', 'Elite', 'Premium', 'Express'])} {random.choice(['Store', 'Mart', 'Center', 'Plaza', 'Mall'])} {i}"
            store_code = f"ST{i:03d}"
            
            # Generate store address
            street_address = f"{random.randint(1, 999)} {random.choice(['Main Road', 'Commercial Area', 'Market Street', 'Shopping District'])}"
            phone = f"+92-{random.randint(300, 349)}-{random.randint(1000000, 9999999)}"
            email = f"info@{store_name.lower().replace(' ', '')}.com"
            
            # Opening date within last 10 years
            opening_date = datetime.now().date() - timedelta(days=random.randint(0, 3650))
            
            stores.append({
                'STORE_ID': i,
                'STORE_NAME': store_name,
                'STORE_CODE': store_code,
                'ADDRESS': street_address,
                'CITY': city,
                'PROVINCE': province,
                'POSTAL_CODE': f"{random.randint(10000, 99999)}",
                'PHONE': phone,
                'EMAIL': email,
                'MANAGER_ID': None,  # Will be set later
                'STORE_TYPE': random.choice(self.store_types),
                'IS_ACTIVE': random.choice([True, True, True, False]),  # 75% active
                'OPENING_DATE': opening_date
            })
        
        return stores

    def generate_employees(self, stores, num_employees=200):
        """Generate employee data"""
        employees = []
        
        for i in range(1, num_employees + 1):
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            email = f"{first_name.lower()}.{last_name.lower()}@company.com"
            phone = f"+92-{random.randint(300, 349)}-{random.randint(1000000, 9999999)}"
            
            # Hire date within last 5 years
            hire_date = datetime.now().date() - timedelta(days=random.randint(0, 1825))
            
            # Job titles and departments
            job_titles = ['Sales Associate', 'Cashier', 'Manager', 'Supervisor', 'Customer Service', 'Stock Clerk']
            departments = ['Sales', 'Customer Service', 'Operations', 'Management', 'Inventory']
            
            job_title = random.choice(job_titles)
            department = random.choice(departments)
            
            # Assign to a random store
            store_id = random.choice(stores)['STORE_ID']
            
            # Generate salary based on job title
            if 'Manager' in job_title:
                salary = random.randint(80000, 150000)  # 80K - 150K PKR
            elif 'Supervisor' in job_title:
                salary = random.randint(60000, 100000)  # 60K - 100K PKR
            else:
                salary = random.randint(30000, 60000)   # 30K - 60K PKR
            
            employees.append({
                'EMPLOYEE_ID': i,
                'FIRST_NAME': first_name,
                'LAST_NAME': last_name,
                'EMAIL': email,
                'PHONE': phone,
                'HIRE_DATE': hire_date,
                'JOB_TITLE': job_title,
                'DEPARTMENT': department,
                'STORE_ID': store_id,
                'MANAGER_ID': None,  # Will be set later
                'SALARY': salary,
                'IS_ACTIVE': random.choice([True, True, True, False])  # 75% active
            })
        
        # Assign managers
        managers = [e for e in employees if 'Manager' in e['JOB_TITLE']]
        non_managers = [e for e in employees if 'Manager' not in e['JOB_TITLE']]
        
        for emp in non_managers:
            if random.random() < 0.3:  # 30% have managers
                emp['MANAGER_ID'] = random.choice(managers)['EMPLOYEE_ID']
        
        # Update store manager IDs
        for store in stores:
            store_employees = [e for e in employees if e['STORE_ID'] == store['STORE_ID'] and 'Manager' in e['JOB_TITLE']]
            if store_employees:
                store['MANAGER_ID'] = random.choice(store_employees)['EMPLOYEE_ID']
        
        return employees

    def generate_orders(self, customers, stores, employees, products, num_orders=5000):
        """Generate order data"""
        orders = []
        order_details = []
        
        for i in range(1, num_orders + 1):
            customer = random.choice(customers)
            store = random.choice(stores)
            employee = random.choice([e for e in employees if e['STORE_ID'] == store['STORE_ID']])
            
            # Generate order date within last 2 years
            order_date = datetime.now().date() - timedelta(days=random.randint(0, 730))
            required_date = order_date + timedelta(days=random.randint(1, 14))
            ship_date = order_date + timedelta(days=random.randint(1, 7)) if random.random() < 0.8 else None
            
            # Order status based on dates
            if ship_date and ship_date < datetime.now().date():
                order_status = random.choice(['Delivered', 'Shipped'])
            elif ship_date:
                order_status = 'Shipped'
            else:
                order_status = random.choice(['Pending', 'Processing'])
            
            # Generate order details (1-5 products per order)
            num_products = random.randint(1, 5)
            order_products = random.sample(products, min(num_products, len(products)))
            
            total_amount = 0
            tax_amount = 0
            shipping_cost = random.randint(0, 500)
            discount_amount = 0
            
            # Create order details
            for product in order_products:
                quantity = random.randint(1, 5)
                unit_price = product['UNIT_PRICE']
                
                # Apply random discount (0-20%)
                discount_percent = random.uniform(0, 0.2)
                discount_amount += (unit_price * quantity * discount_percent)
                
                line_amount = unit_price * quantity * (1 - discount_percent)
                total_amount += line_amount
                
                order_details.append({
                    'ORDER_ID': i,
                    'PRODUCT_ID': product['PRODUCT_ID'],
                    'QUANTITY_ORDERED': quantity,
                    'UNIT_PRICE': unit_price,
                    'DISCOUNT_PERCENT': round(discount_percent * 100, 2),
                    'TOTAL_LINE_AMOUNT': round(line_amount, 2)
                })
            
            # Calculate tax (15% GST in Pakistan)
            tax_amount = total_amount * 0.15
            final_amount = total_amount + tax_amount + shipping_cost - discount_amount
            
            orders.append({
                'ORDER_ID': i,
                'CUSTOMER_ID': customer['CUSTOMER_ID'],
                'STORE_ID': store['STORE_ID'],
                'EMPLOYEE_ID': employee['EMPLOYEE_ID'],
                'ORDER_DATE': order_date,
                'REQUIRED_DATE': required_date,
                'SHIP_DATE': ship_date,
                'ORDER_STATUS': order_status,
                'SHIP_METHOD': random.choice(self.shipping_methods),
                'SHIPPING_ADDRESS_ID': None,  # Will be set later
                'TOTAL_AMOUNT': round(total_amount, 2),
                'TAX_AMOUNT': round(tax_amount, 2),
                'SHIPPING_COST': shipping_cost,
                'DISCOUNT_AMOUNT': round(discount_amount, 2),
                'FINAL_AMOUNT': round(final_amount, 2),
                'PAYMENT_METHOD': random.choice(self.payment_methods),
                'PAYMENT_STATUS': 'Completed' if order_status in ['Delivered', 'Shipped'] else 'Pending',
                'NOTES': f"Order placed by {customer['FIRST_NAME']} {customer['LAST_NAME']}"
            })
        
        return orders, order_details

    def generate_all_data(self, num_customers=1000, num_products=500, num_stores=50, num_employees=200, num_orders=5000):
        """Generate all data sets"""
        print("Generating Pakistan Sales Data...")
        
        # Generate base data
        customers = self.generate_customers(num_customers)
        customer_addresses = self.generate_customer_addresses(customers)
        product_categories = self.generate_product_categories()
        products = self.generate_products(num_products)
        stores = self.generate_stores(num_stores)
        employees = self.generate_employees(stores, num_employees)
        orders, order_details = self.generate_orders(customers, stores, employees, products, num_orders)
        
        # Create consolidated sales data for CSV export
        sales_data = []
        for order in orders:
            order_detail = next((od for od in order_details if od['ORDER_ID'] == order['ORDER_ID']), None)
            if order_detail:
                customer = next((c for c in customers if c['CUSTOMER_ID'] == order['CUSTOMER_ID']), None)
                product = next((p for p in products if p['PRODUCT_ID'] == order_detail['PRODUCT_ID']), None)
                store = next((s for s in stores if s['STORE_ID'] == order['STORE_ID']), None)
                employee = next((e for e in employees if e['EMPLOYEE_ID'] == order['EMPLOYEE_ID']), None)
                
                if all([customer, product, store, employee]):
                    sales_data.append({
                        'ORDER_ID': order['ORDER_ID'],
                        'CUSTOMER_ID': order['CUSTOMER_ID'],
                        'PRODUCT_ID': order_detail['PRODUCT_ID'],
                        'STORE_ID': order['STORE_ID'],
                        'EMPLOYEE_ID': order['EMPLOYEE_ID'],
                        'ORDER_DATE': order['ORDER_DATE'],
                        'SHIP_DATE': order['SHIP_DATE'],
                        'QUANTITY_ORDERED': order_detail['QUANTITY_ORDERED'],
                        'UNIT_PRICE': order_detail['UNIT_PRICE'],
                        'DISCOUNT_PERCENT': order_detail['DISCOUNT_PERCENT'],
                        'TOTAL_AMOUNT': order_detail['TOTAL_LINE_AMOUNT'],
                        'PAYMENT_METHOD': order['PAYMENT_METHOD'],
                        'ORDER_STATUS': order['ORDER_STATUS'],
                        'SHIP_METHOD': order['SHIP_METHOD']
                    })
        
        return {
            'customers': customers,
            'customer_addresses': customer_addresses,
            'product_categories': product_categories,
            'products': products,
            'stores': stores,
            'employees': employees,
            'orders': orders,
            'order_details': order_details,
            'sales_data': sales_data
        }

    def export_to_csv(self, data, output_dir='.'):
        """Export data to CSV files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Export individual tables
        for table_name, table_data in data.items():
            if table_data:  # Skip empty tables
                filename = f"pakistan_{table_name}.csv"
                filepath = os.path.join(output_dir, filename)
                
                df = pd.DataFrame(table_data)
                df.to_csv(filepath, index=False)
                print(f"Exported {len(table_data)} records to {filename}")
        
        # Export main sales data file
        sales_filepath = os.path.join(output_dir, 'pakistan_sales_data.csv')
        sales_df = pd.DataFrame(data['sales_data'])
        sales_df.to_csv(sales_filepath, index=False)
        print(f"Exported {len(data['sales_data'])} sales records to pakistan_sales_data.csv")
        
        return sales_filepath

def main():
    """Main function to generate and export data"""
    generator = PakistanSalesDataGenerator()
    
    # Generate data with realistic volumes for Pakistani market
    data = generator.generate_all_data(
        num_customers=2000,      # 2K customers
        num_products=800,        # 800 products
        num_stores=75,           # 75 stores across provinces
        num_employees=300,       # 300 employees
        num_orders=10000         # 10K orders
    )
    
    # Export to CSV files
    output_dir = 'pakistan_sales_data'
    sales_file = generator.export_to_csv(data, output_dir)
    
    print(f"\n✅ Pakistan Sales Data Generation Complete!")
    print(f"📊 Generated {len(data['sales_data'])} sales records")
    print(f"👥 Generated {len(data['customers'])} customers")
    print(f"🏪 Generated {len(data['stores'])} stores")
    print(f"📦 Generated {len(data['products'])} products")
    print(f"📋 Generated {len(data['orders'])} orders")
    print(f"💼 Generated {len(data['employees'])} employees")
    print(f"\n📁 Files exported to: {output_dir}/")
    print(f"🎯 Main sales file: {sales_file}")

if __name__ == "__main__":
    main()
