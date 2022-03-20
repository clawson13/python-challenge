import os

import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

monthyear = []
profitchanges = []

rowcount = 0
total = 0
lastrowtotal = 0
profitchange = 0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    csvheader = next(csvreader)

    for rows in csvreader:
        rowcount = rowcount + 1
        total += int(rows[1])
        monthyear.append(rows[0])
        profitchange = int(rows[1]) - lastrowtotal
        profitchanges.append(profitchange)
        lastrowtotal = int(rows[1])
        
monthyear.pop(0)
profitchanges.pop(0)
avgchange = round(sum(profitchanges) / len(profitchanges), 2)

greatinc = profitchanges.index(max(profitchanges))
greatdec = profitchanges.index(min(profitchanges))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {monthyear[greatinc]} (${max(profitchanges)})")
print(f"Greatest Decrease in Profits: {monthyear[greatdec]} (${min(profitchanges)})")





# DELETE ME: # hot_days = [temperature for temperature in july_temperatures if temperature > 90]

# july_temperatures = [87, 85, 92, 79, 106]
# hot_days = []
# for temperature in july_temperatures:
#     if temperature > 90:
#         hot_days.append(temperature)
# print(hot_days)

# # List Comprehension with conditional
# # hot_days = [temperature for temperature in july_temperatures if temperature > 90]



# for month in cleandatelist
#     print(month)
    


#         # for month in row:
#         #     if month = "Jan"


    
#     # profitloss.append = row[1]

#         print(yearmonth)
#         print(profitloss)
