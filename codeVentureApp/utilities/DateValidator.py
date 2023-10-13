def is_valid_datetime_value(datetime_str):
    """
    DO NOT MODIFY THIS FUNCTION DEFINITION.
    This function checks if given datetime_str represents
    a valid date and time.
    :param datetime_str: a str representation of time and date
    :return: bool (True if datetime str exists, False otherwise)
    """
    date, time = datetime_str.split(" ")
    day, month, year = date.split("/")
    hour, minute = time.split(":")

    # Convert to integers
    year_num = int(year)
    month_num = int(month)
    day_num = int(day)

    # Retrieve valid range values
    valid_hours = range(24)
    valid_minutes = range(60)
    valid_months = range(1, 13)
    if (int(hour) not in valid_hours
            or int(minute) not in valid_minutes
            or month_num not in valid_months):
        return False

    # Days of a calendar month
    valid_days = []

    if month_num in [1, 3, 5, 7, 8, 10, 12]:
        # 31 days in Jan, Mar, May, Jul, Aug, Oct, Dec
        valid_days = range(1, 32)
    elif month_num in [4, 6, 9, 11]:
        # 30 days in Apr, Jun, Sep, Nov
        valid_days = range(1, 31)
    elif month_num == 2 and is_leap_year(year_num):
        # 29 days in Feb for leap year
        valid_days = range(1, 30)
    elif month_num == 2 and not is_leap_year(year_num):
        # 28 days in Feb for non-leap year
        valid_days = range(1, 29)

    return day_num in valid_days