#import modules
import os
import csv

#Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip Header row 
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
    
    #loop through each row to add up total amount of months and calculate Net Total for P/L column
    for row in csvreader:
        month_count += 1
        monthly_amount = int(row[1])
        net_total += monthly_amount        
      
        profit = int(row[1])
        if previous_profit != 0:
            change = profit - previous_profit
            total_change += change
            change_count += 1
            
            #calculating Greatest Increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
                
        previous_profit =  profit
        
    average_change = total_change / change_count if change_count > 0 else 0
    month_total = month_count
    
    print('Financial Analysis');
    print('-----------------------------');
    print(f'Total Months: {month_total}');
    print(f'Total: ${net_total}');
    print(f"Average Change: ${average_change:.2f}");
    print(f'Greatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})')    
    print(f'Greatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})')    
      
  
  
    #Specify location / folder for new analysis txt file
    outpath = os.path.join('analysis', 'PyBank_Analysis.txt')

    with open(outpath, 'w') as f:
        print('Financial Analysis', file=f)
        print('-----------------------------', file=f)
        print(f'Total Months: {month_total}', file=f)
        print(f'Total: ${net_total}', file=f)
        print(f'Average Change: ${average_change:.2f}', file=f)
        print(f'Greatest Increase in Profits: {greatest_increase_month}: (${greatest_increase})', file=f)    
        print(f'Greatest Decrease in Profits: {greatest_decrease_month}: (${greatest_decrease})', file=f)   