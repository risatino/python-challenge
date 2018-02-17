# Dependencies
import os
import csv

# Try another dependency I learned about from a co-worker http://effbot.org/librarybook/sys.htm 
import sys

# Paths
csvpath1 = os.path.join('Resources', 'budget_data_1.csv')
csvpath2 = os.path.join('Resources', 'budget_data_2.csv')

# My Variables
total_months = 0
total_revenue = 0
greatest_increase = -sys.maxsize - 1
greatest_increase_date = ""
greatest_decrease = sys.maxsize
greatest_decrease_date = ""

# Read CSV File budget_data_1.csv
with open(csvpath1, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    # Count months, finding total revenue, and find greatest increase and decrease in revenue
    for row in csvreader1:
        total_months += 1
        total_revenue += int(row[1])
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

# Read CSV File budget_data_2.csv
with open(csvpath2, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    # Count months, finding total revenue, and find greatest increase and decrease in revenue
    for row in csvreader2:
        total_months += 1
        total_revenue += int(row[1])
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

# Calculate average revenue change
average_change = round(total_revenue/total_months, 2)

# Printing results to terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")

# Create New File
output_file = open("Reports/financial_analysis.txt", "w")

# Write This Inside New File
output_file.write("Financial Analysis \n")
output_file.write("-------------------------------------------- \n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
output_file.write("Average Revenue Change: $" + str(average_change) + "\n")
output_file.write("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
output_file.write("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")

# Not sure...but I think I can do this.
# Zip lists together
# cleaned_csv = zip(title, price, subscribers, reviews, review_percent,length)

# Set variable for output file
# output_file = os.path.join("web_final.csv")

# Open the output file
# with open(output_file, "w", newline="") as datafile:
#    writer = csv.writer(datafile)
    
   # Write the header row
#    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                     "Percent of Reviews", "Length of Course"])

   # Write in zipped rows
#    writer.writerows(cleaned_csv)

