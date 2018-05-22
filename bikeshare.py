#project is in progress

Step 1: imports and initial functions


import pandas as pd
import csv
import numpy as np
import time
import calendar
from calendar import day_name, month_name
from datetime import datetime
from datetime import time as Time
Step 2: user input


city_data = { 'chicago': 'chicago',
             'new york city': 'new_york_city',
              'washington': 'washington' }

def get_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - csv file for the city selected
   
   """
    
    
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n').lower()
        
        # making sure that user inputs one of the cities listed
       
        if city not in ('chicago', 'new york', 'washington'):
            print('\nPlease enter one of the cities listed.\n')
                
        else:
            break
    
    
    if city == 'chicago':
        city_data = 'Documents/chicago.csv'
   
    elif city == 'new york':
        city_data = 'Documents/new_york_city.csv'
    
    else:
        city_data = 'Documents/washington.csv'

    return city, city_data

city, city_data = get_city()
city, city_data
    


def get_time():
    '''Allows the user to select a specific amount of time to use as filter. 
    Args:
        none.
    Returns:
        (str) 
    '''
    # Ask user for input 
    
    while True:
        time_range = input('\nWould you like to filter the data: by month, day, both or, '
                            'not at all? Type "none" for no time filter.\n').lower()
                            
       
    # making sure that user inputs one of the cities listed
       
    
        if time_range not in ('month', 'day', 'both', 'none'):
            print('\nYou didn\'t enter an available filter. Please enter month, day, both or none.')
        else:
            break
   
    # Return user input as (str) lower case
        
        return time_range

time_range = get_time()
time_range 


# gets user input for month (all, january, february, ... , june)

def get_month():
    
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
        
        
        if month not in month_name[:7]:
            print('\nYou didn\'t enter an available month. Please enter one of the months listed.\n')
        else:
            break
   
   
    
    return list(month_name).index(month)

month = get_month()
month


# get user selected day of week)


def get_day():
    
    while True:
        day = input('\nWhich day? Please enter a day of the week from Sunday to Saturday.'
                    '\n').title()
       
        
        if day not in day_name:
            print('\nPlease enter one of the '
                  'days of the week.\n'
                  'Please try again:')
        else:
            break
    
    return list(day_name).index(day)


day = get_day()
day
Step 3: create the dataframe, and perform any necessary wrangling


df = pd.read_csv(city_data)
df.head()


#renaming columns for formatting consistency
df.rename(columns={'Start Time': 'start_time', 'End Time': 'end_time', 'Trip Duration': 'trip_duration', 'Start Station': 'start_station', 'End Station': 'end_station', 'User Type': 'user_type', 'Gender': 'gender', 'Birth Year': 'birth_year'}, inplace = True)
df.head()


df['start_time'] = pd.to_datetime(df.start_time)

#adding an additonal column to show the day of the week as an int

df['week_day'] = df.start_time.apply(datetime.weekday)


df['traveled'] = df.start_station + " to " + df.end_station
df.head()


#to filter according to user input

df = df.loc[df.start_time.dt.month == month]


df = df.loc[df.week_day == day]
df.head()


df.info()
Step 4: Computing Statistics (Popular times of travel)


# will return most popular month
def popular_month(df):
   
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))



# will return the most popular day
def popular_day(df):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    
    
    print('The most popular day of week for start time is {}.'.format(most_pop_day))


# will return the most popular hour
def popular_hour(df):
    df['hour'] = df['start_time'].dt.hour
    return df.hour.mode()[0]

    
    print("Most popular hour of the day for start time: " + d.strftime("%I %p"))
Computing Statistics (Popular stations and trips)


# will return the most popular starting and ending stations
def popular_stations(df):
    most_pop_start = df['start_station'].mode().to_string(index = False)
    most_pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(most_pop_start))
    print('The most popular end station is {}.'.format(most_pop_end))
    
    


# will return most popular trip
def popular_trip(df):
    most_pop_trip = df['traveled'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))
Computing Statistics (Trip Duration)


# will return total trip duration and average trip duration

def trip_duration(df):
    total_trip_duration = df['trip_duration'].sum()
    avg_trip_duration = df['trip_duration'].mean()
    m, s = divmod(total_trip_duration, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)
    
    
    total_trip_duration = "\nTotal trip duration: %d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    m, s = divmod(avg_trip_duration, 60)
    h, m = divmod(m, 60)
    avg_trip_duration = "Average trip duration: %d hrs %02d min %02d sec" % (h, m, s)
    
    return [total_trip_duration, avg_trip_duration]
  
Computing Statistics (User Info)


# will return user info
def users(df):
    user_type_counts = df.groupby('user_type')['user_type'].count()
   
    return user_type_counts


#returns amounts of each gender
def gender(df):
    gender_counts = df.groupby('gender')['gender'].count()
    
    return gender_counts



#will return oldest, youngest, and the year of birth occurring the most

def birth_years(df):
    oldest_birth_year = "Oldest birth year: " + str(int(df['birth_year'].min()))
    youngest_birth_year = "Most recent birth year: " + str(int(df['birth_year'].max()))
    birth_year_counts = df.groupby('birth_year')['birth_year'].count()
    birth_years_or = birth_year_counts.sort_values(ascending=False)
    total_trips = df['birth_year'].count()
    most_pop_birth_year = "Most popular birth year: " + str(int(birth_years_or.index[0])) + " (" + str(birth_years_or.iloc[0]) + " trips, " + '{0:.2f}%'.format(((birth_years_or.iloc[0]/total_trips) * 100)) + " of trips)"
    
    return [oldest_birth_year, youngest_birth_year, most_pop_birth_year]

Step 5: Raw data


#Displays five lines of data until the user rresponds with the str 'no'.


def raw_data(df):
    i = 0
    show_raw_data = input('\nWould you like to see five lines of raw data? Type \'yes\' or \'no\'.\n')
    while show_raw_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        i += 5
        show_raw_data = input(
            '\nWould you like to see five more lines of raw data? Type \'yes\' or \'no\'.\n'
            )
        


raw_data(df)


#User restart
restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
if restart.lower() == 'yes':
    break
    main()
