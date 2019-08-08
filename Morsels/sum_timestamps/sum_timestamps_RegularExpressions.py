import re


TIME_RE = re.compile(r'''
    ^
    (?:
        ( \d + )
        :
    )?
    ( \d + )
    :
    ( \d + )
    $
''', re.VERBOSE)


def parse_time(time_string):
    hours, minutes, seconds = TIME_RE.search(time_string).groups()
    return int(hours or 0)*3600 + int(minutes)*60 + int(seconds)


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:01d}:{seconds:02d}"


def sum_timestamps(timestamps):
    return format_time(sum(parse_time(t) for t in timestamps))

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
