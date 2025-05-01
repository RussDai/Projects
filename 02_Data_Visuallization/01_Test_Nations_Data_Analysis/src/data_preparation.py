# 1. Data Cleaning:

import pandas as pd 
import numpy as np
import sys
import warnings
from datetime import datetime
warnings.filterwarnings("ignore") # Ignore warnings

# Define a helper function to process the data:
def data_process():
    data= pd.read_csv("C:/Users/MyMachine/Desktop/Mission-Project/00_DataSets/25_Cricket-all-teams-all-matches.csv")

    # Rename column to smallcase:
    data.columns = data.columns.str.lower()

    # Replace spaces with underscores:
    data.columns = data.columns.str.replace(' ', '_')

    # Replace special characters with underscores:
    data.columns = data.columns.str.replace('[^a-zA-Z0-9_]', '_', regex=True)

    # Replace multiple underscores with a single underscore:
    data.columns = data.columns.str.replace('__+', '_', regex=True)

    # Remove underscores at the beginning and end of column names:
    data.columns = data.columns.str.strip('_')

    # Extract scores for each format using regex from scorecard column:
    data['test_score'] = data['scorecard'].str.extract(r'Test\s#\s(\d+)', expand=False)
    data['odi_score'] = data['scorecard'].str.extract(r'ODI\s#\s(\d+)', expand=False)
    data['t20i_score'] = data['scorecard'].str.extract(r'T20I\s#\s(\d+)', expand=False)

    # Convert the extracted values to numeric, replacing missing values with NaN
    data['test_score'] = pd.to_numeric(data['test_score'], errors='coerce')
    data['odi_score'] = pd.to_numeric(data['odi_score'], errors='coerce')
    data['t20i_score'] = pd.to_numeric(data['t20i_score'], errors='coerce')

    # Delete scorecard column:
    data= data.drop(axis= 0, columns= ["scorecard"])

    # In test_score, odi_score and t20i_score columns, replace Missing value by 0:
    data[["test_score", "odi_score", "t20i_score"]]= data[["test_score", "odi_score", "t20i_score"]].fillna(0)

    # All scores should be in integer format:
    data[["test_score", "odi_score", "t20i_score"]]= data[["test_score", "odi_score", "t20i_score"]].astype(int)
    
    return data

# -------------------------------------------------------------------------------------

# Define a function to split and parse the match_date column:
def split_match_date(date_str):
    try:
        # Split the match_date into the `range` and `year`;
        date_range, year = date_str.split(", ")
        
        # Extract the start date (first part of the range)
        start_date_str = date_range.split("-")[0] + " " + year
        start_date = pd.to_datetime(start_date_str, format="%b %d %Y", errors="coerce")
        
        # Extract the year with month
        year_with_month = start_date.strftime("%Y-%b") if start_date else None
        
        # Calculate the total duration (days)
        if "-" in date_range:
            # Check if the second part of the range includes a month
            end_date_part = date_range.split("-")[-1]
            if not any(char.isalpha() for char in end_date_part):  # If no month is present
                end_date_str = date_range.split("-")[0][:3] + " " + end_date_part + " " + year
            else:
                end_date_str = end_date_part + " " + year
            
            end_date = pd.to_datetime(end_date_str, format="%b %d %Y", errors="coerce")
            total_duration = (end_date - start_date).days + 1 if end_date else None
        else:
            total_duration = 1  # Single-day match
        
        return year_with_month, start_date, total_duration
    except Exception:
        return None, None, None

# ------------------------------------------------------------------------------------

# helper function to get year and total_duration columns;
def data_out(data):
    data["year_with_month"]= data["year_with_month"].str.split("-", expand= True)[0]
    data.rename(columns= {"year_with_month": "year", "match_duration": "match_duration"}, inplace= True)

    # Delete match_date column:
    data= data.drop(axis= 0, columns= ["match_date"])

    # Replace None or NaN values in the year column with a default value (e.g., 0):
    data["year"] = data["year"].fillna(0)

    # Convert the year column to integer type
    data["year"] = data["year"].astype(int)

    # total_duration should be in int format:
    data["total_duration"].replace(value= 0, to_replace= np.nan, inplace=True)
    data["total_duration"]=data["total_duration"].astype(int)

    return data

# --------------------------------------------------------------------------------------

# Wrapper function to process data end-to-end
def process_data_pipeline():
    # Step 1: Clean and preprocess the data
    data = data_process()
    
    # Step 2: Apply the split_match_date function
    data[["year_with_month", "start_date", "total_duration"]] = data["match_date"].apply(
        lambda x: pd.Series(split_match_date(x))
    )
    
    # Step 3: Finalize the data using data_out
    data = data_out(data)
    
    return data

# --------------------
# For data engineering, we need to call the wrapper function to get the final processed data
#data = process_data_pipeline()
# --------------------------------------------------------------------------------------
# 2. Data Engineering:

def data_engineering(data):
    # 1. Create month column from start_date column:
    # add month column to the dataframe:
    data["month"]= data["start_date"].dt.month
    # replace nan by most frequently occuring value of the column:
    data["month"].fillna(data["month"].mode(), inplace= True)
    # Map numeric month values to actual month names:
    month_mapping = {
    1.0: 'Jan', 2.0: 'Feb', 3.0: 'Mar', 4.0: 'Apr',
    5.0: 'May', 6.0: 'Jun', 7.0: 'Jul', 8.0: 'Aug',
    9.0: 'Sep', 10.0: 'Oct', 11.0: 'Nov', 12.0: 'Dec'}
    # Apply the mapping to the 'Month' column:
    data['month'] = data['month'].map(month_mapping)