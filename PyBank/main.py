# ## Option 1: PyBank

# ![Revenue](Images/revenue-per-lead.jpg)

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset

# * The total amount of revenue gained over the entire period

# * The average change in revenue between months over the entire period

# * The greatest increase in revenue (date and amount) over the entire period

# * The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```

# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv

revenue = 0
months = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]

filepath = os.path.join("raw_data", "budget_data_1.csv")

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    
    

    for row in reader:
        
        months+=1

        revenue += int(row["Revenue"])

        if (int(row["Revenue"]) > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = int(row["Revenue"])

        if (int(row["Revenue"]) < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = int(row["Revenue"])


wfilepath = os.path.join("raw_data", "test.txt")
with open(wfilepath,"w+") as writer:


    writer.write("Financial Analysis\n" )
    writer.write("-" * 28)
    writer.write(f"\nTotal Months: {months}\n")
    writer.write(f"Total Revenue: ${revenue}\n")
    writer.write(f"Average Revenue Change: ${revenue / months}\n")
    writer.write(f"Greatest Increase in Revenue: {greatest_increase}\n")
    writer.write(f"Greatest Decrease in Revenue: {greatest_decrease}\n")

    writer.seek(0) #points file back to beginning before printing
    print(writer.read())


