####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below

my_name=input("what is your name: ")
print("your name length multiplied by 5, the result is: ",len(my_name)*5)

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"


# Insert code below
n = 8
x=test_string[:8:1]
y=test_string[9::1]

print(x+y)



####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

# Insert code below

my_string = "This is my string"  # example string - modify to test

x=len(my_string)>10 or len(my_string)<5
print(x)    


####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string



    
# Insert code below

my_string = "How many times is the letter e in this string?"
x="e"
yeni=""

for i in my_string:
    if i in x:
        continue
    yeni=(yeni+i)

print(abs(len(yeni)-len(my_string)))

yeni=yeni.split()
k=" "
yeni= k.join(yeni)

print(yeni)