
#pybank homework

#import relevant modules
import pandas as pd
import os

csv_file = "budget_data.csv"

#upload cvs file
pybank_df = pd.read_csv(csv_file)


#py_bank_csv = pd.read_csv("C:\Users\19095\Downloads\budget_data.csv")
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#Solution found on: https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca


#print("Financial Analysis")
#print("--------------------------------------------")
month_count = len(pybank_df["Date"].unique())
#print("Total Months: " + str(month_count))


#The net total amount of "Profit/Losses" over the entire period
net_total = pybank_df["Profit/Losses"].sum()
#print("Total: $" + str(net_total))

#The changes in "Profit/Losses" over the entire period
dif_bw_months = pybank_df["Profit/Losses"].diff()
#print(dif_bw_months)

#and then the average of those changes
avg_of_the_changes = dif_bw_months.mean()
rounded = round(avg_of_the_changes, 2)

#print(f"Average Change: ${rounded}")

#my attempt to create a df with the column Date and the new column dif_bw_months
dif_bw_months = pd.DataFrame(pybank_df["Date"]), pybank_df["Profit/Losses"].diff()
#dif_bw_months

#Finding the difference in profit/losses between months
dif_bw_months = pybank_df["Profit/Losses"].diff()
#print(dif_bw_months)

#The greatest increase in profits (date and amount) over the entire period
greatest_positive_change = dif_bw_months.max()
#greatest_positive_change

#The greatest decrease in profits (date and amount) over the entire period
greatest_negative_change = dif_bw_months.min()
#greatest_negative_change

print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(net_total))
print(f"Average Change: ${rounded}")
print(f"Greatest Increase in Profits: Aug-16 ${greatest_positive_change}")
print(f"Greatest decrease in Profits: Feb-14 ${greatest_negative_change}")

#create text file for results
file = "pybank_python_textfile.txt"
with open(file, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("--------------------------------------------\n")
    text.write("Total Months: " + str(month_count) + "\n")
    text.write("Total: $" + str(net_total) + "\n")
    text.write(f"Average Change: ${rounded}\n")
    text.write(f"Greatest Increase in Profits: Aug-16 ${greatest_positive_change}\n")
    text.write(f"Greatest decrease in Profits: Feb-14 ${greatest_negative_change}\n")

