import csv
import time

COLOR_NUM = 3
ASSIGNMENT_NUM = 0
BACKTRACKING_NUM = 0

class CSP:
    def __init__(self, variables, Domains, constraints):
        self.variables = variables
        self.domains = Domains
        self.constraints = constraints
        self.solution = None
        self.assignment_num = 0
        self.backtrack_num = 0

    def solve(self):
        assignment = {}
        #print("Starting backtracking...")
        self.solution = self.backtrack(assignment)
        #print("Finished backtracking.")
        return self.solution

    def backtrack(self, assignment):

        #print("Current assignment:", assignment)
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        #print("Selected variable:", var)
        for value in self.order_domain_values(var, assignment):
            #print("Considering value:", value)
            self.assignment_num += 1
            if self.is_consistent(var, value, assignment):
                #print("Value is consistent.")
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                #print("No solution found with this value. Backtracking...")
                self.backtrack_num += 1
                del assignment[var]
            else:
                print("Value is not consistent. Trying next value...")
        return None

    def select_unassigned_variable(self, assignment):
        unassigned_vars = [var for var in self.variables if var not in assignment]
        return min(unassigned_vars, key=lambda var: len(self.domains[var]))

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_consistent(self, var, value, assignment):
        for constraint_var in self.constraints.get(var, []):
            if constraint_var in assignment and assignment[constraint_var] == value:
                return False
        for constraint_var, constraint_values in self.constraints.items():
            if var in constraint_values and constraint_var in assignment and assignment[constraint_var] == value:
                return False
        return True
    
    def assignments(self):
        assignmnets = self.assignment_num
        return assignmnets
    
    def backtracks(self):
        backtracks = self.backtrack_num
        return backtracks

# Read the CSV file
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

# Create variables values from CSV data
def create_variables(csv_data):
    variables = {}
    for i, row in enumerate(csv_data[1:], start=1):  # start from 1 to skip header row
        variable_name = f'X{i}'
        variables[variable_name] = 1
    return variables

# Create domain values for variables
def create_domain(variables):
    domain = {var: set(range(1, COLOR_NUM+1)) for var in variables}
    return domain

# Create constraint values from CSV data
def create_constraint(csv_data):
    constraint = {}
    for i, row in enumerate(csv_data[1:], start=1):  # start from 1 to skip header row
        variable_name = f'X{i}'
        constraint_values = [f'X{j+1}' for j, value in enumerate(row[1:], start=0) if value == '1']  # start from 1 to skip header column
        if constraint_values:  # Check if domain is not empty
            for value in constraint_values:
                if value not in constraint:
                    constraint[value] = []
                constraint[value].append(variable_name)
    return constraint

# Main function
def main():
    start = time.time()
    filename = 'CSPData.csv'
    csv_data = read_csv(filename)
    variables = create_variables(csv_data)
    domains = create_domain(variables)
    constraints = create_constraint(csv_data)
    print("Variables:", variables)
    print("Domains:", domains)
    print("Constraints:", constraints)

    csp = CSP(variables, domains, constraints)
    sol = csp.solve()
    end = time.time()
    ASSIGNMENT_NUM = csp.assignments()
    BACKTRACKING_NUM = csp.backtracks()

    print("Solution:", sol)
    print("Assignments:", ASSIGNMENT_NUM)
    print("Backtracks:", BACKTRACKING_NUM)
    print(end-start)

if __name__ == "__main__":
    main()

