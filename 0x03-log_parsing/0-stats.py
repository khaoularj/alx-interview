#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


total = 0
count = {'200': 0,
         '301': 0,
         '400': 0,
         '401': 0,
         '403': 0,
         '404': 0,
         '405': 0,
         '500': 0}
count_line = 0

try:
    for line in sys.stdin:
        count_line += 1
        try:
            args = line.split(' ')
            if len(args) > 2:
                status_line = args[-2]
                file_size = args[-1]
                code_status = int(status_line)
                if str(code_status) in count:
                    count[str(code_status)] += 1
                total += int(file_size)
                if count_line == 10:
                    print('File size: {:d}'.format(total))
                    sorted_keys = sorted(count.keys())
                    for key in sorted_keys:
                        value = count[key]
                        if value != 0:
                            print('{}: {}'.format(key, value))
                    count_line = 0
        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    pass

finally:
    print('File size: {:d}'.format(total))
    sorted_keys = sorted(count.keys())
    for key in sorted_keys:
        value = count[key]
        if value != 0:
            print('{}: {}'.format(key, value))
