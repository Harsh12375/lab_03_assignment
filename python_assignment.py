class EmployeeTable:
    def __init__(self):
        self.data = [
            {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary": 56000},
            {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary": 67500},
            {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary": 82100},
            {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary": 55000},
            {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary": 44000},
        ]

    def search_by_age(self, age):
        result = [employee for employee in self.data if employee["Age"] == age]
        return result

    def search_by_name(self, name):
        result = [employee for employee in self.data if employee["Name"].lower() == name.lower()]
        return result

    def search_by_salary(self, operator, salary):
        if operator == ">":
            result = [employee for employee in self.data if employee["Salary"] > salary]
        elif operator == "<":
            result = [employee for employee in self.data if employee["Salary"] < salary]
        elif operator == ">=":
            result = [employee for employee in self.data if employee["Salary"] >= salary]
        elif operator == "<=":
            result = [employee for employee in self.data if employee["Salary"] <= salary]
        else:
            result = []
        return result

    def display_result(self, result):
        if not result:
            print("No matching records found.")
        else:
            for employee in result:
                print(f"Employee ID: {employee['Employee ID']}")
                print(f"Name: {employee['Name']}")
                print(f"Age: {employee['Age']}")
                print(f"Salary: {employee['Salary']}")
                print("-" * 30)

def main():
    employee_table = EmployeeTable()

    while True:
        print("Search Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            age = int(input("Enter Age: "))
            result = employee_table.search_by_age(age)
            employee_table.display_result(result)
        elif choice == "2":
            name = input("Enter Name: ")
            result = employee_table.search_by_name(name)
            employee_table.display_result(result)
        elif choice == "3":
            operator = input("Enter operator (>, <, >=, <=): ")
            salary = int(input("Enter Salary: "))
            result = employee_table.search_by_salary(operator, salary)
            employee_table.display_result(result)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
