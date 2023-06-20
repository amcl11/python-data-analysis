#import modules
import os
import csv

#Establish path to collect the CSV file from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#open the CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip /store Header row 
    csv_header = next(csvreader)
    
    #create all variables 
    month_count = 0
    net_total = 0
    previous_profit = 0
    total_change = 0
    change_count = 0
    increase = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    
    #loop through each row to add up total amount of months 
    for row in csvreader:
        month_count += 1
        monthly_amount = int(row[1])
        net_total += monthly_amount        
      
        # calculate Net Total for P/L column
        profit = int(row[1])
        if previous_profit != 0:
            change = profit - previous_profit
            total_change += change
            change_count += 1
            
            #calculating Greatest Increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            
            #calculating Greatest Decrease
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
                
        previous_profit = profit
        
    #calculate average P/L change over the period     
    average_change = total_change / change_count if change_count > 0 else 0
    month_total = month_count
    
    #print found values using spaces and lines per the example in BootCampSpot making it easier to read. 
    print('\nFinancial Analysis');
    print('\n-----------------------------');
    print(f'\nTotal Months: {month_total}');
    print(f'\nTotal: ${net_total}');
    print(f'\nAverage Change: ${average_change:.2f}');
    print(f'\nGreatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})')    
    print(f'\nGreatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})\n')    
      
    #Specify location / folder for new analysis txt file to be written to 
    outpath = os.path.join('analysis', 'PyBank_Analysis.txt')

    with open(outpath, 'w') as f:
        print('\nFinancial Analysis', file=f)
        print('\n-----------------------------', file=f)
        print(f'\nTotal Months: {month_total}', file=f)
        print(f'\nTotal: ${net_total}', file=f)
        print(f'\nAverage Change: ${average_change:.2f}', file=f)
        print(f'\nGreatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})', file=f)    
        print(f'\nGreatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})\n', file=f)   