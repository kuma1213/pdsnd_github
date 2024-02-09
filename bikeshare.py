import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']

# Get information for filters from user 
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
    city_list = ['chicago', 'new york city', 'washington']
    city = input('Please enter one city name. Options:chicago, new york city, washington\n').lower()
    while city not in city_list:
        city = input('Please enter one city name. Options:chicago, new york city, washington\n').lower()
    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('Please enter one month name or all\n').lower()
    while month not in month_list:
        month = input('Please enter one month name or all\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('Please enter one day of the week or all\n').lower()
    while day not in day_of_week_list:
        day = input('Please enter one day of the week or all\n').lower()

    print('-'*40)
    return city, month, day

# load the data and create dataframe
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # read the data
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # create month and day_of_week column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # month convert to the corresponding number
    month = month_list.index(month) + 1
    # filer by month
    if month != 13:
        df = df[df['month'] == month]
    # filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.capitalize()]
    return df

# filter the dataframe by user input
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week: {}'.format(common_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print('The most common hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# print station statistical data
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most common end station: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + ' and ' + df['End Station']
    common_combi_station = df['Start and End'].value_counts().idxmax()
    print('The most common combination of start and end station: {}'.format(common_combi_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# print trip duration statistical data
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total trabel time:{}'.format(total))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('Mean trabel time:{}'.format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# print user statistical data
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('Counts of user types:\n{}'.format(count_user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].dropna(axis=0).value_counts()
        print('Counts of gender:\n{}'.format(count_gender))
    else:
        print('This dataframe does not have Gender column.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        min_birth = df['Birth Year'].dropna(axis=0).min()
        max_birth = df['Birth Year'].dropna(axis=0).max()
        common_birth = df['Birth Year'].dropna(axis=0).value_counts().idxmax()
        print('The earliest birth year:{}'.format(min_birth))
        print('The most recent birth year:{}'.format(max_birth))
        print('The most common birth year:{}'.format(common_birth))
    else:
        print('This dataframe does not have Birth Year column.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    response = input('Do you want to look at the first 5 data in the dataframe? Enter yes or no.\n').lower()
    while response not in ['yes', 'no']:
        response = input('Do you want to look at the first 5 data in the dataframe? Enter yes or no.\n').lower()
    start = 0
    while response == 'yes':
        if start +5 < len(df):
            print(df.iloc[start:start+5])
            start += 5
            response =  input('Do you want to look at the next 5 data in the dataframe? Enter yes or no.\n').lower()
            while response not in ['yes', 'no']:
                response = input('Do you want to look at the first 5 data in the dataframe? Enter yes or no.\n').lower()
        else:
            print(df.iloc[start:len(df)])
            break
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()