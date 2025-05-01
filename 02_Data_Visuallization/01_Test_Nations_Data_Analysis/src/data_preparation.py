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
data = process_data_pipeline()
# --------------------------------------------------------------------------------------

# 2. Data Engineering:

def data_engineering(data):
    # Data from data preparation step:
    data = process_data_pipeline()

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

    # 2. **Create `"Is Neutral Ground"` column:**

    # Create the mapping of each ground to its country
    grounds = [
    'Bengaluru', 'Eden Gardens', 'Delhi', 'Karachi', 'Faisalabad',
    'Lahore', 'Mohali', 'Rawalpindi', 'Multan', 'Chennai', 'Sialkot',
    'Ahmedabad', 'Jaipur', 'Nagpur', 'Jalandhar', 'Hyderabad (Sind)',
    'Kanpur', 'Wankhede', 'Brabourne', 'Peshawar', 'Bahawalpur',
    'Dhaka', 'Lucknow', 'Dubai (DICS)', 'Colombo (RPS)', 'Pallekele',
    'Manchester', 'The Oval', 'Birmingham', 'Adelaide', 'Mirpur',
    'Dambulla', 'Centurion', 'Gwalior', 'Guwahati', 'Abu Dhabi',
    'Jamshedpur', 'Visakhapatnam', 'Kochi', 'Amstelveen', 'Sharjah',
    'W.A.C.A', 'Hobart', 'Brisbane', 'Toronto', 'Colombo (SSC)',
    'Singapore', 'Sydney', 'Gujranwala', 'Pune', 'Hyderabad (Deccan)',
    'Indore', 'Melbourne', 'Quetta', 'Sahiwal', 'New York',
    'Johannesburg', 'Durban', 'Hambantota', 'Leeds', 'Fatullah',
    'Hangzhou', 'Perth', "Lord's", 'Colombo (PSS)', 'Taunton',
    'Nairobi (Gym)', 'Melbourne (Docklands)', 'Nottingham', 'Cardiff',
    'Canberra', 'Harare', 'Gros Islet', 'Chattogram', 'Khulna',
    'Northampton', 'Moratuwa', 'Christchurch', 'Cape Town',
    'Southampton', 'Bristol', 'Chester-le-Street', 'Cuttack',
    'Bridgetown', 'Dublin (Malahide)', 'Dublin', 'Belfast', 'Kingston',
    'Lauderhill', 'Mount Maunganui', 'Hamilton', 'Wellington',
    'Napier', 'Dunedin', 'Auckland', 'Nelson', 'Queenstown', 'Derby',
    'East London', 'Gqeberha', 'Sheikhupura', 'Paarl', 'Benoni',
    'Bloemfontein', 'Tangier', 'Galle', 'Kandy', 'Colombo (CCC)',
    'Hyderabad', 'Kimberley', 'Sargodha', 'Swansea', 'King City (NW)',
    'Roseau', 'Basseterre', 'Providence', "St John's", 'Georgetown',
    'Port of Spain', 'Kingstown', "St George's", 'Albion', 'Bulawayo',
    'Dharamsala', 'Ranchi', 'Rajkot', 'Vadodara', 'Chandigarh',
    'Kuala Lumpur', 'Margao', 'Srinagar', 'Thiruvananthapuram',
    'New Delhi', 'Chelmsford', 'Raipur', 'North Sound', 'Mumbai',
    'Faridabad', 'Taupo', 'Amritsar', 'Launceston', 'Hove', 'Mackay',
    'Tarouba', 'Vijayawada', 'Jodhpur', 'Leicester', 'Tunbridge Wells',
    'Sylhet', 'Dehradun', 'Tolerance Oval', 'Greater Noida',
    'Rotterdam', 'Bready', 'Cairns', 'Darwin', 'Canterbury',
    'Sheffield', 'Potchefstroom', 'Carrara', 'Geelong', 'Castries',
    'Townsville', 'Bogra', 'Pietermaritzburg', 'Dallas',
    'Nairobi (Aga)', 'Scarborough', 'Ballarat', 'Devonport', 'Albury',
    'Aberdeen', 'Whangarei', 'Nairobi (Club)', 'Berri', 'Coolidge',
    'Worcester', 'Patna', 'New Plymouth'
]

    # Country lookup based on cities/venues:
    ground_to_country = {}

    # Helper mapping by partial match:
    country_keywords = {
    'India': ['Bengaluru', 'Eden Gardens', 'Delhi', 'Mohali', 'Chennai', 'Ahmedabad', 'Jaipur',
              'Nagpur', 'Jalandhar', 'Kanpur', 'Wankhede', 'Brabourne', 'Lucknow', 'Gwalior',
              'Guwahati', 'Jamshedpur', 'Visakhapatnam', 'Kochi', 'Pune', 'Hyderabad (Deccan)',
              'Indore', 'Rajkot', 'Vadodara', 'Chandigarh', 'Margao', 'Srinagar',
              'Thiruvananthapuram', 'New Delhi', 'Raipur', 'Mumbai', 'Faridabad', 'Amritsar',
              'Vijayawada', 'Jodhpur', 'Dehradun', 'Greater Noida', 'Patna'],
    'Pakistan': ['Karachi', 'Faisalabad', 'Lahore', 'Rawalpindi', 'Multan', 'Sialkot',
                 'Hyderabad (Sind)', 'Peshawar', 'Bahawalpur', 'Gujranwala', 'Quetta',
                 'Sahiwal', 'Sheikhupura', 'Sargodha'],
    'Bangladesh': ['Dhaka', 'Mirpur', 'Fatullah', 'Chattogram', 'Khulna', 'Sylhet', 'Bogra'],
    'Sri Lanka': ['Colombo (RPS)', 'Pallekele', 'Dambulla', 'Hambantota', 'Colombo (SSC)',
                  'Moratuwa', 'Galle', 'Kandy', 'Colombo (PSS)', 'Colombo (CCC)'],
    'UAE': ['Dubai (DICS)', 'Sharjah', 'Abu Dhabi'],
    'England': ['Manchester', 'The Oval', 'Birmingham', "Lord's", 'Taunton', 'Nottingham',
                'Leeds', 'Southampton', 'Bristol', 'Chester-le-Street', 'Northampton',
                'Derby', 'Chelmsford', 'Hove', 'Leicester', 'Tunbridge Wells', 'Sheffield',
                'Scarborough', 'Worcester'],
    'Australia': ['Adelaide', 'W.A.C.A', 'Hobart', 'Brisbane', 'Sydney', 'Melbourne',
                  'Melbourne (Docklands)', 'Perth', 'Canberra', 'Launceston', 'Mackay',
                  'Carrara', 'Geelong', 'Townsville', 'Ballarat', 'Devonport', 'Albury',
                  'Berri'],
    'New Zealand': ['Taupo', 'Mount Maunganui', 'Hamilton', 'Wellington', 'Napier',
                    'Dunedin', 'Auckland', 'Nelson', 'Queenstown', 'Whangarei',
                    'New Plymouth'],
    'South Africa': ['Johannesburg', 'Durban', 'Centurion', 'East London', 'Gqeberha',
                     'Paarl', 'Benoni', 'Bloemfontein', 'Kimberley', 'Potchefstroom',
                     'Pietermaritzburg'],
    'West Indies': ['Bridgetown', 'Kingston', 'Lauderhill', 'Roseau', 'Basseterre',
                    'Providence', "St John's", 'Georgetown', 'Port of Spain',
                    'Kingstown', "St George's", 'Albion', 'Castries', 'Coolidge',
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
    'Namibia': [],
    'Afghanistan': [],
    'Nepal': [],
    'Hong Kong': [],
    'Germany': [],
    'Italy': [],
    'Morocco': ['Tangier'],
    'France': [],
    'UAE': ['Tolerance Oval'],
    'England': ['Canterbury'],  # UK variant
}

    # Assign countries to grounds
    for ground in grounds:
        assigned = False
        for country, keywords in country_keywords.items():
            if ground in keywords:
                ground_to_country[ground] = country
                assigned = True
                break
        if not assigned:
            ground_to_country[ground] = 'Unknown'

    ground_to_country_sorted = dict(sorted(ground_to_country.items()))

    # 3. Map ground to country:
    data['ground_country'] = data['ground'].map(ground_to_country_sorted)

    # 4. Create is_neutral_ground column:
    data['is_neutral_ground'] = ~(
    (data['team_1'] == data['ground_country']) |
    (data['team_2'] == data['ground_country']))

    # .4 **Creating `won_by_runs` and `won_by_inns` columns from `margin`:**

    # Filter out rows where the match is drawn or winner is missing
    data = data[data["winner"].notna() & (data["winner"] != "drawn")]
    # Extract the number of wickets from the margin column
    data["won_by_wickets"] = data["margin"].str.extract(r"(\d+)\s+wickets", expand=False).astype(float)

    # Extract the number of runs from the margin column
    data["won_by_runs"] = data["margin"].str.extract(r"(\d+)\s+runs", expand=False).astype(float)

    # Handle matches won by "innings and X runs"
    innings_and_runs = data["margin"].str.extract(r"innings\s+and\s+(\d+)\s+runs", expand=False).astype(float)
    data["won_by_runs"] = data["won_by_runs"].fillna(innings_and_runs)

    return data

# For Testing if the whole pipeline is doing well or not:
#data_engineering(data)
#print(data.shape)

