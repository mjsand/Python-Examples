### this program will represent a progressive tax bracket, and given an income level return the amount of taxes owed

def tax(income):
    
    income_levels = [10000, 30000, 100000, 250000, 500000, 1000000, 10000000]
    tax_rate = [0, 0.10, 0.25, 0.40, 0.50, 0.60, 0.70]
    
    
    if income <= income_levels[0]:
        t = income * tax_rate[0]
        
    elif income <= income_levels[1]:
        t = (income - income_levels[0]) * tax_rate[1]
        
    elif income <= income_levels[2]:
        t = (income - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    elif income <= income_levels[3]:
        t = (income - income_levels[2]) * tax_rate[3] + (income_levels[2] - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    elif income <= income_levels[4]:
        t = (income - income_levels[3]) * tax_rate[4] + (income_levels[3] - income_levels[2]) * tax_rate[3] + (income_levels[2] - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    elif income <= income_levels[5]:
        t = (income - income_levels[4]) * tax_rate[5] + (income_levels[4] - income_levels[3]) * tax_rate[4] + (income_levels[3] - income_levels[2]) * tax_rate[3] + (income_levels[2] - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    elif income <= income_levels[6]:
        t = (income - income_levels[5]) * tax_rate[6] + (income_levels[5] - income_levels[4]) * tax_rate[5] + (income_levels[4] - income_levels[3]) * tax_rate[4] + (income_levels[3] - income_levels[2]) * tax_rate[3] + (income_levels[2] - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    elif income >= income_levels[7]:
        t = (income - income_levels[6]) * tax_rate[7] + (income_levels[6] - income_levels[5]) * tax_rate[6] + (income_levels[5] - income_levels[4]) * tax_rate[5] + (income_levels[4] - income_levels[3]) * tax_rate[4] + (income_levels[3] - income_levels[2]) * tax_rate[3] + (income_levels[2] - income_levels[1]) * tax_rate[2] + (income_levels[1] - income_levels[0]) * tax_rate[1]
        
    effective_tax_rate = (t/income) * 100
    
    print('Amount of tax owed is: $', t, '\nEffective tax rate is: ', effective_tax_rate, '%')


tax(1000000)