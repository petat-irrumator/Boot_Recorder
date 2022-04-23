import time


# Getting the current date and time
current_time = time.localtime()

current_year = "Year:"+str(current_time.tm_year)
current_month = " Month:"+str(current_time[1])
current_month_day = " Day:"+str(current_time.tm_mday)
current_hour = " Hour:"+str(current_time[3])
current_min = " Minute:"+str(current_time[4])

total_time = current_year+current_month + \
    current_month_day+current_hour+current_min
# Storing the date and time in a .txt file named record

record_file = open(
    r"D:\All-vs-studio-vs-code-sublimeProjects\VS-Code-Projects\Boot_Recorder\record.txt", 'a')
record_file.write(f"SHUTDOWN {total_time}\n")
record_file.close()
