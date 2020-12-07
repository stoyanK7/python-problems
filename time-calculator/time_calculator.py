def add_time(start_time, duration, startingDayOfWeek=""):
    # Start time
    start_time_split = start_time.split()
    start_time_hours = int(start_time_split[0].split(":")[0])
    start_time_minutes = int(start_time_split[0].split(":")[1])
    start_time_am_pm = start_time_split[1]
    
    # Duration
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    
    # Turn start_time into 24 hour format
    if start_time_am_pm == "PM":
        start_time_hours += 12
    
    # Calculate result time
    result_minutes = start_time_minutes + duration_minutes
    result_hours = start_time_hours + duration_hours + (result_minutes // 60)
    result_minutes %= 60
    result_am_pm = "AM"

    # Turn result time to 12 hour format
    if (result_hours % 24) >= 12:
        result_am_pm = "PM"
    
    if (result_hours % 24) > 12:
        result_hours -= 12
    
    old_result_hours = result_hours
    # 0 AM is always displayed as 12 AM
    if (result_hours % 24 == 0) and (result_am_pm == "AM"):
        result_hours = 12

    # Format result time
    result_time = f"{result_hours % 24}:{result_minutes:02} {result_am_pm}"
    
    # Go back to original hours(only when it is 12 AM)
    result_hours = old_result_hours

    # Calculate how many days after start time, result time is
    days = result_hours // 24
    
    # If optional parameter is passed
    if startingDayOfWeek:
        # Input is case sensitive
        startingDayOfWeek = startingDayOfWeek.lower()
        daysOfWeek = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        # Calculate result time day of week
        startingDayOfWeekNumber = daysOfWeek[startingDayOfWeek]
        finishingDayOfWeekNumber = startingDayOfWeekNumber + days
        finishingDayOfWeekNumber %= 7
        finishingDayOfWeek = None
        # Find key in dictionary by value
        for key,value in daysOfWeek.items():
            if(value == finishingDayOfWeekNumber):
                finishingDayOfWeek = key
                break
        
        # Add result time day to output string
        result_time += f", {finishingDayOfWeek.capitalize()}"

    # If result time is next day, we should display it
    if result_hours // 24 == 1:
        result_time += " (next day)"

    # If result time is after 2 or more days
    if result_hours // 24 >= 2:
        result_time += f" ({days} days later)"

    # Return result time
    return result_time
