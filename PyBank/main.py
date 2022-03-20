# Import os module to create file paths across operating systems
import os

# Import csv module to read imported csv file
import csv

# Store file path to csv study file as variable
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create list for storing each month/year in csv file
monthyear = []

# Create list for storing each month's profit/loss change
profitchanges = []

# Create list for storing the results of our analysis
resultslist = []

# Create variables for counting number of rows (months) and total profit/loss
rowcount = 0
total = 0

# Creat variables for calculating each month's profit/loss change
lastrowtotal = 0
profitchange = 0

# Open our csv file and separate data using comma delimiter
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # Skip the header row (no figures for calculation)
    csvheader = next(csvreader)

    # For each row in our csv file:
    for rows in csvreader:
        # Add row (month) to a cumulative count in our assigned variable
        rowcount = rowcount + 1

        # Calculate cumulative profit/loss total, storing increasing figure in our assigned variable
        total += int(rows[1])

        # Store the row's month/year in our assigned list
        monthyear.append(rows[0])

        # Calculate each month's change in profit/loss (current month minus last month) and
        # store the value in our assigned list
        profitchange = int(rows[1]) - lastrowtotal
        profitchanges.append(profitchange)

        # Store the current month's profit/loss for the next month's (row's) change calculation
        lastrowtotal = int(rows[1])

# Since our data set's first row (month/year) has no prior period for profit/loss change
# calculation, toss its false values
monthyear.pop(0)
profitchanges.pop(0)

# Calculate average profit/loss change: sum of our profit/loss change list divided by
# the list's count, and round to two digits
avgchange = round(sum(profitchanges) / len(profitchanges), 2)

# Determine the index number for the greatest increase/decrease profit changes (max/min)
greatinc = profitchanges.index(max(profitchanges))
greatdec = profitchanges.index(min(profitchanges))

# Store assembled reporting data to a list for our analysis tables
resultslist.append("Financial Analysis")
resultslist.append("----------------------------")
resultslist.append(f"Total Months: {rowcount}")
resultslist.append(f"Total: ${total}")
resultslist.append(f"Average Change: ${avgchange}")
resultslist.append(f"Greatest Increase in Profits: {monthyear[greatinc]} (${max(profitchanges)})")
resultslist.append(f"Greatest Decrease in Profits: {monthyear[greatdec]} (${min(profitchanges)})")

# Store file path for our txt analysis file as variable
results_txt = os.path.join("Analysis", "results.txt")

# Export our analysis list to the txt file
with open (results_txt, 'w') as textfile:
    for results in resultslist:
        textfile.write(results)
        textfile.write('\n')

# Print our analysis list to the terminal
for results in resultslist:
    print(results)