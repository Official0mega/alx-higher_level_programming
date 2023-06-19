#!/usr/bin/python3
'''A script that Reads HTTP log entries from standard input,
extracts metrics such as the total file size and the counts of different
..status codes, periodically prints the accumulated statistics.
'''
import re


status_codes_stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
"""To print each status code and its counts...
"""
total_file_size = 0
"""variable keeps track of the commulative sum of the sizes in the HTTP logs
"""
fp = (
    r'\s*(?P<ip>\S+)\s*',
    r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
    r'\s*"(?P<request>[^"]*)"\s*',
    r'\s*(?P<status_code>\S+)',
    r'\s*(?P<file_size>\d+)'
)
"""This tupple contains regular expressions that define the pattern for each
field in the log entry. These expressions that capture the IP address,
date, request, status codem and the file size.
"""
log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
'''This string combines the regular expressions from 'fp' to create a single
regex pattern that matches an entire log entry.
'''


def print_statistics():
    """This function prints the accumulated statistics of the HTTP log.
    It first prints the total file size and then iterates over the sorted keys
...'of status_codes_stats' to print each status code and its count.
    """
    global total_file_size, status_codes_stats
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def get_metrics(line):
    """
    This function retrieves the metrics from a given HTTP log line. It uses
    the regex pattern 'log_fmt' to match the line and extract the status
    code and file size. It increments the 'total_file_size' by the file size
    update the count in 'status_codes_stats' for the corresponding status code
    """
    global total_file_size, log_fmt, status_codes_stats
    resp_match = re.fullmatch(log_fmt, line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        total_file_size += file_size
        if status_code in status_codes_stats.keys():
            status_codes_stats[status_code] += 1


def run():
    """
    This function is the main Entry Point of the script. It reads lines of
    input using the 'input()' function and processes each line by calling
    'get_metrics(line)' to extract the metrics. It keeps track of the line
    number and prints the statistics using 'print_statistics()' every 10 lines
    """
    line_num = 0
    try:
        """The 'try_except' block in this 'run()' function catches a...
        'keyboardInterrupt' or 'EOFError' excepton, which occur when the user
        Interrupts the script with Ctrl+C or when the end of input is reached
        In either case, it calls 'print_statistics()' to print
        ..the final statistics...
        """
        while True:
            line = input()
            get_metrics(line)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics()
    except (KeyboardInterrupt, EOFError):
        print_statistics()


if __name__ == '__main__':
    """
    The 'if__name__ == '__main__':' block ensures that the code inside
    is only executed when the script is run directly and not imported...
    as a module... it calls the 'run()' function to start the log parser
    """
    run()
