from datetime import datetime as dt
import calendar
import getopt, sys

import numpy as np

import pandas
import pandas as pd
import os
import pathlib
import numpy
from functions import *
from hours import *
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def print_help():
    print("This tool is designed to keep track of working hours.")
    print("It can track both daily work per month, and monthly totals")
    print("Here are the following command line arguments:")
    print("-h | --help\t\t\t Print this help")
    print("-a | --add\t\t\t Add a new entry to the database.")
    print("-r | --remove <DD/MM/YYYY>\t Remove entry from database, at the given date. The date needs to be in the DD/MM/YYYY format")
    print("-m | --month <MM/YYYY>\t Analyze the desired month, and plot the entries")
    print("-t | --total\t\t\t Compare all of the monthes in the database")


def add_entry(db_path):
    df = pd.read_csv(db_path, index_col='Date')
    date = input("Please enter the date of the new entry\n[DD/MM/YYYY] : ")
    date = dt.strptime(date, '%d/%m/%Y').date()
    data = input("Enter the amount of hours worked, or type 's' in case of sick leave\n")
    try:
        is_sickleave = data.lower().split()[0][0]
    except:
        print("Unable to parse the data, please insert data according to the specified formatting and try again.")
        exit()
    if is_sickleave == 's':
        hours = numpy.nan
        overtime = numpy.nan
        sick = True
        in_office = False
    else:
        try:
            hours = int(data)
        except:
            print("Unable to parse the data, please insert data according to the specified formatting and try again.")
            exit()
        if (hours > 9):
            overtime = hours - 9
        else:
            overtime = 0
        sick = False
        in_office = input("Were you in-office?\n[Y/n] : ")
        if (in_office == ''):
            in_office = True
        else:
            if (in_office.lower().split()[0][0] == 'y'):
                in_office = True
            else:
                in_office = False
    df.loc[date] = [hours, overtime, in_office, sick]
    df.index = pandas.to_datetime(df.index, format='%Y-%m-%d')
    df = df.sort_values(by='Date')
    df.to_csv(path_or_buf=db_path, index=True)
    print("The entry was added successfully")




def print_df(db_path):
    df = pandas.read_csv(db_path)
    print(df)

def remove_entry(db_path, remove_date):
    df = pandas.read_csv(filepath_or_buffer=db_path)
    df.drop(labels=df.loc[df['Date'] == remove_date].index, inplace=True)
    df.to_csv(path_or_buf=db_path, index=False)


def analyze_month(db_path, month, year):
    df = pandas.read_csv(filepath_or_buffer=db_path, index_col='Date')
    start_month = "{}-{:02d}-{:02d}".format(year, month, 1)
    end_month = "{}-{:02d}-{:02d}".format(year, month, 31)
    df = df.loc[df.index >=start_month]
    df = df.loc[df.index <=end_month]
    df['sick'] = 0
    df.loc[df['Sick leave'] == True,'sick'] = 8.6
    df['Regular'] = df['Hours Worked'] - df['Overtime']
    plt.bar(df.index, df['Regular'], width=0.35, label='Regular Working Hours', color='green')
    plt.bar(df.index, df['Overtime'], width=0.35, label='Overtime', color='red', bottom=df['Regular'])
    plt.bar(df.index, df['sick'], width=0.35, label='Sick leave', color='purple')
    plt.xlabel("Date")
    plt.title("Monthly summary for {}, {}".format(calendar.month_name[start_work.month], year))
    plt.legend(loc='upper right')
    plt.show()
    estimated_salary = (salary * df['Regular'].sum() + salary * 1.25 * df['Overtime'].sum() + travel*len(df) + 8.6 * len(df.loc[df['Sick leave'] == True])) * 0.62
    print("The estimated salary for {}/{} is {}".format(month, year, estimated_salary))
def compare_all(db_path):
    df = pandas.read_csv(filepath_or_buffer=db_path, index_col='Date')
    df['Date'] = df.index

    def fix_string(x):
        x = x.split('-')[:2]
        x = '-'.join(x)
        return x

    df['Date'] = df['Date'].apply(fix_string)
    df['sick'] = 0
    df.loc[df['Sick leave'] == True, 'sick'] = 8.6
    df['Regular'] = df['Hours Worked'] - df['Overtime']
    dates = df['Date'].unique()
    time = pandas.DataFrame(columns=['Date', 'Sick', 'Regular', 'Overtime', 'Salary'])
    for date in dates:
        start_month = "{}-{:02d}".format(date, 1)
        end_month = "{}-{:02d}".format(date, 31)
        dfx = df.loc[df.index >= start_month]
        dfx = dfx.loc[dfx.index <= end_month]
        regular = dfx['Regular'].sum()
        overtime = dfx['Overtime'].sum()
        sick = len(dfx.loc[dfx['Sick leave'] == True])
        estimated_salary = (salary * regular + salary * 1.25 * overtime + travel * len(dfx.loc[dfx['In-office'] == True]) + 8.6 * sick * salary ) * 0.62
        time.loc[len(time) + 1] = [date, sick, regular, overtime, estimated_salary]
    print(time)
    figure, axis = plt.subplots(2, 2)
    axis[0,0].bar(time['Date'], time['Regular'], width=0.35, label='Regular Working Hours', color='green')
    axis[0,0].bar(time['Date'], time['Overtime'], width=0.35, label='Overtime', color='red', bottom=time['Regular'])
    axis[0,1].bar(time['Date'], time['Sick'], width=0.35, label='Sick', color='purple')
    axis[0, 1].set_xlabel("Month")
    axis[0, 0].set_xlabel("Month")
    axis[0, 0].set_title("Working hours across all of the months")
    axis[0, 1].set_title("Sick leave days across all of the months")
    axis[1, 0].bar(time['Date'], time['Salary'], width=0.35, label='Estimated Salary')
    axis[1, 0].set_title("Estimated salary across all of the monthes")
    axis[1, 0].set_xlabel("Month")
    plt.show()
