#Employee Hours exercise


        #Define employee name
def getEmpName():
    empName = input("Enter employee name: ")
    return empName

        #Define hours worked
def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

        #Define hourly rate
def getHourlyRate():
    hourlyRate = float(input("Enter Houly Rate: "))
    return hourlyRate

        #Define tax rate
def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

        #Define hours, hourly rate, and tax rate to calculate net pay
def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

        #Define print info to include empName, hours, hourlyRate, gPay, taxRate, incomeTax, and netPay
def printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    
        #Define print totals to include totalEmployees, totalHours, totalGrossPay, totalTax, and totalNetPay
def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal Number Of Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours:,.2f}")
    print(f"Total Gross Pay: {totalGrossPay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total Net Pay: {totalNetPay:,.2f}")
    

        
        #Create if statement for totalEmployees, totalHours, totalGrossPay, totalTax, and totalNetPay
if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
        #Create while/if statement for getEmpName
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        
        #Print info to include empName, hours, hourlyRate, gPay, taxRate, incomeTax, and netPay
        printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)
        
        #Calculate totalEmployee, totalHours, totalGrossPay, totalTax, and totalNetPay
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay
        
        #Print results 
    PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)
    
        
