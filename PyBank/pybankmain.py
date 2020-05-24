#imports
import os
import csv
# Set path for file
budgetdata = os.path.join("..", "Resources", "budget_data.csv")
monthscounter = 0
profittotal = 0
previousnet = 0
monthchange = []
netchangelist = []
greatestincrease = ["",0]
greatestdecrease = ["",9999999999999999]
#open the file
with open(budgetdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    #skipping the the headers
    header = next(csvreader)
    #skipping the first row of data
    firstrow = next(csvreader)
    #Counting how many months in the data
    monthscounter +=1
    profittotal += int(firstrow[1])
    previousnet = int(firstrow[1])
    for row in csvreader:
        monthscounter +=1
        #adding up the profit/loss column
        profittotal += int(row[1])
        #tracking net change
        netchange = int(row[1])- previousnet
        previousnet = int(row[1])
        #creating a list of netchange values
        netchangelist = netchangelist + [netchange]
        monthchage = monthchange + [row[0]]
        #calculating Greatest Increase
        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
        #Calculating Greatest Decrease
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange
netmonthlyaverage = sum(netchangelist)/len(netchangelist)
print("Financial Analysis")
print("--------------------------")
print("Total Months:" + " ",int(monthscounter))
print("Total:" + " " + "${:,.2f}".format(profittotal))
print("Average Change:" + " " + "${:,.2f}".format(netmonthlyaverage))
print("Greatest Increase in Profits:" + " "  + str(greatestincrease))
print("Greatest Decrease in Profits:" + " "  + str(greatestdecrease))

output_path = os.path.join("..", "Resources", "bankresults.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')