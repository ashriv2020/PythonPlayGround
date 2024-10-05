from GenAIPreq.ClassDemo.employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employee(self):
        print('current employees:')
        for item in self.employees:
            print(f'Employee Name: {item.fname} {item.lname}')   
            print('--------------------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            
            print(f"Amount: ${i.calculate_paycheck():.2f }")
            print('--------------------------')

def main():
    my_company = Company()     

    employeee1 = Employee('Abhishek', 'Shrivastav', 50000)
    my_company.add_employee(employeee1)      
    employeee2 = Employee('Aayansh', 'Shrivastav', 100000)
    my_company.add_employee(employeee2) 
    
    #my_company.display_employee()
    my_company.pay_employees()

main()
