#!/usr/bin/python3
"""
Module containing Student class
"""


import sys


"""
Something
"""
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
lines_processed = 0

"""
Something more
"""
try:
    for line in sys.stdin:
        lines_processed += 1
        line = line.strip()
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code = int(parts[-2])
            if status_code in status_code_count:
                status_code_count[status_code] += 1
        if lines_processed % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{code}: {count}")
