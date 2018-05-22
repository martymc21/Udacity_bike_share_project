## THIS PROJECT IS IN PROGRESS

##imports

import pandas as pd
import csv
import numpy as np
import time
import calendar
from datetime import datetime
from calendar import day_name, month_name
from datetime import time as Time



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
    # Use the input to select a filename
    
    if city == 'chicago':
        city_data = 'Documents/chicago.csv'
   
    elif city == 'new york':
        city_data = 'Documents/new_york_city.csv'
    
    else:
        city_data = 'Documents/washington.csv'

    return city, city_data

city, city_data = get_city()
city, city_data
    
    
#############################



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
            print('\nYou didn\'t enter an available filter. Please enter month, day, both or none.)
        else:
            break
   

        
        return time_range

time_range = get_time()
time_range 
                  
###########

# gets user input for month (all, january, february, ... , june)

def get_month():
    '''Returns month between January and June, according to user input.
    Args:
       name of month to analyze.
    Returns:
        (int) representing the number of month to filter by ('January' = 1)
    '''
    # Ask user for input
    
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
        
        # Confirms if input string is one of the listed months and ask again if not
        
        if month not in month_name[:7]:
            print('\nYou didn\'t enter an available month. Please enter one of the months listed.\n')
        else:
            break
   
    # Return user input as (str) 
    
    return list(month_name).index(month)

month = get_month()
month


##########

# get user input for day of week (all, monday, tuesday, ... sunday)


def get_day():
    '''Asks the user for a day and returns int representing the day selected
    Args:
      name of the day of thw week to filter by
    Returns:
        (int) day of the week as day_name ('monday' = 0).
    '''
    
    
    
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


##creating dataframe
df = pd.read_csv(city_data)
df.head()

df.info()

#######

   #getting rid of the spaces in the column titles

df.rename(columns={'Start Time': 'start_time', 'End Time': 'end_time', 'Trip Duration': 'trip_duration', 'Start Station': 'start_station', 'End Station': 'end_station', 'User Type': 'user_type', 'Gender': 'gender', 'Birth Year': 'birth_year'}, inplace = True)
df.head()

df['start_time'] = pd.to_datetime(df.start_time)

#adding an additonal column for weekday to help with filtering

df['weekday'] = df.start_time.apply(datetime.weekday)

df = df.loc[df.weekday == day]
df.head()

df.info()

#####Computing statistics

#most popular month

def popular_month(df):
   
 #counts the months and then Sorts the months and then returns a string showing the month with the highest value
   
   monthly_trips = df.groupby('month')['start_time'].count()
   
    #Sorts the months and then returns a string showing the monthe with the highest value
    
    return "Most popular month for start time: " + calendar.month_name[int(monthly_trips.sort_values(ascending=False).index[0])]

#most popular day

def popular_day(df):
    
 #counts the days and then sorts the days and then returns a string showing the day with the highest value
    
  trips_per_day = df.groupby('day')['start_time'].count()
    

    return "Most popular day of the week for start time: " + calendar.day_name[int(trips_per_day.sort_values(ascending=False).index[0])]


# will return the most popular hour

def popular_hour(df):
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    
    return "Most popular hour of the day for start time: " + d.strftime("%I %p")

# will return the most popular station

def popular_stations(df):
    
    start_station_counts = df.groupby('start_station')['start_station'].count()
    
    end_station_counts = df.groupby('end_station')['end_station'].count()
    
    start_stations_or = start_station_counts.sort_values(ascending=False)
    
    end_stations_or = end_station_counts.sort_values(ascending=False)
    
    total_trips = df['start_station'].count()
    
    most_pop_start_station = "\nMost popular start station: " + start_stations_or.index[0] + " (" + str(start_stations_or[0]) + " trips, " + '{0:.2f}%'.format(((start_stations_or[0]/total_trips) * 100)) + " of trips)"
    
     most_popular_end_station = "Most popular end station: " + end_stations_or.index[0] + " (" + str(end_stations_or[0]) + " trips, " + '{0:.2f}%'.format(((end_stations_or[0]/total_trips) * 100)) + " of trips)"
    
    
    return [most_pop_start_station, most_pop_end_station]

                  
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

  
 # will return most popular trip

def popular_trip(df):
                  
    trip_counts = df.groupby(['start_station', 'end_station'])['start_time'].count()
   
    trip_stations_or = trip_counts.sort_values(ascending=False)
    
    total_trips = df['start_station'].count()
    
    
    return "Most popular trip: " + "\n  start station: " + str(sorted_trip_stations.index[0][0]) + "\n  End station: " + str(trip_stations_or.index[0][1]) + "\n  (" + str(trip_stations_or[0]) +  " trips, " + '{0:.2f}%'.format(((trip_stations_or[0]/total_trips) * 100)) + " of trips)"
  
  # will return user info
def users(df):
                  
    user_type_counts = df.groupby('user_type')['user_type'].count()
   
    return user_type_counts
  
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


 def raw_data(df):
    '''Displays five lines of data until the user rresponds with the str 'no'.

    Args:
        Pandas DF
    Returns:
        none.
    '''
   
    i = 0
    show_raw_data = input('\nWould you like to see five lines of raw data? Type \'yes\' or \'no\'.\n')
    while show_raw_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        i += 5
        show_raw_data = input(
            '\nWould you like to see five more lines of raw data? Type \'yes\' or \'no\'.\n'
            )
        
                  
 raw_data(df)
        
# User restart
restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
if restart.lower() == 'yes':
    break
    main()
