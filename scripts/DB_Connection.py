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
