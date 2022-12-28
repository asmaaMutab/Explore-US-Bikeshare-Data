import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'sunday','monday', 'tuesday', 'wednesday', 'friday', 'saturday']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Define a variable
    city_name = ''
    #handle user input and incase sensitive inputs 
    while city_name.lower() not in CITY_DATA:
        city_name = input("\n What is the name of the city to analyze data? Please choose from the following (chicago, new york city, washington)\n")
    #if user enter the correct name of city
    if city_name.lower() in CITY_DATA:
            # get the name of the city to analyze 
                 city = CITY_DATA[city_name.lower()]
    else:
            #wrong name of city , continue the loop.
                  print(" Unknown value , Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month 
    #Define a variable
    month_name = ''
    #handle user input and incase sensitive inputs 
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\n What is the name of the month to filter data? Please choose as the following ( 'all' to apply no month filter or january, february, ... , june)\n")
    #if user enter the correct name of month
        if month_name.lower() in MONTH_DATA:
         # get the name of the month to analyze 
            month = month_name.lower()
        else:
            #wrong name of month , continue the loop.
            print("Unknown value , Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #Define a variable
    day_name = ''
     #handle user input and incase sensitive inputs 
    while day_name.lower() not in DAY_DATA:
        day_name = input("\n What is the name of the day to filter data? Please choose as the following ( 'all' to apply no day filter or monday, tuesday, ... sunday)\n")
        #if user enter the correct name of day
    if day_name.lower() in DAY_DATA:
         # get the name of the day to analyze 
                 day = day_name.lower()
    else:
        #wrong name of day , continue the loop.
                 print("Unknown value, Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        data_f - Pandas DataFrame containing city data filtered by month and day
    """
# load data file to the dataframe
    data_f = pd.read_csv(city)
 # casting from the Start Time column to datetime
    data_f['Start Time'] = pd.to_datetime(data_f['Start Time'])
 # get the month and day of week from Start Time to create New Columns
    data_f['month'] = data_f['Start Time'].dt.month
    data_f['day_of_week'] = data_f['Start Time'].dt.weekday_name
    data_f['hour'] = data_f['Start Time'].dt.hour
 # filter by month 
    if month != 'all':
 # use the the months index in the list to get the int
         month = MONTH_DATA.index(month)
 # filter by month to create the new dataframe , if it's matching the user input
         data_f = data_f.loc[data_f['month'] == month]
 # filter by day of week 
    if day != 'all':
 # filter by day of week to create the new dataframe , if it's matching the user input
         data_f = data_f.loc[data_f['day_of_week'] == day.title()]
#return the result 
    return data_f
#end of the function 


def time_stats(data_f):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = data_f['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[common_month].title())


    # TO DO: display the most common day of week
    common_day_of_week = data_f['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)


    # TO DO: display the most common start hour
    common_start_hour = data_f['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))
    #cacluting the amount of time 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(data_f):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = data_f['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = data_f['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (data_f['Start Station'] + "||" + data_f['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    #cacluting the amount of time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(data_f):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = data_f['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = data_f['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    #cacluting the amount of time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(data_f):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = data_f['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))
    #check the city value
    if city == 'chicago.csv' or city == 'new_york_city.csv':

    # TO DO: Display counts of gender
        gender = data_f['Gender'].value_counts()
    print("The count of user gender is: \n" + str(gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = data_f['Birth Year'].min()
    most_recent_birth = data_f['Birth Year'].max()
    most_common_birth = data_f['Birth Year'].mode()[0]
    print('Earliest birth is: {}\n'.format(earliest_birth))
    print('Most recent birth is: {}\n'.format(most_recent_birth))
    print('Most common birth is: {}\n'.format(most_common_birth) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(data_f):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(data_f.head())
    #varaible to track the 5 rows
    nrow = 0
    #start the loop with boolean condition
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        #if the user input is yes , print the next 5 rows
        if view_raw_data.lower() != 'yes':
            return
        nrow = nrow + 5
        # search for index location using iloc function
        print(data_f.iloc[nrow:nrow+5])
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(data_f)
        station_stats(data_f)
        trip_duration_stats(data_f)
        user_stats(data_f)
        while True:
            #start the program 
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(data_f)
            break
            #ask user to restart the program 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
   