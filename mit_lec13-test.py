# def sum_digits_except(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             print("couldn't convert character", char)
#     return print(total)


# sum_digits_except("asdfasf8")


# def sum_digits_assert(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     assert len(s) != 0, "s is empty"
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError("string contained a character") 
#     return total

# # print(sum_digits_assert(""))
# # print(sum_digits_assert("123"))
# print(sum_digits_assert("123abc"))


def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of 
        equal lengths containing numbers

    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 

    Raise a ValueError if Ldenom contains 0. """
    assert len(Lnum)==len(Ldenom), ("both list length has to be equal")
    assert len(Ldenom) and len(Lnum)!=0, ("list's length has to bigger than 0")

    try:
        return [Lnum[i]/Ldenom[i] for i in range(len(Lnum))] 
    except ZeroDivisionError:
        raise ValueError(Ldenom,"contains 0 in it's list")
    except TypeError:
        raise TypeError("lists only contains integers")      
   
    
    # challenge: write this with list comprehension!

    
# For example:
L1 = [4,5,6]
L2 = [1,2,3]
print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError


# to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3,1,"a"]    
print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
print(pairwise_div(L1, L2))  # raises an AssertionError



def pairwise_div(Lnum, Ldenom):
    """ Lnum and Ldenom are non-empty lists of equal lengths
        containing numbers
    Returns a new list whose elements are the pairwise 
    division of an element in Lnum by an element in Ldenom. 
    Raise a ValueError if L2 contains 0 or if the code can't 
    perform the division for some reason. """
    assert (len(Lnum) == len(Ldenom)) and (len(Ldenom) != 0)
    L = []
    for i in range(len(Lnum)):
        try:
            L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError
    return L



def get_stats(class_list, avg_func):
    """ class_list is a list of student info: 
            * name as a list
            * grades as a list
        avg_func is a function that takes in a list and returns a float
    """
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg_func(person[1])])
    return new_stats 

test_grades = [[['peter', 'parker'], [10.0, 55.0, 85.0]], 
               [['bruce', 'wayne'], [10.0, 80.0, 75.0]],
               [['captain', 'america'], [80.0,10.0,96.0]],
               [['thor'], []]]

## Note in the get_stats function calls below, 
## we are passing the various avg1/2/3 function names as params
## to test different avg function behaviours with the same data

# avg function: version without an exception
def avg1(grades):
    return (sum(grades))/len(grades)
# print(get_stats(test_grades, avg1))
    

# avg function: version with an exception
def avg2(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
# print(get_stats(test_grades, avg2))


# avg function: version with an exception
def avg3(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0
# print(get_stats(test_grades, avg3))


# avg function: version with assert
def avg4(grades):
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades)/len(grades)
# print(get_stats(test_grades, avg4))
