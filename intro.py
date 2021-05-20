#!/usr/bin/env python3
from datetime import datetime as dt
import calendar
import getopt, sys
import pandas
import os
from functions import *
cfg_path = './hours.py'

# Check  if the user configuration exists
if not os.path.isfile(cfg_path):
    response = input("No user configuration found!\nWould you like to run the configuration? \n[Y/n] : ")
    if (response == ''):
        response = True
    elif (response.lower().split()[0][0] == 'y'):
        response = True
    else:
        response = False
    if response == True:
        print("Fantastic!")
        first_name = input("What is your first name?\n")
        if first_name.lower() == 'michal':
            print("I love you Michal! <3\n")
        last_name = input("What is your last name?\n")
        # Workplace name
        workplace = input("What is your workplace name?\n")
        # Starting date
        start_work = input("When did you start working in your current workplace? Leave empty for today\n[MM/YYYY] : ")
        if (start_work == ''):
            start_work = dt.today().date()
            print(start_work)
        else:
            start_work = dt.strptime(start_work, '%m/%Y')
        # start_work = start_work.date().split('-')[:1]
        print(start_work.date())
        # Salary
        salary = input("What is your hourly salary?\nPress enter to skip\n")
        if (salary ==''):
            salary = False
        else:
            salary = int(salary)
        currency = 'ILS'
        travel = input("What is your received travel expense?\n")
        try:
            travel = float(travel)
        except:
            print("Couldn't parse the inserted float value. Please make sure its valid and try again.")
            exit()
        print("#####\n"*3)
        print("So, to summarize:\nfirst_name:\t{}\nlast_name:\t{}\nWorking at {} since {}, {} for {}{} hourly rate.".format(first_name, last_name, workplace, calendar.month_name[start_work.month], start_work.year, salary, currency))
        print("Nice to meet you!\n")
        print("#####\n" * 3)
        with open(cfg_path, 'w') as f:
            f.write("from datetime import datetime as dt\n")
            f.write("first_name = '{}'\n".format(first_name))
            f.write("last_name = '{}'\n".format(last_name))
            f.write("workplace = '{}'\n".format(workplace))
            f.write("start_work = dt.strptime('{:02d}/{}', '%m/%Y')\n".format(start_work.month, start_work.year))
            f.write("salary = {}\n".format(salary))
            f.write("currency = '{}'\n".format(currency))
            f.write("travel = {}".format(travel))
    else:
        exit()


db_path = pathlib.Path('hours.csv').absolute()
if not os.path.isfile(db_path):
    print("No database is found!\nCreating a new, blank database!")
    df = pandas.DataFrame(columns=[ 'Hours Worked', 'Overtime', 'In-office', 'Sick leave'])
    df.to_csv(path_or_buf=db_path, index=True, index_label='Date')


# Handle Command Line Argument #
argumentList = sys.argv[1:]
# Options
options = "har:m:t"
# Long options
long_options = ["help", "add", "remove=", "month=", "total"]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print_help()
            exit()
        elif currentArgument in ("-a", "--add"):
            add_entry(db_path)
        elif currentArgument in ("-r", "--remove"):
            try:
                remove_date = dt.strptime(currentValue, '%d/%m/%Y').date()
                remove_date = '{}-{:02d}-{:02d}'.format(remove_date.year, remove_date.month, remove_date.day)
            except:
                print("Unable to parse the provided date.\nPlease enter the data according to the specified formatting, and try again")
                exit()
            remove_entry(db_path, remove_date)
        elif currentArgument in ("-m", "--month"):
            try:
                parse_month = dt.strptime(currentValue, '%m/%Y').date()
                month = parse_month.month
                year = parse_month.year
            except:
                print(
                    "Unable to parse the provided month.\nPlease enter the data according to the specified formatting, and try again")
                exit()
            analyze_month(db_path, month, year)
        elif currentArgument in ("-t", "--total"):
            compare_all(db_path)
except getopt.error as err:
    print(str(err))
