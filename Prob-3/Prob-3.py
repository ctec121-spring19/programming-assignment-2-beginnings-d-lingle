# Module 2
#   Programming Assignment 2
#     Prob-3.py

# Daniel (Ash) Lingle
import math

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nAsh's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    myv1, myv2, myv3 = math.pi, 6485, "CTEC 121"
    # print the values of the 3 variables
    print("myv1:", myv1)
    print("myv2:", myv2)
    print("myv3:", myv3)
    print()
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method
    newv1, newv2, newv3 = eval(input("Enter 3 values seperated by commas:"))
    print("newv1:", newv1)
    print("newv2:", newv2)
    print("newv3:", newv3)
    print()

example()
studentCode()

