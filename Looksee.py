#!/usr/bin/env python3
''' IMPORT STATEMENTS '''
import re
import random

''' Instance data variables and hard code '''
# TODO: Add more options (show user agent strings?), add/combine options to show least + most occurring IP's

print('''\n\n\n.____                  __                          
|    |    ____   ____ |  | __  ______ ____   ____  
|    |   /  _ \ /  _ \|  |/ / /  ___// __ \_/ __ \ 
|    |__( <_|_>| <_|_>)    <  \___ \\\  ___/\  ___/ 
|_______ \____/ \____/|__|_ \/____  >\___  >\___  >
        \/                 \/     \/     \/     \/ ''')

internet_log_menu = "\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
            \n\u0413--Please enter a number from the following menu:\
            \n|  1: View IP occurrance information.\
            \n|  2: Response code information.\
            \nL--0: Back"

internet_log_occurrance_menu = "\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
                      \n\u0413--Please enter the occurance information you wish to view:\
                      \n|  1: View least occurring IP's.\
                      \n|  2: View highest occurring IP.\
                      \n|  3: View IP occurrances (Warning: Large output!)\
                      \nL--0: Back"

internet_log_response_menu = "\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
            \n\u0413--Please enter the response code information you wish to view:\
                              \n|  1: View all response codes generated from a given IP\
                              \n|  2: View all IPs associated with a given response code\
                              \nL--0: Back"

network_log_menu = "\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
            \n\u0413--Please enter a number from the following menu:\
                    \n|  1: View communication information given an ip of interest\
                    \nL--0: Back"

srcip_menu = "\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
            \n\u0413--How many entries would you like to see?\
                    \n|  1: All\
                    \n|  2: Print to file\
                    \nL--0: Back"

main_choice = ""

int_log_ip_location = 0
int_log_resourse_location = 6
int_log_resonse_location = 8
net_log_src_ip_location = 2
net_log_dst_ip_location = 4
net_log_src_port_location = 3
net_log_dst_port_location = 5
net_log_prtcl_location = 8

found = False
while not found:
    try:
        intake_file = input(
            "\n\n\nPlease enter the complete file name or path: \n")
        open_file = open(intake_file)
        found = True
    except FileNotFoundError:
        print(
            "File name or path may be wrong. Please check and enter again.\n")
file = open_file.readlines()
file = sorted(file)
''' HELPER FUNCTIONS (IF NECESSARY) '''
# Returns the IP that appears the least (needs tweaking, adjust to return ALL singles?)


def internet_log_main():
    option = ""
    correct = "012"
    while option != "0":
        print(internet_log_menu)
        option = input("[")
        if option in correct:
            if option == '1':
                ip_occurrance_main()
            elif option == '2':
                ip_response_main()
            elif option == '0':
                main()
        else:
            print("Please restrict input to the given options\n")


def network_log_main():
    option = ""
    correct = "01"
    while option != "0":
        print(network_log_menu)
        option = input("[")
        if option in correct:
            if option == '1':
                srcip()
            elif option == '0':
                main()
        else:
            print("Please restrict input to the given options\n")


def ip_occurrance_main():
    option = ""
    correct = "0123"
    while option != "0":
        print(internet_log_occurrance_menu)
        option = input("[")
        if option in correct:
            if option == "1":
                least_occurring_ip()
            elif option == "2":
                most_occurring_ip()
            elif option == "3":
                ip_and_occurrance()
            elif option == "0":
                internet_log_main()
        else:
            print("Please restrict input to the given options\n")


def ip_response_main():
    option = ""
    correct = "012"
    while option != "0":
        print(internet_log_response_menu)
        option = input("[")
        if option in correct:
            if option == "1":
                sort_by_ip()
            elif option == "2":
                sort_by_response()
            elif option == "0":
                internet_log_main()
        else:
            print("Please restrict input to the given options\n")


def sort_by_ip():
    ip = input(
        "Please enter the ip address you wish to query for response codes:\n")
    int_ip_response_dict = {}
    for line in file:
        line = line.rstrip().split()
        if ip in line[int_log_ip_location]:
            if (line[int_log_resourse_location],
                    line[int_log_resonse_location]) in int_ip_response_dict:
                int_ip_response_dict[line[int_log_resourse_location],
                                     line[int_log_resonse_location]] += 1
            else:
                int_ip_response_dict[line[int_log_resourse_location],
                                     line[int_log_resonse_location]] = 1
    if int_ip_response_dict:
        print('\n------------------------------------------------------------------\n' + str(ip) +
              " Requested these resources/received these responses:")
        for key, value in int_ip_response_dict.items():
            print('\n' + str(key[0]) + ', ' + str(key[1]) + ', ' + str(value) +
                  ' times.' + '\n' +
                  '------------------------------------------------------------------')


