import os
import csv
# Set path for file
polldata = os.path.join("..", "Resources", "election_data.csv")
electioninfo = {"Candidates": ["Khan", "Correy","Li","O'Tooley"]}
#set the variables
totalvotes = 0
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0
khanper= 0
correyper = 0
liper = 0
otooleyper = 0
#open the file
with open(polldata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    #skipping the the headers
    header = next(csvreader)
    #using for loop to count the total votes 
    for row in csvreader:
        totalvotes +=1
        #using if statements inside a for loop to count each person vote
        if row[2] == electioninfo["Candidates"][0]:
            khanvotes +=1
        elif row[2] == electioninfo["Candidates"][1]:
            correyvotes +=1
        elif row[2] == electioninfo["Candidates"][2]:
            livotes +=1
        elif row[2] == electioninfo["Candidates"][3]:
            otooleyvotes +=1      
    #using if statement to find winner  
    if khanvotes > correyvotes and khanvotes > livotes and khanvotes > otooleyvotes:
        winner = "Khan"
    elif correyvotes > khanvotes and correyvotes > livotes and correyvotes > otooleyvotes:
        winner = "Correy"
    elif livotes > khanvotes and  livotes > correyvotes and livotes > otooleyvotes:
        winner = "Li"
    else:
        winner = "O'Tooley"

print("Elections Results")
print("----------------------")
print("Total Votes:" + " " + str(totalvotes))
print("----------------------")
#in statements below format numbers to percent
print("Khan:" + " " + "{:.2%}".format(khanvotes/totalvotes) + " " + str(khanvotes))
print("Correy:" + " "+"{:.2%}".format(correyvotes/totalvotes)+ " " + str(correyvotes))
print("Li:" + " " +"{:.2%}".format(livotes/totalvotes)+ " " + str(livotes))
print("O'Tooley:"+ " " + "{:.2%}".format(otooleyvotes/totalvotes)+ " " + str(otooleyvotes))
print("----------------------")
print("Winner:" + " " + winner)
print("----------------------")

output_path = os.path.join("..", "Resources", "election winner.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

  