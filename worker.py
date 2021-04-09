# Just checking this thing out.

class Employee:
    def __init__(self, emp_name, emp_number):
        self.__emp_name = emp_name
        self.__emp_number = emp_number
        
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
    
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def get_emp_name(self):
        return self.__emp_name
    
    def get_emp_number(self):
        return self.__emp_number
    

class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_number,
                 shift_number, hrly_pay_rate):
        Employee.__init__(self, emp_name, emp_number)
        self.__shift_number = shift_number
        self.__hrly_pay_rate = hrly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hrly_pay_rate(self, hrly_pay_rate):
        self.__hrly_pay_rate = hrly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hrly_pay_rate(self):
        return self.__hrly_pay_rate