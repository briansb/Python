#   My solution
# -----------------------
##def sum_timestamps(tstamps):
##
##    sum_minute = sum_second = sum_hour = 0
##    for x in tstamps:
##        if x.count(':') == 2:
##            hour, minute, second = x.split(':')
##        else:
##            minute, second = x.split(':')
##            hour = 0
##            
##        sum_hour += int(hour)
##        sum_minute += int(minute)
##        sum_second += int(second)
##        
##    sum_minute += int(sum_second / 60)
##    sum_second = sum_second % 60
##
##    sum_hour += int(sum_minute / 60)
##    sum_minute = sum_minute % 60
##    
##    return str(sum_hour) + ":" + str(sum_minute).rjust(2,'0') + ":" + str(sum_second).rjust(2,'0')


#  Better solution
# ----------------------
def parse_time(time_string):
    sections = time_string.split(':')
    try:
        hours, minutes, seconds = sections
    except ValueError:
        hours = 0
        minutes, seconds = sections
    return int(hours)*3600 + int(minutes)*60 + int(seconds)

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:01d}:{seconds:02d}"
    
##def sum_timestamps(timestamps):
##    total_time = 0
##    for time in timestamps:
##        total_time += parse_time(time)
##    return format_time(total_time)

# use generator expression
def sum_timestamps(timestamps):
    total_time = sum(
        parse_time(time)
        for time in timestamps
    )
    return format_time(total_time)



def main():
    time_stamps = ['1:05:32','0:03:37']
    print(time_stamps)
    print(sum_timestamps(time_stamps))
    time_stamps = ['2:03:27','1:08:17','4:28:32']
    print(time_stamps)
    print(sum_timestamps(time_stamps))
    time_stamps = ['4:03:27','2:08:17','1:28:32', '0:45:03']
    print(time_stamps)
    print(sum_timestamps(time_stamps))


if __name__ == '__main__':
    main()
