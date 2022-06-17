class McDonalds:
    boss = "The Boss"

    def __init__(self, employee_salary, employee_name, work_type):
        self.employee_salary = employee_salary
        self.employee_name = employee_name
        self.work_type = work_type

    def print_employee(self):
        print(f"Director is: {McDonalds.boss}. "
              f"\nEmployee name is: {self.employee_name}"
              f"\nEmployee salary is: {self.employee_salary}."
              f"\nWork type is: {self.work_type}.\n")


class PA(McDonalds):
    def __init__(self, employee_salary, employee_name, work_type):
        super().__init__(employee_salary, employee_name, work_type)


class CA(McDonalds):
    def __init__(self, employee_salary, employee_name, work_type):
        super().__init__(employee_salary * 1.2, employee_name, work_type)


employeePA = PA(1000, "Peter", "full-time")
employeeCA = CA(1000, "Mary", "full-time")

employeeCA.print_employee()

employeePA.print_employee()
