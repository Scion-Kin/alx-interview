#!/usr/bin/python3
''' This defines a program to parse logs in real time '''

import sys
import re
import signal

regex = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] \"GET \/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)'

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_lines = 0
file_size = 0

try:
    for line in sys.stdin:
        total_lines += 1

        match = re.fullmatch(regex, line.strip())
        if match:
            stat_code = int(match.group(2))
            in_file_size = int(match.group(3))
            file_size += in_file_size

            if stat_code in status_codes:
                status_codes[stat_code] += 1

            if total_lines % 10 == 0:
                print(f"File size: {file_size}")
                for key, val in sorted(status_codes.items()):
                    print(f"{key}: {val}")

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for key, val in status_codes.items():
        print(f"{key}: {val}")

