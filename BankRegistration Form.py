#Bank employee registration form
class BankEmployee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position
    
    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print("")

def register_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    
    employee = BankEmployee(emp_id, name, position)
    print("\nEmployee Registered Successfully!\n")
    return employee

def main():
    print("Welcome to the Bank Employee Registration System\n")
    
    employees = []
    while True:
        print("1. Register a New Employee")
        print("2. View All Employees")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            employee = register_employee()
            employees.append(employee)
        elif choice == '2':
            if not employees:
                print("No employees registered yet.\n")
            else:
                print("List of Employees:")
                for emp in employees:
                    emp.display_info()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
