"""Lambdata - a collection of Data Science helper functions"""

#accessing libraries through pipenv
import pandas as pd
import numpy as np

def state_abb(df, col):
    """adds a column to a DF with state abbreivations"""
    us_state_abbrev = {'ALABAMA': 'AL',  
                    'ALASKA': 'AK', 
                    'AMERICAN SAMOA': 'AS',
                    'ARIZONA': 'AZ',
                    'ARKANSAS': 'AR',
                    'CALIFORNIA': 'CA',
                    'COLORADO': 'CO',
                    'CONNECTICUT': 'CT',
                    'DELAWARE': 'DE',
                    'DISTRICT OF COLUMBIA': 'DC',
                    'FLORIDA': 'FL',
                    'GEORGIA': 'GA',
                    'GUAM': 'GU',
                    'HAWAII': 'HI',
                    'IDAHO': 'ID',
                    'ILLINOIS': 'IL',
                    'INDIANA': 'IN',
                    'IOWA': 'IA',
                    'KANSAS': 'KS',
                    'Kentucky': 'KY',
                    'LOUISIANA': 'LA',
                    'MAINE': 'ME',
                    'MARYLAND': 'MD',
                    'MASSACHUSETTS': 'MA',
                    'MICHIGAN': 'MI',
                    'MINNESOTA': 'MN',
                    'MISSISSIPPI': 'MS',
                    'MISSOURI': 'MO',
                    'MONTANA': 'MT',
                    'NEBRASKA': 'NE',
                    'NEVADA': 'NV',
                    'NEW HAMPSHIRE': 'NH',
                    'NEW JERSEY': 'NJ',
                    'NEW MEXICO': 'NM',
                    'NEW YORK': 'NY',
                    'NORTH CAROLINA': 'NC',
                    'NORTH DAKOTA': 'ND',
                    'NORTHERN MARIANA ISLANDS':'MP',
                    'OHIO': 'OH',
                    'OKLAHOMA': 'OK',
                    'OREGON': 'OR',
                    'PENNSYLVANIA': 'PA',
                    'PUERTO RICO': 'PR',
                    'RHODE ISLAND': 'RI',
                    'SOUTH CAROLINA': 'SC',
                    'SOUTH DAKOTA': 'SD',
                    'TENNESSEE': 'TN',
                    'TEXAS': 'TX',
                    'UTAH': 'UT',
                    'VERMONT': 'VT',
                    'VIRGIN ISLANDS': 'VI',
                    'VIRGINIA': 'VA',
                    'WASHINGTON': 'WA',
                    'WEST VIRGINIA': 'WV',
                    'WISCONSIN': 'WI',
                    'WYOMING': 'WY'
    }
    
    df['state_abbreviation'] = df[col].str.upper().map(us_state_abbrev)
    
    return df
    
def outlier_rm(df, col):
    IQR = np.quantile(df[col], 0.75) - np.quantile(df[col], 0.25)
    Q3 = np.quantile(df[col], 0.75)
    Q1 = np.quantile(df[col], 0.25) 
    u_bound = Q3 + IQR * 1.5
    l_bound = Q1 - IQR * 1.5

    return df[(df[col] < u_bound) & (df[col] > l_bound)]