def sort_by_response():
    response_code = input(
        "Please enter the response code you wish to query: \n")
    print("------------------------------------------------------------------")
    int_ip_response_dict = {}
    for line in file:
        line = line.rstrip().split()
        if line[int_log_ip_location] in int_ip_response_dict:
            int_ip_response_dict[line[int_log_ip_location],
                                 line[int_log_resonse_location]] += 1
        else:
            int_ip_response_dict[line[int_log_ip_location],
                                 line[int_log_resonse_location]] = 1
    sorted_response_dict = sorted(int_ip_response_dict.items(),
                                  key=lambda x: int(x[0][1]))
    present = 0
    for ip_response_pair in sorted_response_dict:
        if ip_response_pair[0][1] == response_code:
            print("Response code " + response_code + " is generated by " +
                  ip_response_pair[0][0])
            present += 1
    if present == 0:
        print("\nResponse code not generated by any IPs on the given log.")


# Returns the IP that appears the least
def least_occurring_ip():
    int_ip_dict = {}
    for line in file:
        line = line.rstrip().split()
        if line[int_log_ip_location] in int_ip_dict:
            int_ip_dict[line[int_log_ip_location]] += 1
        else:
            int_ip_dict[line[int_log_ip_location]] = 1
    x = min(int_ip_dict.items())
    print("------------------------------------------------------------------" + "\n" + "IP Address: " +
          str(x[0]) + ' - ' + " Appearances: " + str(x[1]))


# Returns the IP that appears the most
def most_occurring_ip():
    int_ip_dict = {}
    for line in file:
        line = line.rstrip().split()
        if line[int_log_ip_location] in int_ip_dict:
            int_ip_dict[line[int_log_ip_location]] += 1
        else:
            int_ip_dict[line[int_log_ip_location]] = 1
    x = max(int_ip_dict.items())
    print("------------------------------------------------------------------" + "\n" +
          "Most occurring IP Address: " + str(x[0]) + ' - ' +
          " Appearances: " + str(x[1]))


# Returns all IP's and how many times they appear in the log in descending order
def ip_and_occurrance():
    int_ip_dict = {}
    for line in file:
        line = line.rstrip().split()
        if line[int_log_ip_location] in int_ip_dict:
            int_ip_dict[line[int_log_ip_location]] += 1
        else:
            int_ip_dict[line[int_log_ip_location]] = 1
    sort_mydict = sorted(int_ip_dict.items(), key=lambda x: x[1])
    for i in sort_mydict:
        print("IP Address: " + str(i[0]) + "  Appearances: " + str(i[1]))


def srcip():
    valid_ip = re.compile(
        '''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'''
    )
    valid = False
    while not valid:
        net_ip_dict = {}
        net_log_ip_of_interest = input('Input IP of interest: \n')
        if net_log_ip_of_interest == "0":
          network_log_main()
          valid = True
          break
        elif valid_ip.match(net_log_ip_of_interest):
            for line in file:
                line = line.rstrip().split(';')
                if net_log_ip_of_interest in line[net_log_src_ip_location]:
                  if (line[net_log_dst_ip_location], line[net_log_dst_port_location]) in net_ip_dict:
                    net_ip_dict[line[net_log_dst_ip_location], line[net_log_dst_port_location]] += 1
                  else:
                    net_ip_dict[line[net_log_dst_ip_location], line[net_log_dst_port_location]] = 1
            if net_ip_dict:
                resultentries = 0
                for i in net_ip_dict.values():
                    resultentries += int(i)
                print(net_log_ip_of_interest + ' communicates ' +
                      str(resultentries) + ' times')
                print(srcip_menu)
                choice = input("[")
                if choice == "1":
                    for key, value in sorted(net_ip_dict.items()):
                        print(net_log_ip_of_interest + " communicated to " +
                              str(key[0]) + ' on port ' + str(key[1]) + '  ' +
                              str(value) + ' times')
                elif choice == "2":
                    print()

                elif choice == "3":
                  print()
                elif choice == "4":
                  print()
                elif choice == "5":
                    print("\nWriting to a file instead...")
                    out = open("net_log_communication_output.txt", "a")
                    for key, value in net_ip_dict.items():
                        out.write(net_log_ip_of_interest +
                                  " communicated to " + str(key[0]) +
                                  ' on port ' + str(key[1]) + '  ' +
                                  str(value) + ' times' + "\n" + "\n")
                    print("\nDone!")
                    out.close()
                    valid = True
                elif choice == "0":
                  network_log_main()
                  break;
        else:
            print("Please enter a valid IP")


def main():
    print("\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------------------------\
            \n\u0413--Please choose the type of file you are trying to analyze: \
        \n|  1: Internet access log \
        \n|  2: Network log \
        \nL--0: Quit")
    main_choice = ""
    choices = "012"
    while main_choice != "0":
        main_choice = input("[")
        if main_choice in choices:
          if main_choice == "1":
              internet_log_main()
          elif main_choice == "2":
              network_log_main()
          elif main_choice == "0":
            quit()
        else:
          print("Please restrict input to the given options\n")

    open_file.close()


if __name__ == "__main__":
    main()