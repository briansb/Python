def sum_timestamps(tstamps):

    sum_minute = sum_second = 0
    for x in tstamps:
        minute, second = x.split(':')
        sum_minute += int(minute)
        sum_second += int(second)
        
    sum_minute += int(sum_second / 60)
    sum_second = sum_second % 60
    
    return str(sum_minute) + ":" + str(sum_second).rjust(2,'0')






def main():
    time_stamps = ['5:32','4:37']
    print(time_stamps)
    print(sum_timestamps(time_stamps))    

if __name__ == '__main__':
    main()
