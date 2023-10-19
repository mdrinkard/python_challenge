# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path(r'C:\Users\Micha\Documents\Module 2 Hwk\python_challenge\Pyramen\Resources\menu_data.csv')
sales_filepath = Path(r'C:\Users\Micha\Documents\Module 2 Hwk\python_challenge\Pyramen\Resources\sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu_data = []
sales_data = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath) as m_csvfile:
    next(m_csvfile)
    m_reader = csv.reader(m_csvfile)
    menu_data = list(m_reader)
# @TODO: Read in the sales data into the sales list
with open(sales_filepath) as s_csvfile:
    next(s_csvfile)
    s_reader = csv.reader(s_csvfile)
    sales_data = list(s_reader)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for s in sales_data:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(s[3])
    menu_item = s[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report.keys():
        report[menu_item] = {'count' : quantity, 'revenue' : 0, 'cost' : 0, 'profit' : 0}
        # print('first',menu_item,report)
    else:
        report[menu_item]['count'] += quantity
        # print('add',menu_item,report)
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for m in menu_data:
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        price = float(m[3])
        cost = float(m[4])
        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        
        if menu_item in m:
            
            # @TODO: Print out matching menu data
            # print('looking for ',menu_item,'found', m[0], 'sold at',price,'cogs', cost, 'profit', profit)
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]['revenue'] = price * report[menu_item]['count']
            report[menu_item]['cost'] = cost * report[menu_item]['count']
            report[menu_item]['profit'] = profit * report[menu_item]['count']
        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else: 
            continue


    # @TODO: Increment the row counter by 1
    row_count += 1
   
    
# @TODO: Print total number of records in sales data
print(len(report.keys()))


# @TODO: Write out report to a text file (won't appear on the command line output)

with open('report.txt', 'w') as txt_file:
    for item, metrics in report.items():
        txt_file.write(f'{item} {metrics}\n')
txt_file.close()
