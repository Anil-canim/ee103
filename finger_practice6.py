# Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
# guess N. the code prints two lines: count: with how many guesses it took to find N, and answer: with the
# value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one
import random
N= random.randint(0,100)
print(N)
low=0
high=100
ans=(high+low)/2
guess=1
while ans<N or ans>N:
    if ans<N:
        low=ans
    elif ans>N:
        high=ans
    else:
        guess +=1
        print(ans)
        break
    guess += 1
    ans=(high+low)/2
    print(ans)
print("guess count is: ", guess)