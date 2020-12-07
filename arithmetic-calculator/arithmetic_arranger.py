from calculate_problem import calculate_problem

def arithmetic_arranger(list_of_problems, shouldInCludeAnswers=False):
    # Chars used in formatted strings
    whitespace = " "
    dash = "-"
    # Problems should not be more than five
    if len(list_of_problems) > 5:
        return "Error: Too many problems."

    # Variable for each row
    row1 = ""
    row2 = ""
    dashes_row = ""
    results_row = ""

    result_string = None

    for problem in list_of_problems:
        # Split problem into num1, operator and num2
        parts = problem.split()
        operator = parts[1]

        # Check if operator is different than + or -
        if not ((operator != "-") ^ (operator != "+")):
            return "Error: Operator must be '+' or '-'."

        num1 = None
        num2 = None
        # Operands should be numbers indeed
        try:
            num1 = int(parts[0])
            num2 = int(parts[2])
        except:
            return "Error: Numbers must only contain digits."

        # Operands should not have more than 4 digits
        if num1 > 9999 or num2 > 9999:
            return "Error: Numbers cannot be more than four digits."

        # Length of expression is equal to the length of the bigger number + 2(operator and whitespace)
        expression_length = len(str(max(num1, num2))) + 2 

        
        # Add number to each string by moving it to the right and include 4 whitespaces
        row1 += f"{str(num1).rjust(expression_length)}{whitespace * 4}"
        row2 += f"{operator} {str(num2).rjust(expression_length - 2)}{whitespace * 4}"
        dashes_row += f"{expression_length * dash}{whitespace * 4}"
        if shouldInCludeAnswers:
            results_row += f"{str(calculate_problem(num1, num2, operator)).rjust(expression_length)}{whitespace * 4}"


    # Return single string if everything is successful
    result_string = f"{row1.rstrip()}\n{row2.rstrip()}\n{dashes_row.rstrip()}"
    if shouldInCludeAnswers:
        result_string += f"\n{results_row.rstrip()}"

    return result_string
