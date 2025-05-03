import pandas as pd
import numpy as np
import sys
import warnings
from datetime import datetime
warnings.filterwarnings("ignore") # Ignore warnings
import re

# Data Processor:
def data_process(filepath="C:/Users/MyMachine/Desktop/Mission-Project/00_DataSets/25_Cricket-all-teams-all-matches.csv"):
    # Load data
    data = pd.read_csv(filepath)

    # Standardize column names
    data.columns = (
        data.columns.str.lower()
        .str.replace(' ', '_')
        .str.replace('[^a-zA-Z0-9_]', '_', regex=True)
        .str.replace('__+', '_', regex=True)
        .str.strip('_')
    )

    # Extract match numbers from 'scorecard' using regex
    data['test_score'] = data['scorecard'].str.extract(r'Test\s#\s*(\d+)', expand=False)
    data['odi_score'] = data['scorecard'].str.extract(r'ODI\s#\s*(\d+)', expand=False)
    data['t20i_score'] = data['scorecard'].str.extract(r'T20I\s#\s*(\d+)', expand=False)

    # Convert extracted match numbers to integers (fill missing with 0)
    for col in ['test_score', 'odi_score', 't20i_score']:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0).astype(int)

    # Drop 'scorecard' column
    data.drop(columns=['scorecard'], inplace=True)

    return data

 # ----------------------------------------

def split_match_date(data):
    """
    Takes a DataFrame with a 'match_date' column and returns a DataFrame
    with added columns: 'start_date', 'year_month', and 'match_duration'.
    """

    def parse_date(row):
        try:
            date_str = row['match_date']
            if pd.isna(date_str):
                return pd.NaT, None, None
            
            # Split into date range and year
            if ", " not in date_str:
                return pd.NaT, None, None
            date_range, year = date_str.split(", ")

            # Extract start date
            start_date_str = date_range.split("-")[0].strip() + " " + year
            start_date = pd.to_datetime(start_date_str, format="%b %d %Y", errors="coerce")

            # Extract year-month
            year_month = start_date.strftime("%Y-%b") if pd.notna(start_date) else None

            # Extract end date if it's a multi-day match
            if "-" in date_range:
                end_date_part = date_range.split("-")[-1].strip()
                # Determine if the end date includes a month
                if any(char.isalpha() for char in end_date_part):
                    end_date_str = end_date_part + " " + year
                else:
                    end_date_str = date_range.split("-")[0][:3] + " " + end_date_part + " " + year
                
                end_date = pd.to_datetime(end_date_str, format="%b %d %Y", errors="coerce")
                duration = (end_date - start_date).days + 1 if pd.notna(end_date) else None
            else:
                duration = 1  # Single-day match

            return start_date, year_month, duration

        except Exception:
            return pd.NaT, None, None

    # Apply the parser row-wise
    parsed = data.apply(parse_date, axis=1, result_type="expand")
    parsed.columns = ['start_date', 'year_month', 'match_duration']

    # Concatenate back with original DataFrame
    data = pd.concat([data, parsed], axis=1)

    return data

# -------------------------------------------------------------------

def data_out():
    # Step 1: Get pre-processed and parsed data
    data = data_process()
    data = split_match_date(data)

    # Step 2: Extract year from 'year_month' column
    data['year'] = data['year_month'].str.split('-', expand=True)[0]

    # Step 3: Drop 'match_date' column
    data.drop(columns=['match_date'], inplace=True)

    # Step 4: Handle missing or invalid years
    data['year'] = data['year'].fillna(0)
    data['year'] = data['year'].astype(int)

    # Step 5: Clean up total_duration
    data['match_duration'] = data['match_duration'].fillna(0)
    data['match_duration'] = data['match_duration'].astype(int)

    return data

# -----------------------------------

