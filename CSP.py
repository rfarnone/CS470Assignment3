import csv

# Read the CSV file
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

# Create variables and domain values from CSV data
def create_variables(csv_data):
    variables = {}
    for i, row in enumerate(csv_data[1:]):  # skip the first row as it contains headers
        variable_name = f'X{i+1}'
        domain_values = [j for j, value in enumerate(row) if value == '1']
        variables[variable_name] = domain_values
    return variables

# Main function
def main():
    filename = 'CSPData.csv'
    csv_data = read_csv(filename)
    variables = create_variables(csv_data)
    print(variables)

    # Create CSP problem
    #problem = Problem()

    # Add variables to the problem with their domain values
    #for var, domain in variables.items():
        #problem.addVariable(var, domain)

    # Solve the problem
    #solutions = problem.getSolutions()
    #for solution in solutions:
        #print(solution)

if __name__ == "__main__":
    main()
