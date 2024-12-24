import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def fetch_xdr_data():
    """
    Fetch data from the 'xdr_data' table in the PostgreSQL database.    
    """
    # Get the database URL from environment variables
    DATABASE_URL = os.getenv('DATABASE_URL')
    QUERY = "SELECT * FROM xdr_data"

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")

    try:
        # Create a database engine
        engine = create_engine(DATABASE_URL)
        # Execute query and fetch data into a DataFrame
        data = pd.read_sql(QUERY, engine)
        return data
    except Exception as e:
        raise Exception(f"An error occurred while fetching data: {e}")

def insert_data_to_db(df, table_name):
    """
    Insert DataFrame into a PostgreSQL table.
    """
    DATABASE_URL = os.getenv('DATABASE_URL')

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")

    try:
        # Create a database engine
        engine = create_engine(DATABASE_URL)
        # Insert DataFrame into the specified table
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data has been successfully inserted into the {table_name} table.")
    except Exception as e:
        raise Exception(f"An error occurred while inserting data: {e}")

def update_data_in_db(table_name, update_values, condition):
    """
    Update records in a PostgreSQL table.
    """
    DATABASE_URL = os.getenv('DATABASE_URL')

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")

    try:
        # Create a database engine
        engine = create_engine(DATABASE_URL)
        # Update records
        with engine.connect() as conn:
            conn.execute(f"UPDATE {table_name} SET {update_values} WHERE {condition}")
        print(f"Records in {table_name} have been successfully updated.")
    except Exception as e:
        raise Exception(f"An error occurred while updating data: {e}")

def delete_data_from_db(table_name, condition):
    """
    Delete records from a PostgreSQL table.
    """
    DATABASE_URL = os.getenv('DATABASE_URL')

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")

    try:
        # Create a database engine
        engine = create_engine(DATABASE_URL)
        # Delete records
        with engine.connect() as conn:
            conn.execute(f"DELETE FROM {table_name} WHERE {condition}")
        print(f"Records from {table_name} have been successfully deleted.")
    except Exception as e:
        raise Exception(f"An error occurred while deleting data: {e}")

def fetch_filtered_data(query):
    """
    Fetch filtered data based on a custom SQL query.
    """
    DATABASE_URL = os.getenv('DATABASE_URL')

    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the .env file")

    try:
        # Create a database engine
        engine = create_engine(DATABASE_URL)
        # Execute query and fetch filtered data into a DataFrame
        data = pd.read_sql(query, engine)
        return data
    except Exception as e:
        raise Exception(f"An error occurred while fetching filtered data: {e}")

# Example usage
if __name__ == "__main__":
    # Fetch data from 'xdr_data'
    xdr_data = fetch_xdr_data()
    print(xdr_data.head())

    # Insert new data into a PostgreSQL table
    insert_data_to_db(xdr_data, 'xdr_data_copy')

    # Update data in a table
    update_data_in_db('xdr_data', "column_name = 'new_value'", "column_name = 'old_value'")

    # Delete data from a table
    delete_data_from_db('xdr_data', "column_name = 'value_to_delete'")

    # Fetch filtered data based on a custom query
    filtered_data = fetch_filtered_data("SELECT * FROM xdr_data WHERE column_name = 'some_value'")
    print(filtered_data.head())
