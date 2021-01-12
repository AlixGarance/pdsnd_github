import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data from Chicago, Washington or New York City? ').lower()
        if city in dict.keys(CITY_DATA):
            print('Looks like you want to know more about {}!'.format(city))
            print()
            break
        else:
            print('Please type your city like in the following examples: Chicago, Washington or New York City.')

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input('Which month would you like to kmow more about: all, january, february, march, april, may or june? ').lower()
        if month == 'all' or month in months:
            print('Looks like you want to know more about {}!'.format(month))
            print()
            break
        else:
            print('Please type all or type your month like in the following examples: january, february, march, april, may or june.')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input('Which day would you like to kmow more about: all, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ').lower()
        if day == 'all' or day in days:
            print('Looks like you want to know more about {}!'.format(day))
            print()
            break
        else:
            print('Please type all or type your month like in the following examples: monday, tuesday, wednesday, thursday, friday, saturday or sunday.')

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day)

    # display the most common start hour, should add df['Start Time'] = pd.to_datetime(df['Start Time']) ????
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour of week:', common_hour)

    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most common Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is: ', int(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in seconds is: ', int(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_count(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Count...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The count of users is:\n', count_user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    if city == 'washington':
        print('\nThere is no data about gender and birth year for Washington.\n')
        print('-'*40)
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of gender
        count_gender = df['Gender'].value_counts()
        print('The count of gender is:\n', count_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest birth year is: ', int(earliest_birth_year))
        latest_birth_year = df['Birth Year'].max()
        print('The latest birth year is: ', int(latest_birth_year))
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', int(common_birth_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def see_data(df):
    """Displays 5 more rows."""

    x = 5
    ask_raw_data = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n')

    while True:
        if ask_raw_data == 'yes':
            print(df.head(x))
            x += 5
            ask_raw_data = input('Do you want to see 5 more lines of raw data? Enter yes or no.\n')
        elif ask_raw_data != 'yes':
            print('-'*40)
            print('\nThanks for your inputs!\n')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_count(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
