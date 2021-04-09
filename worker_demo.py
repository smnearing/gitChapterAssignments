# This program uses classes from worker.py to store production workers
# information and display them as needed. 

import worker

def main():
    print("-----------------------------")
    emp_name = input("Name: ")
    emp_number = input("Employee Number: ")
    shift_number = input("Shift number (1 or 2): ")
    hrly_pay_rate = input("Hourly Pay Rate: ")
    print("-----------------------------")
    print("-----------------------------")

    if shift_number == 1:
        shift_number = 'Day'
    else:
        shift_number = 'Night'

    my_production_worker = worker.ProductionWorker(emp_name, emp_number,
                                            shift_number, hrly_pay_rate)

    print("Production Worker Information")
    print("-----------------------------")
    print("Employee Name: ", my_production_worker.get_emp_name())
    print("Employee number: ", my_production_worker.get_emp_number())
    print("Shift number: ", my_production_worker.get_shift_number())
    print("Hourly Pay Rate: $", my_production_worker.get_hrly_pay_rate())
    print("-----------------------------")

if __name__ == '__main__':
    main()