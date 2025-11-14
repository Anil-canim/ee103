

def speak(input_string):
    print(input_string)
    input_string=input_string*5
    return input_string*5 

def sum(num1, num2):
    result= num1 + num2
    return (result)

def sub(num1, num2):
    result= num1 - num2
    return (result)

def multiply(num1, num2):
    result= num1 * num2
    return (result)

def divide(num1, num2):
    result= num1 / num2
    return (result)


def calculation(num1, num2, operation):
    return operation(num1, num2)


def is_polindrome(input_string):
    if input_string == input_string[::-1]:
        return True
    else:
        return False
    