import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    # temp = (float(25))
    # DEGREE_SYMBOL = u"\N{DEGREE SIGN}"
    
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.
    Args: 
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

# 1 ----- DONE :) 
def convert_date(iso_string):
    change_format = datetime.fromisoformat(iso_string)
    s = change_format.strftime("%A %d %B %Y")
    return s 

    """Converts an ISO formatted date into a human readable format.
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

# 2 ----- DONE : ) 
def convert_f_to_c(temp_in_fahrenheit):
    celsius = (float(temp_in_fahrenheit) - 32) * 5/9
    return round (celsius ,1)

    """Converts an temperature from fahrenheit to celsius.
    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celsius, rounded to 1dp.
    """

# 3 ----- DONE :) 
def calculate_mean(weather_data):
    #  total = weather_data *** do not need to create variable for weather_data
    total = 0
    for item in weather_data:
        total += float(item)  
    mean = total / len(weather_data)
    return mean
    
    """Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

# 4  ----- DONE :) 
def load_data_from_csv(csv_file):
    list = []
    with open (csv_file,encoding = "UTF-8") as csv_open:
        reader = csv.reader(csv_open)
        next(reader) #this means it skips the header
        for line in reader: #figure out another way to write this
            if not (line): #checking if the line is empty and ignoring/continue
                continue
            list.append([line[0],int(line[1]),int(line[2])]) # this is connected with the 3 above, if indented the same as for then it would be seperate
    return list

    """Reads a csv file and stores the data in a list.
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

# 5 ---- DONE but why didn't the other one work?
def find_min(weather_data):

    if len(weather_data) == 0:
        return()

    min_index = 0
    minimum = float(weather_data[0])

    enumerated_wd = enumerate(weather_data)

    for data in enumerated_wd:
        index, temp = data
        temp = float(temp)

        if temp <= minimum:
            minimum = temp
            min_index = index 

    return (minimum, min_index)


    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list."""

# 6 ---- DONE :) 
def find_max(weather_data):

    if len(weather_data) > 0:

        max_value = float(max(weather_data)) #max is an inbuilt function
        print(max_value)
        max_index = 0

    #    i = position of index when using range, w/o using range it will show u the value
        for item in range(len(weather_data)):
            value = float(weather_data[item])
            if max_value == value:
                max_index = item

        return max_value, max_index

    else: return ()   
   

    """Calculates the maximum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

# 7 ---- DONE :)
def generate_summary(weather_data):
    # define variables that we plug into strings and reference lists
    Overview_day = len(weather_data)
    list_min = []
    list_max = []

    for item in weather_data:
        list_min.append(convert_f_to_c(item[1]))
        list_max.append(convert_f_to_c(item[2]))

    lowest_temp = find_min(list_min) #don't need to reference position again, as already done so above
    format_lowest_temp = format_temperature(lowest_temp[0])
    # date = weather_data[0]
    lowest_temp_day = convert_date(weather_data[lowest_temp[1]][0]) #need to convert date format

    highest_temp = find_max(list_max)
    format_highest_temp = format_temperature(highest_temp[0])
    highest_temp_day = convert_date(weather_data[highest_temp[1]][0]) 

    avg_low = calculate_mean(list_min)
    format_avg_low = format_temperature(round(avg_low,1))

    avg_high = calculate_mean(list_max) #needs to return in Celsius
    format_avg_high = format_temperature(round(avg_high,1))

    # \n = move to a newline. W/ two spaces after the \n means that 2x indentation will be placed after the \n.
    summary = (f"{Overview_day} Day Overview\n  The lowest temperature will be {format_lowest_temp}, and will occur on {lowest_temp_day}.\n  The highest temperature will be {format_highest_temp}, and will occur on {highest_temp_day}.\n  The average low this week is {format_avg_low}.\n  The average high this week is {format_avg_high}.\n"  )     

    # print(summary) 
    return summary 
    
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    
  """
    """Hello  # 3x" will hold format
    Laura"""

# 8 ---- DONE :) 
def generate_daily_summary(weather_data):

    data_to_return = ""
    for daily_weather_list in weather_data:
        date_string = daily_weather_list[0] #to collect date in list
        converted_date_string = convert_date(date_string)
        min_temp_f = daily_weather_list[1] #collect temp from list/index 1
        min_temp_c = convert_f_to_c(min_temp_f) #using already defined function of converting Farenheit to Celsius
        max_temp_f = daily_weather_list[2] #collect temp from list/index 2
        max_temp_c = convert_f_to_c(max_temp_f) #using already defined function of converting Farenheit to Celsius
        daily_summary = f"---- {converted_date_string} ----\n  Minimum Temperature: {min_temp_c}°C\n  Maximum Temperature: {max_temp_c}°C\n\n"
        data_to_return = data_to_return + daily_summary #combine in one variable
        
    # print(data_to_return)
    return data_to_return
    
    """ Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """ 