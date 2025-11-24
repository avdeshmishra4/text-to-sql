"""
Setup script to create SQLite database from CSV files
"""

import pandas as pd
import sqlite3
import os

def create_database():
    """ Create SQLite database from CSV files in data/ directory"""

    # Database file
    db_name = "ecommerce"

    # Connect to SQLite database
    conn = sqlite3.connect(db_name)

    # CSV files in data directory

    csv_files = [
        'users.csv',
        'orders.csv',
        'order_items.csv',
        'products.csv',
        'inventory_items.csv',
        'distribution_centers.csv',
        'events.csv'
    ]

    print('Setting up database from CSV files ....')

    for csv_file in csv_files:
        file_path = os.path.join('data', csv_file)

        if os.path.exists(file_path):
            table_name = os.path.splitext(csv_file)[0]

            print(f"Creating table: {table_name}")

            # Read CSV and create_table
            df = pd.read_csv(file_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)

            print(f"{len(df)} rows inserted into {table_name}")

        else:
            print(f"File not found: {file_path}")

    # verify tables were crated
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print(f"\nDatabase setup complete!")
    print(f"Created tables: {[table[0] for table in tables]}")
    
    conn.close()

if __name__ == "__main__":
    create_database()
