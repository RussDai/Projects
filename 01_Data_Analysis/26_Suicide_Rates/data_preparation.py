
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_loader(): 

    data= pd.read_csv("C:/Users/MyMachine/Desktop/Mission-Project/00_DataSets/24_Suicide_Rates.csv")

    Percentage_of_null_values= data["HDI for year"].isnull().sum() / len(data) *100


    # Remove $ signs from the column names:
    data.columns = data.columns.str.replace('$', '')

    # Remove commas from the column names:
    data.columns = data.columns.str.replace(',', '')

    # Remove spaces from the column names:
    data.columns = data.columns.str.replace(' ', '')

    # Remove periods from the column names:
    data.columns = data.columns.str.replace('.', '')

    # convert date column datatype to datetime
    #data['year'] = pd.to_datetime(data['year'])
    # I comment it out because data values other then year are all zero and that makes
    # no sense

    # From age column; the repeating years word should be removed:
    data["age"]= data["age"].str.replace("years","")

    # In gdp for year column; all the commas should be removed:
    data["gdp_for_year()"]= data["gdp_for_year()"].str.replace(",","")

    # Define a dictionary mapping countries to their continents
    country_to_continent = {
    'Albania': 'Europe', 'Antigua and Barbuda': 'North America', 'Argentina': 'South America',
    'Armenia': 'Asia', 'Aruba': 'North America', 'Australia': 'Oceania',
    'Austria': 'Europe', 'Azerbaijan': 'Asia', 'Bahamas': 'North America',
    'Bahrain': 'Asia', 'Barbados': 'North America', 'Belarus': 'Europe',
    'Belgium': 'Europe', 'Belize': 'North America', 'Bosnia and Herzegovina': 'Europe',
    'Brazil': 'South America', 'Bulgaria': 'Europe', 'Cabo Verde': 'Africa',
    'Canada': 'North America', 'Chile': 'South America', 'Colombia': 'South America',
    'Costa Rica': 'North America', 'Croatia': 'Europe', 'Cuba': 'North America',
    'Cyprus': 'Europe', 'Czech Republic': 'Europe', 'Denmark': 'Europe',
    'Dominica': 'North America', 'Ecuador': 'South America', 'El Salvador': 'North America',
    'Estonia': 'Europe', 'Fiji': 'Oceania', 'Finland': 'Europe',
    'France': 'Europe', 'Georgia': 'Asia', 'Germany': 'Europe',
    'Greece': 'Europe', 'Grenada': 'North America', 'Guatemala': 'North America',
    'Guyana': 'South America', 'Hungary': 'Europe', 'Iceland': 'Europe',
    'Ireland': 'Europe', 'Israel': 'Asia', 'Italy': 'Europe',
    'Jamaica': 'North America', 'Japan': 'Asia', 'Kazakhstan': 'Asia',
    'Kiribati': 'Oceania', 'Kuwait': 'Asia', 'Kyrgyzstan': 'Asia',
    'Latvia': 'Europe', 'Lithuania': 'Europe', 'Luxembourg': 'Europe',
    'Macau': 'Asia', 'Maldives': 'Asia', 'Malta': 'Europe',
    'Mauritius': 'Africa', 'Mexico': 'North America', 'Mongolia': 'Asia',
    'Montenegro': 'Europe', 'Netherlands': 'Europe', 'New Zealand': 'Oceania',
    'Nicaragua': 'North America', 'Norway': 'Europe', 'Oman': 'Asia',
    'Panama': 'North America', 'Paraguay': 'South America', 'Philippines': 'Asia',
    'Poland': 'Europe', 'Portugal': 'Europe', 'Puerto Rico': 'North America',
    'Qatar': 'Asia', 'Republic of Korea': 'Asia', 'Romania': 'Europe',
    'Russian Federation': 'Europe', 'Saint Kitts and Nevis': 'North America',
    'Saint Lucia': 'North America', 'Saint Vincent and Grenadines': 'North America',
    'San Marino': 'Europe', 'Serbia': 'Europe', 'Seychelles': 'Africa',
    'Singapore': 'Asia', 'Slovakia': 'Europe', 'Slovenia': 'Europe',
    'South Africa': 'Africa', 'Spain': 'Europe', 'Sri Lanka': 'Asia',
    'Suriname': 'South America', 'Sweden': 'Europe', 'Switzerland': 'Europe',
    'Thailand': 'Asia', 'Trinidad and Tobago': 'North America', 'Turkey': 'Asia',
    'Turkmenistan': 'Asia', 'Ukraine': 'Europe', 'United Arab Emirates': 'Asia',
    'United Kingdom': 'Europe', 'United States': 'North America', 'Uruguay': 'South America',
    'Uzbekistan': 'Asia'
}

    # Map the continent to a new column
    data['continent'] = data['country'].map(country_to_continent)

    # Group by continent and find the average for HDIforyear column for each continent
    continent_avg = data.groupby('continent')['HDIforyear'].mean()

    data["HDIforyear"]= data['HDIforyear'].fillna(data.groupby('continent')['HDIforyear'].transform('mean'),)

    # Convert datatype of gdp_for_year() column to numeric:
    data["gdp_for_year()"] = pd.to_numeric(data["gdp_for_year()"])

    # Add a hyphen between the country name and the year in the 'country-year' column
    data['country-year'] = data['country'] + '-' + data['year'].astype(str)

    return data