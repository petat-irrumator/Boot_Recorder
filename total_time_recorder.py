import datetime


record_file = open(
    r"D:\All-vs-studio-vs-code-sublimeProjects\VS-Code-Projects\Boot_Recorder\record.txt", "r")

record_num = 0

startup_time_list = []
shutdown_time_list = []


# reading all the records from the record file

for records in record_file:
    record_num += 1

    year_index = records.find("Year")
    month_index = records.find("Month")
    day_index = records.find("Day")
    hour_index = records.find("Hour")
    minute_index = records.find("Minute")

    # getting all the startup record time values
    if record_num % 2 != 0:

        startup_year = records[year_index+5:month_index]
        startup_month = records[month_index+6:day_index]
        startup_day = records[day_index+4:hour_index]
        startup_hour = records[hour_index+5:minute_index]
        startup_minute = records[minute_index+7:]

        startup_time_format = fr"{startup_year}M{startup_month}D{startup_day}H{startup_hour}E{startup_minute}"

        startup_time_list.append(startup_time_format)

        # print(startup_year, startup_month, startup_day,
        #      startup_hour, startup_minute)

    # getting all the shutdown record time values
    elif record_num % 2 == 0:

        shutdown_year = records[year_index+5:month_index]
        shutdown_month = records[month_index+6:day_index]
        shutdown_day = records[day_index+4:hour_index]
        shutdown_hour = records[hour_index+5:minute_index]
        shutdown_minute = records[minute_index+7:]

        shutdown_time_format = f"{shutdown_year}M{shutdown_month}D{shutdown_day}H{shutdown_hour}E{shutdown_minute}"

        shutdown_time_list.append(shutdown_time_format)

        # print(shutdown_year, shutdown_month, shutdown_day,
        #      shutdown_hour, shutdown_minute)


# deleting the last item from startup_time_list is it can disturb calculation of the time interval


startup_time_list_length = startup_time_list.__len__()

startup_time_list.__delitem__(startup_time_list_length-1)


# print(startup_time_list)
# print(shutdown_time_list)

# removing escape character /n presesnt in every string in list startup_time_list


new_startup_time_list = []

for time_entry in startup_time_list:
    escapes = ''.join([chr(char) for char in range(1, 32)])
    translator = str.maketrans('', '', escapes)
    new_time_entry = time_entry.translate(translator)

    new_startup_time_list.append(new_time_entry)

# removing escape character /n presesnt in every string in list shutdown_time_list


new_shutdown_time_list = []

for time_entry in shutdown_time_list:
    escapes = ''.join([chr(char) for char in range(1, 32)])
    translator = str.maketrans('', '', escapes)
    new_time_entry = time_entry.translate(translator)

    new_shutdown_time_list.append(new_time_entry)


# print(new_startup_time_list)
# print(new_shutdown_time_list)


startup_obj_list = []
shutdown_obj_list = []

# converting every item in new_startup_time_list to class datetime and storing the new entries to startup_obj_list
for every_time_entry in new_startup_time_list:

    str(every_time_entry)

    new_time_entry_year = int(every_time_entry[:every_time_entry.find("M")])

    new_time_entry_month = int(
        every_time_entry[every_time_entry.find("M")+1:every_time_entry.find("D")])

    new_time_entry_day = int(
        every_time_entry[every_time_entry.find("D")+1:every_time_entry.find("H")])

    new_time_entry_hour = int(
        every_time_entry[every_time_entry.find("H")+1:every_time_entry.find("E")])

    new_time_entry_minute = int(
        every_time_entry[every_time_entry.find("E")+1:])

    # print(new_time_entry_year, new_time_entry_month, new_time_entry_day,
    #      new_time_entry_hour, new_time_entry_minute)

    new_time_entry = datetime.datetime(
        new_time_entry_year, new_time_entry_month, new_time_entry_day, new_time_entry_hour, new_time_entry_minute)

    startup_obj_list.append(new_time_entry)


# converting every item in new_shutdown_time_list to class datetime and storing the new entries to shutdown_obj_list
for every_time_entry in new_shutdown_time_list:

    str(every_time_entry)

    new_time_entry_year = int(every_time_entry[:every_time_entry.find("M")])

    new_time_entry_month = int(
        every_time_entry[every_time_entry.find("M")+1:every_time_entry.find("D")])

    new_time_entry_day = int(
        every_time_entry[every_time_entry.find("D")+1:every_time_entry.find("H")])

    new_time_entry_hour = int(
        every_time_entry[every_time_entry.find("H")+1:every_time_entry.find("E")])

    new_time_entry_minute = int(
        every_time_entry[every_time_entry.find("E")+1:])

    # print(new_time_entry_year, new_time_entry_month, new_time_entry_day,
    #      new_time_entry_hour, new_time_entry_minute)

    new_time_entry = datetime.datetime(
        new_time_entry_year, new_time_entry_month, new_time_entry_day, new_time_entry_hour, new_time_entry_minute)

    shutdown_obj_list.append(new_time_entry)


# print(startup_obj_list)
# print(shutdown_obj_list)


# calculating time interval by subtracting entries from startup_obj_list and hutdown_obj_list and putting the entires in a another time_interval_list. These entries have the same index

time_interval_list = []
counter = 0

for time_entries in startup_obj_list:

    startup_obj = startup_obj_list[counter]
    shutdown_obj = shutdown_obj_list[counter]

    time_interval = shutdown_obj-startup_obj
    counter += 1

    time_interval_list.append(time_interval)
    # print(time_interval)

# print(time_interval_list)

# calculating the sum of all the time intervals and writing the sum in a file

sum_of_time_interval_list = datetime.datetime(2022, 1, 1, 0, 0)

refrence_time = datetime.datetime(2022, 1, 1, 0, 0)

for time_intervals in time_interval_list:

    sum_of_time_interval_list = sum_of_time_interval_list + time_intervals

    # print(time_intervals)

# print(sum_of_time_interval_list-refrence_time)


total_time_file = open(r"D:\All-vs-studio-vs-code-sublimeProjects\VS-Code-Projects\Boot_Recorder\total_time.txt", "a")

total_time_file.write(f"{sum_of_time_interval_list-refrence_time}\n")


total_time_file.close()
record_file.close()
