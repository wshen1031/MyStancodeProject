"""
File: babynames.py
Name: Willy
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    # 把內容加入name_data的動作
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    year_rank = {year: rank}
    # 把輸入的year和rank先做成dictionary
    # 用兩個if來篩選出同一年有兩個的名字，並比對他們的rank,找出較低者
    if name not in name_data:
        # 如果輸入的name在name_date找不到（第一次輸入）
        name_data[name] = year_rank
        # {name:{year:rank}, ...}
    else:
        name_data_year_rank = name_data[name]  # {'2010': '57', '2000': '104'}
        if year in name_data_year_rank:
            if int(name_data[name][year]) > int(rank):
                name_data[name][year] = int(rank)
        else:
            # 塞入新資料
            name_data[name][year] = rank


def add_file(name_data, filename):
    # 讀取檔案裡面的內容,使其可以儲存在name_data這個dictionary裏面
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    line_count = 0
    FILE = f'{filename}'
    with open(FILE,'r') as f:
        for line in f:
            tokens = line.split(",")
            if line_count == 0:
                year = tokens[0]
                year = year.strip()
            else:
                rank = tokens[0]
                rank = rank.strip()
                name1 = tokens[1]
                name1 = name1.strip()
                name2 = tokens[2]
                name2 = name2.strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)
            line_count += 1


def read_files(filenames):
    # 讀取到每一個包含資料的檔案
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for item in filenames:
        filename = item
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    # 在資料庫這個dictionary裡找到要找的名字
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_name = []
    for key in name_data:
        if target.lower() in key.lower():
            matching_name.append(key)
    return matching_name


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
