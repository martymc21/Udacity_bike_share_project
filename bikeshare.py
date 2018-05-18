##imports

from calendar import day_name, month_name
from datetime import datetime
from datetime import time as Time
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline


###
###


## Filenames
chicago_data = pd.read_csv('Documents/chicago.csv')
new_york_city_data = pd.read_csv('Documents/new_york_city.csv')
washington_data = pd.read_csv('Documents/washington.csv')


CITY_DATA = { 'chicago': 'chicago',
              'new york city': 'new_york_city',
              'washington': 'washington' }

def get_city():
    """
    Asks user to choose a city and displays the data for selected city.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
   
   """
    #get user input for city (chicago, new york city, washington). HINT use a while loop to handle invalid inputs
    
    # Ask user for input while managing incorrect input
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n').lower()
        # Confirm if input string is one of the listed cities and ask again if not
        if city not in ('chicago', 'new york', 'washington'):
            print('\nPlease enter one of the cities listed.\n'
                  'Returning you to the original input request:')
        else:
            break
    # Use the input to select a filename
    if city == 'chicago':
        city_data = 'chicago.csv'
    elif city == 'new york':
        city_data = 'new_york_city.csv'
    else:
        city_data = 'washington.csv'

    return city, city_data

city, city_data = get_city()
city, city_data
    
#############################



def get_time():
    '''Allows the user to select a specific amount of time to use as filter. 
    Args:
        none.
    Returns:
        (str) inputted type of filter.
    '''
    # Ask user for input while incorrect input
    
    while True:
        time_range = input('\nWould you like to filter the data: by month, day, both or, '
                            'not at all? Type "none" for no time filter.'
                            '(This next step will take some time.)\n').lower()
       
    # Confirm if input string is one of the listed options and ask again if not
       
    
        if time_range not in ('month', 'day', 'both', 'none'):
            print('\nYou didn\'t enter an available filter. Please enter month, day, both or none.'
                  '\nReturning you to the original input request:')
        else:
            break
    # Return user input as (str) lower case
    return time_range


time_range = get_time()
time_range 


###########

def get_month():
    '''Returns month between January and June, according to user input, while managing
       incorrect input.

    Args:
        none.
    Returns:
        (int) month as its index of month_name ('January' = 1)
    '''
    # Ask user for input while managing incorrect input
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
        # Confirm if input string is one of the listed months and ask again if not
        if month not in month_name[:7]:
            print('\nYou didn\'t enter an available month. Please enter one of the months listed.\n'
                  'Returning you to the original input request:')
        else:
            break
    # Return user input as (str) title case
    return list(month_name).index(month)

month = get_month()
month


##########

def get_day():
    '''Asks the user for a day and returns the corresponding index, while managing
       for incorrect input.

    Args:
        none.
    Returns:
        (int) day of the week as its index of day_name ('monday' = 0).
    '''
    
    # Ask user for input while managing incorrect input
    while True:
        day = input('\nWhich day? Please enter a day of the week from Sunday to Saturday.'
                    '\n').title()
        # Confirm if input string is one of the days of the week and ask again if not
        if day not in day_name:
            print('\nYou didn\'t enter an available day. Please enter one of the '
                  'days of the week.\n'
                  'Returning you to the original input request:')
        else:
            break
    # Return (int) of day's index in day_name
    return list(day_name).index(day)



day = get_day()
day
