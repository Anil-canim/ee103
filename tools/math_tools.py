def check_even_odd(input_number):
    if input_number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def calc_sum(input_number1, input_number2):
    return input_number1 + input_number2

def analyze_sum(input_number1, input_number2):
    total = calc_sum(input_number1, input_number2)
    check= check_even_odd(total)
    print("Sum of", input_number1, "and", input_number2, "is:", total, "which is", check)
    return total, check