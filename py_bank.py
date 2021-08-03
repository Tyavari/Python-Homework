# import modules
import os
import csv

#importing statistics for minimum, maximum and average calculations
import statistics as st

#use empyt lists to store data
month_list = []
amount_list = []
difference = []
print("hello")
print(os.getcwd())

#define csv and txt path 
py_bank_data = os.path.join('budget_data.csv')
py_bank_txt = os.path.join('py_bank_analysis')

with open (py_bank_data, 'r') as pybankdata:
    pybankfinal = csv.reader(pybankdata, delimiter= ',')
    pybankfinal =list( pybankfinal)
    
    rows =  pybankfinal[1:]
    profit_loss = 0 
    months_count = len(rows)
    profit_max = 0
    profit_min = 0 
    print(f' there are {months_count} months in the data set')

    for row in rows: 
        profit_loss =  int(row[1]) + profit_loss
        
    print(f' Total profit/loss is {profit_loss}')

    for row in rows: 
        if int(row[1]) > profit_max:
            profit_max = int(row[1])
    print(f' Highest profit over a month was $ {profit_max}')

    for row in rows: 
        if int(row[1]) < profit_min:
            profit_min = int(row[1])
    print(f' Highest lost over a month was $ {profit_min}')

average_profit = profit_loss/ months_count
print(f' The average profit over the period is ${average_profit: .2f}')

