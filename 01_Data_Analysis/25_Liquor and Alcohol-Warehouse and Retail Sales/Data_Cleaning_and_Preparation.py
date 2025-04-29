<<<<<<< HEAD
import pandas as pd
import numpy as np

#  Disable future warnings:
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


def load_and_prepare_data():
    data = pd.read_csv(
    "C:/Users/MyMachine/Desktop/Mission-Project/00_DataSets/23_Liquor_and_Alcohol-Warehouse_and_Retail_Sales_DataSet.csv"
)

    data["RETAIL SALES"] = data["RETAIL SALES"].replace(
    to_replace=np.nan, value=data["RETAIL SALES"].mean()
)

    data["ITEM TYPE"].mode()[0]

    data["ITEM TYPE"] = data["ITEM TYPE"].replace(
    to_replace=np.nan, value=data["ITEM TYPE"].mode()[0]
)

    data["SUPPLIER"] = data["SUPPLIER"].replace(
    to_replace=np.nan, value=data["SUPPLIER"].mode()[0]
)

    data.columns = [
    "year",
    "month",
    "supplier",
    "item code",
    "item description",
    "item type",
    "retail sales",
    "retail transfers",
    "warehouse sales",
]

    # Define a mapping of numeric month values to month names
    month_mapping = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

    # Use replace() to map the numeric month values to corresponding month names
    data["month"] = data["month"].replace(month_mapping)

    # Define the ordered list of month names
    month_names = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

    # Convert the month column to a categorical type with an ordered list of categories
    data["month"] = pd.Categorical(data["month"], categories=month_names, ordered=True)

    # Alternative way:
    """
    month_mapping = {
    1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
    5: 'may', 6: 'jun', 7: 'jul', 8: 'aug',
    9: 'sep', 10: 'oct', 11:'nov', 12:'dec'
}

    # Use map() to replace numeric month values with month names
    data["month"] = data["month"].map(month_mapping)

    # Define the ordered list of month names
    ordered_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    # Convert the month column to a categorical data type with an ordered list
    data["month"] = pd.Categorical(data["month"], categories=ordered_months, ordered=True)
    """

    data["supplier"] = pd.Categorical(data["supplier"])
    data["item code"] = pd.Categorical(data["item code"])
    data["item description"] = pd.Categorical(data["item description"])
    data["item type"] = pd.Categorical(data["item type"])

    return data

#print(data)




'''
    # way-1: Make it more import friendly:
    # prepare_data.py
    def load_and_prepare_data():
    # all your cleaning logic here
    return data

'''

"""
# Way-2: Works but not Recommended:
# prepare_data.py

def get_data(data):
    return data
# Then guard it with a __name__ == "__main__" block to prevent accidental execution when importing:
if __name__ == "__main__":
data = get_data()  # only runs when you run the script directly
"""
#print(data.shape)
#load_and_prepare_data()
=======
import pandas as pd
import numpy as np

#  Disable future warnings:
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


def load_and_prepare_data():
    data = pd.read_csv(
    "/home/russ/Desktop/Mission-Project/00_DataSets/23_Liquor_and_Alcohol-Warehouse_and_Retail_Sales_DataSet.csv"
)

    data["RETAIL SALES"] = data["RETAIL SALES"].replace(
    to_replace=np.nan, value=data["RETAIL SALES"].mean()
)

    data["ITEM TYPE"].mode()[0]

    data["ITEM TYPE"] = data["ITEM TYPE"].replace(
    to_replace=np.nan, value=data["ITEM TYPE"].mode()[0]
)

    data["SUPPLIER"] = data["SUPPLIER"].replace(
    to_replace=np.nan, value=data["SUPPLIER"].mode()[0]
)

    data.columns = [
    "year",
    "month",
    "supplier",
    "item code",
    "item description",
    "item type",
    "retail sales",
    "retail transfers",
    "warehouse sales",
]

    # Define a mapping of numeric month values to month names
    month_mapping = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

    # Use replace() to map the numeric month values to corresponding month names
    data["month"] = data["month"].replace(month_mapping)

    # Define the ordered list of month names
    month_names = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

    # Convert the month column to a categorical type with an ordered list of categories
    data["month"] = pd.Categorical(data["month"], categories=month_names, ordered=True)

    # Alternative way:
    """
    month_mapping = {
    1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr',
    5: 'may', 6: 'jun', 7: 'jul', 8: 'aug',
    9: 'sep', 10: 'oct', 11:'nov', 12:'dec'
}

    # Use map() to replace numeric month values with month names
    data["month"] = data["month"].map(month_mapping)

    # Define the ordered list of month names
    ordered_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    # Convert the month column to a categorical data type with an ordered list
    data["month"] = pd.Categorical(data["month"], categories=ordered_months, ordered=True)
    """

    data["supplier"] = pd.Categorical(data["supplier"])
    data["item code"] = pd.Categorical(data["item code"])
    data["item description"] = pd.Categorical(data["item description"])
    data["item type"] = pd.Categorical(data["item type"])

    return data

#print(data)




'''
    # way-1: Make it more import friendly:
    # prepare_data.py
    def load_and_prepare_data():
    # all your cleaning logic here
    return data

'''

"""
# Way-2: Works but not Recommended:
# prepare_data.py

def get_data(data):
    return data
# Then guard it with a __name__ == "__main__" block to prevent accidental execution when importing:
if __name__ == "__main__":
data = get_data()  # only runs when you run the script directly
"""
#print(data.shape)
#load_and_prepare_data()
>>>>>>> 389f30ffef1a17d195c89a879bd2adc4c3404cdc
