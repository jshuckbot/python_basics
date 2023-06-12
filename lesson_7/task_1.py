import os
from pathlib import Path


def group_rename(count_digit: int, extension: str, new_extension: str, range_file_name: list[int], final_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(
                f"{file.split('.')[0][range_file_name[0]:range_file_name[1]]}{final_name}{count:0>{count_digit}}.{new_extension}")
