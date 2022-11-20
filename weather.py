import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    isodate = datetime.fromisoformat(iso_string)
    return isodate.strftime("%A %d %B %Y")

#do this first 
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celsius = (float(temp_in_farenheit) - 32) * 5 / 9
    return round(temp_in_celsius,1)

#do this 2nd
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(x) for x in weather_data] #converting weather_data list to float
    return sum(weather_data) / len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == []: #getting rid of empty list
                pass
            elif row == ["date", "min", "max"]: #getting rid of header
                pass
            else: #need to convert the temp into int/float
                child_list=[]
                child_list.append(row[0])
                child_list.append(int(row[1]))
                child_list.append(int(row[2]))
                data.append(child_list)
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    weather_data = [float(x) for x in weather_data]
    min_num = min(weather_data)
    min_index = weather_data.index(min_num)
    return min_num, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    weather_data = [float(x) for x in weather_data]
    max_num = max(weather_data)
    max_index = weather_data.index(max_num)
    return max_num, max_index

#the harder one
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_temps = []
    max_temps = []
    count = 0

    for row in weather_data:
        min_temps.append(row[1])
        max_temps.append(row[2])
        count += 1

    avg_min = calculate_mean(min_temps)
    lowest_min = find_min(min_temps)
    lowest_min_index = lowest_min[1]
    lowest_min_day = weather_data[lowest_min_index][0]

    avg_max = calculate_mean(max_temps)
    highest_max = find_max(max_temps)
    highest_max_index = highest_max[1]
    highest_max_day = weather_data[highest_max_index][0]

    days = len(weather_data)

    summary = f"{days} Day Overview\n  The lowest temperature will be {format_temperature(convert_f_to_c(lowest_min[0]))}, and will occur on {convert_date(lowest_min_day)}.\n  The highest temperature will be {format_temperature(convert_f_to_c(highest_max[0]))}, and will occur on {convert_date(highest_max_day)}.\n  The average low this week is {format_temperature(convert_f_to_c(avg_min))}.\n  The average high this week is {format_temperature(convert_f_to_c(avg_max))}.\n"
    return summary

#2nd hardest
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    line_count = 0
    summary = ""
    for row in weather_data:
        line_count += 1
        summary += f"---- {convert_date(row[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n\n"
    return summary
