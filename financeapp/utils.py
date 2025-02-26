def postTaxSal(salary):
    if salary < 12571:
        return salary
    elif salary > 12570 and salary < 50271:
        return ((salary-12570) * 0.8) + 12570
    elif salary > 50270 and salary < 100001:
        return ((salary-50270) * 0.6) + (37700 * 0.8) + 12570
    elif salary > 100000 and salary < 125141:
        return ((salary-100000) * 0.4) + (49730 * 0.6) + (37700 * 0.8) + 12570
    elif salary > 125140:
        return ((salary-125150) * 0.55)+(74870 * 0.6) + (37700 * 0.8) + 12570

def nationalInsurance(salary):
    monthly = salary/12
    if monthly > 1048:
        #Removes first 1048
        if monthly > 4189:
            first = 3140.99 * 0.92
            second = (monthly-4189) * 0.94
            return (first+second+1048)*12
        else:
            first = (monthly-1048)*0.92
            return (first+1048)*12