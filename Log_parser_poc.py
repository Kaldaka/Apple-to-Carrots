import sys
import re

log_list = "1: View total number of IP's" \
           "\n2: View list of IP's" \
           "\n3: View number of unique IP's" \
           "\n4: View List of unique IP's"

def handler(file_name):
    print(file_name)
    if "pcap" in file_name:
        pcap_formatter(file_name)
    elif "log" in file_name:
        log_formatter(file_name)
    else:
        print("else block")


def pcap_formatter(file_name):
    print("in pcap formatter")


def log_formatter(file_name):
    log = file_name.readlines()
    print("What information would you like to view?" + log_list)
    match input():
        case 1:
            counter = 0;
            for lines in log:
                if ".*\..*\..*\.*." in lines:
                    counter += 1
        case 2:
            for lines in log:
                if ".*\..*\..*\.*." in lines:



def main():
    reading_file = True
    print("Please enter the name or path of log you wish to use.")
    while reading_file:
        try:
            file_name = "C:\\Users\\ellio\\PycharmProjects\\pythonProject\\access_log"  # input()
            reading_file = False
        except FileNotFoundError:
            print("Invalid file name or location. Please try again.")
    open_file = open(file_name)
    handler(file_name)
    open_file.close()


if __name__ == "__main__":
    main()
