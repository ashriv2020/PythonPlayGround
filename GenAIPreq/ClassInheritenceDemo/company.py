from employee import Employee, SalaryEmployee, HourlyEmplyoee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employees(self, new_employee):
        self.employees.append(new_employee) 

    def display_employee(self):
        print('Current Employees:')
        for e in self.employees:
            print(e.fname, ' ', e.lname)  
        print('--------------------------')

    def pay_employee(self):
        print('Paying to employee:')
        for e in self.employees:  
            print('Paycheck for:', e.fname, e.lname)
            print(f'Amount: ₹{e.calculate_paycheck()}')
            print('--------------------------') 


def main():
    myCompany = Company()
    employee1 = SalaryEmployee('Abhishek', 'Shrivastav', 5000000)
    myCompany.add_employees(employee1)
    employee2 = HourlyEmplyoee('Amit', 'Sinha', 40, 1500)
    myCompany.add_employees(employee2)
    employee3 = CommissionEmployee('Sweta', 'Singh', 4800000, 2500, 10.5)
    myCompany.add_employees(employee3)


    myCompany.display_employee()
    myCompany.pay_employee()

main()    
