import time
import pandas as pd

# Data is only for early 2017
# Bikeshare is a hypothetical company

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
Asking = True
data_city = ['chicago', 'new york city', 'washington']
data_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


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
    while Asking:
        city = input('1. Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city in data_city:
            break
        else:
            print("Please only choose between chicago, new york city, or washington ")

            # TO DO: get user input for month (all, january, february, ... , june)
    while Asking:
        month = input(
            '2. Which month do you want the data filtered by - January, February, March, April, May, or June?').lower()
        if month in data_months:
            break
        else:
            print("Please only choose between January, February, March, April, May, June or all ")

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while Asking:
        day = input(
            '3. Which day do you want the data filtered by - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        if day in day_of_the_week:
            break
        else:
            print("Please only choose between Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all ")

    print('-' * 40)
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
    # Loading Data then convert to datetime
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # get the month and day of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # To make sure to get the exact day and month if not all
    if month != 'all':
        month = data_months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].value_counts().idxmax()
    most_common_day = df['day_of_week'].value_counts().idxmax()
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].value_counts().idxmax()

    # TO DO: display the most common month
    print('The Most Common Month is:', most_common_month)

    # TO DO: display the most common day of week
    print('The Most Common Day is:', most_common_day)

    # TO DO: display the most common start hour
    print('The Most Common Start Hour is:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()
    most_commonly_used_start_station = df['Start Station'].value_counts().idxmax()
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()
    most_commonly_used_startNend_station = df.groupby(['Start Station', 'End Station']).count()

    # TO DO: display most commonly used start station
    print('The Most Commonly Used Start Station is:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    print('The Most Commonly Used End Station is:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('The Most Frequent Combination of Start and End Station are:', most_commonly_used_startNend_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    # TO DO: display total travel time
    print("The Total Travel Time is :", total_travel_time)

    # TO DO: display mean travel time
    print("The Mean of The Travel Time is :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("User Types :", counts_of_user_types)

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print("Counts of Gender:", counts_of_gender)
    except KeyError:
        print("Counts of Gender: No Data available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        print("The Earliest Year of Birth is:", int(earliest_year_of_birth))
    except KeyError:
        print("The Earliest Year of Birth is: No Data available")
    try:
        most_recent_year_of_birth = df['Birth Year'].max()
        print("The Most Recent Year of Birth is:", int(most_recent_year_of_birth))
    except KeyError:
        print("The Most Recent Year of Birth is: No Data available")
    try:
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print("The Most Common Year of Birth is:", int(most_common_year_of_birth))
    except KeyError:
        print("The Most Common Year of Birth is: No Data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def view_raw_data(df):
    start_loc = 0
    while Asking:
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
        if view_data == 'yes':
            print(df[start_loc:start_loc + 5])
            start_loc = start_loc + 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()                                                                                                                                                         