def data_engineering():
    # Step 0: Load data
    data = data_out()

    # Step 1: Ensure start_date is datetime
    if not np.issubdtype(data['start_date'].dtype, np.datetime64):
        data['start_date'] = pd.to_datetime(data['start_date'], errors='coerce')

    # Step 2: Create 'month' column
    data["month"] = data["start_date"].dt.month
    if data["month"].isna().any():
        mode_month = data["month"].mode()
        if not mode_month.empty:
            data["month"].fillna(mode_month[0], inplace=True)

    month_mapping = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
        5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    data['month'] = data['month'].map(month_mapping)

    # Step 3: Create ground-to-country mapping
    country_keywords = {
        'India': ['Bengaluru', 'Eden Gardens', 'Delhi', 'Mohali', 'Chennai', 'Ahmedabad', 'Jaipur', 'Nagpur',
                  'Jalandhar', 'Kanpur', 'Wankhede', 'Brabourne', 'Lucknow', 'Gwalior', 'Guwahati',
                  'Jamshedpur', 'Visakhapatnam', 'Kochi', 'Pune', 'Hyderabad (Deccan)', 'Indore', 'Rajkot',
                  'Vadodara', 'Chandigarh', 'Margao', 'Srinagar', 'Thiruvananthapuram', 'New Delhi',
                  'Raipur', 'Mumbai', 'Faridabad', 'Amritsar', 'Vijayawada', 'Jodhpur', 'Dehradun',
                  'Greater Noida', 'Patna'],
        'Pakistan': ['Karachi', 'Faisalabad', 'Lahore', 'Rawalpindi', 'Multan', 'Sialkot', 'Hyderabad (Sind)',
                     'Peshawar', 'Bahawalpur', 'Gujranwala', 'Quetta', 'Sahiwal', 'Sheikhupura', 'Sargodha'],
        'Bangladesh': ['Dhaka', 'Mirpur', 'Fatullah', 'Chattogram', 'Khulna', 'Sylhet', 'Bogra'],
        'Sri Lanka': ['Colombo (RPS)', 'Pallekele', 'Dambulla', 'Hambantota', 'Colombo (SSC)', 'Moratuwa',
                      'Galle', 'Kandy', 'Colombo (PSS)', 'Colombo (CCC)'],
        'UAE': ['Dubai (DICS)', 'Sharjah', 'Abu Dhabi', 'Tolerance Oval'],
        'England': ['Manchester', 'The Oval', 'Birmingham', "Lord's", 'Taunton', 'Nottingham', 'Leeds',
                    'Southampton', 'Bristol', 'Chester-le-Street', 'Northampton', 'Derby', 'Chelmsford',
                    'Hove', 'Leicester', 'Tunbridge Wells', 'Sheffield', 'Scarborough', 'Worcester', 'Canterbury'],
        'Australia': ['Adelaide', 'W.A.C.A', 'Hobart', 'Brisbane', 'Sydney', 'Melbourne', 'Melbourne (Docklands)',
                      'Perth', 'Canberra', 'Launceston', 'Mackay', 'Carrara', 'Geelong', 'Townsville',
                      'Ballarat', 'Devonport', 'Albury', 'Berri'],
        'New Zealand': ['Taupo', 'Mount Maunganui', 'Hamilton', 'Wellington', 'Napier', 'Dunedin', 'Auckland',
                        'Nelson', 'Queenstown', 'Whangarei', 'New Plymouth'],
        'South Africa': ['Johannesburg', 'Durban', 'Centurion', 'East London', 'Gqeberha', 'Paarl', 'Benoni',
                         'Bloemfontein', 'Kimberley', 'Potchefstroom', 'Pietermaritzburg'],
        'West Indies': ['Bridgetown', 'Kingston', 'Lauderhill', 'Roseau', 'Basseterre', 'Providence', "St John's",
                        'Georgetown', 'Port of Spain', 'Kingstown', "St George's", 'Albion', 'Castries', 'Coolidge',
                        'North Sound', 'Tarouba'],
        'Zimbabwe': ['Harare', 'Bulawayo'],
        'Ireland': ['Dublin (Malahide)', 'Dublin', 'Belfast', 'Bready'],
        'Scotland': ['Aberdeen'],
        'Kenya': ['Nairobi (Gym)', 'Nairobi (Aga)', 'Nairobi (Club)'],
        'Canada': ['Toronto', 'King City (NW)'],
        'USA': ['New York', 'Dallas'],
        'Netherlands': ['Amstelveen', 'Rotterdam'],
        'Malaysia': ['Kuala Lumpur'],
        'China': ['Hangzhou'],
        'Singapore': ['Singapore'],
        'Morocco': ['Tangier']
    }

    # Invert mapping: ground -> country
    ground_to_country = {}
    for country, grounds in country_keywords.items():
        for ground in grounds:
            ground_to_country[ground] = country

    # Step 4: Map ground to country
    data['ground_country'] = data['ground'].map(ground_to_country).fillna('Unknown')

    # Step 5: Create is_neutral_ground
    data['is_neutral_ground'] = ~(
        (data['team_1'] == data['ground_country']) |
        (data['team_2'] == data['ground_country'])
    )

    # Step 6: Filter out drawn or missing winner
    data = data[data['winner'].notna() & (data['winner'].str.lower() != 'drawn')]

    # Step 7: Extract won_by_wickets, won_by_runs, won_by_inns
    data['won_by_wickets'] = data['margin'].str.extract(r'(\d+)\s+wickets', expand=False).astype(float)
    data['won_by_runs'] = data['margin'].str.extract(r'(\d+)\s+runs', expand=False).astype(float)
    data['won_by_inns'] = data['margin'].str.contains('innings', case=False, na=False)

    # Optional: Fill NaNs with 0 or False if you prefer
    data['won_by_wickets'].fillna(0, inplace=True)
    data['won_by_runs'].fillna(0, inplace=True)

    return data