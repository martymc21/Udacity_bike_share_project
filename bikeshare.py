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
    Asks user to choose a city and displays the data for selected city.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
   
   """
    #get user input for city (chicago, new york city, washington). HINT use a while loop to handle invalid inputs
    
    # Asks user for input 
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
    # Asks user for input 
    
    while True:
        time_range = input('\nWould you like to filter the data: by month, day, both or, '
                            'not at all? Type "none" for no time filter.'
                            '(This next step will take some time.)\n').lower()
       
    # Confirms if the  input string is one of the listed options and then redirects  back to prompt if string is not in list
       
    
        if time_range not in ('month', 'day', 'both', 'none'):
            print('\nYou didn\'t enter an available filter. Please enter month, day, both or none.'
                  '\nReturning you to the original input request:')
        else:
            break
  
  # Returns the user input as (str) lower case
    return time_range


time_range = get_time()
time_range 


###########

def get_month():
    '''Returns month between January and June.

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
   
  # Returns the user input as (str) title case
    return list(month_name).index(month)

month = get_month()
month


##########

def get_day():
    '''Asks the user to choose a particular day 

    Args:
        none.
    Returns:
        (int) day of the week as its index of day_name ('monday' = 0).
    '''
    
    # Asks user for input 
    while True:
        day = input('\nWhich day? Please enter a day of the week from Sunday to Saturday.'
                    '\n').title()
      
      # Confirms if input string is one of the days of the week and redirects back to orginal prompt if it isnt
      
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


##creating dataframe
df = pd.read_csv(city_data)
df.head()

df.info()
###
#renaming columns for formatting consistency
df.rename(columns={'Start Time': 'start_time', 'End Time': 'end_time', 'Trip Duration': 'trip_duration', 'Start Station': 'start_station', 'End Station': 'end_station', 'User Type': 'user_type', 'Gender': 'gender', 'Birth Year':'birth_year'}, inplace = True)
df.head()

#converting 
df['start_time'] = pd.to_datetime(df.start_time)

#adding an additonal column for the day of the week
df['weekday'] = df.start_time.apply(datetime.weekday)

df = df.loc[df.weekday == day]
df.head()

df.info()

#####Computing statistics

#most popular month
def popular_month(df):
   
    #Count the number of rows that have a particular month value.
   
    trips_by_month = df.groupby('month')['start_time'].count()
   
    #Sorts the months and then returns a string showing the monthe with the highest value
    
    return "Most popular month for start time: " + calendar.month_name[int(trips_by_month.sort_values(ascending=False).index[0])]

#most popular day
def popular_day(df):
    
    #Count the number of rows that have a particular Day of Week value.
    
    trips_by_day = df.groupby('day')['start_time'].count()
    
    #Sorts the days and then returns a string showing the day with the highest value

    return "Most popular day of the week for start time: " + calendar.day_name[int(trips_by_day_of_week.sort_values(ascending=False).index[0])]


#most popular hour
def popular_hour(df):
    
#Count the number of rows that have a particular Hour of Day value.
    
    trips_per_hour = df.groupby('Hour of Day')['start_time'].count()
    
#Sort the results highest to lowest and then return the hour of the day that was highest (first in sorted list)
    
    most_pop_hour = trips_per_hour.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(most_pop_hour, "%H")
   
    
    return "Most popular hour of the day for start time: " + d.strftime("%I %p")
  
  #most popular station
def popular_stations(df):
    
    start_station_counts = df.groupby('start_station')['start_station'].count()
    
    end_station_counts = df.groupby('end_station')['end_station'].count()
    
    start_stations_or = start_station_counts.sort_values(ascending=False)
    
    end_stations_or = end_station_counts.sort_values(ascending=False)
    
    total_trips = df['start_station'].count()
    
    most_pop_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " (" + str(sorted_start_stations[0]) + " trips, " + '{0:.2f}%'.format(((sorted_start_stations[0]/total_trips) * 100)) + " of trips)"
    
    most_pop_end_station = "Most popular end station: " + sorted_end_stations.index[0] + " (" + str
    
    #total trip duration and average trip duration

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


 def display_data(df):
    '''Provides the user the option of viewing five lines of data, repeating this upon request
       until the user responds with 'no'.

    Args:
        Pandas DataFrame.
    Returns:
        none.
    '''
   
    i = 0
    show_data = input('\nWould you like to see five lines of raw data? Type \'yes\' or \'no\'.\n')
    while show_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        i += 5
        show_data = input(
            '\nWould you like to see five more lines of raw data? Type \'yes\' or \'no\'.\n'
            )
        
        
# Restart?
restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
if restart.lower() == 'yes':
    break
    main()
