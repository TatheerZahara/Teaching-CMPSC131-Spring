# -*- coding: utf-8 -*-
"""R.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m0XOsSHgkB6pe1LQ1EjLxjP5_k4sssCm

# Write a function that takes a number as a parameter and prints it multiplicative table. For example, if you give 2 as a parameter, the output will look like: 

> 2*1=2

> 2*2=4

> 2*3=6

.

.

.



> 2*10=20

# Use the program that you had written in the previous question, and do the following: 
* Remove the parameters: Your name, number of courses, names of courses 
* Add the parameters: marks in courses (if you have three courses, you’d have three parameters)
* Find the average marks and return the average to the main body. 
* Print the average outside the function
"""

def information(mark1, mark2, mark3, mark4): 
  avg=(mark1+mark2+mark3+mark4)/4
  return avg 

a=information(40,50,90,100)
print("Average:", a)

"""# Write a program that takes nothing as parameters, but still prints a table of female students in a class along with the color of their eyes. """

def table_of_female():
  print("Names       |        Color of eyes")
  print(" Tatheer    |        Brown")

table_of_female()

"""# Suppose you work at a school, and several people ask you about your email address. Instead of typing your entire email, you just want to use a function to handle everything for you. You can do this by defining a function named sendEmail. This function takes no parameters, but returns your email address. """

def sendEmail():
  email="tzz5184@psu.edu"
  return email


hey=sendEmail()
print("Your email is", hey)

"""# Write a program that takes numbers of days as parameters and prints out the years, weeks, days separately within the body of the function. 


"""

# Function to find

DAYS_IN_WEEK = 7
# year, week, days
def find( number_of_days ):
 
    # Assume that years is
    # of 365 days
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
                DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK
     
    print("years = ",year,
          "\nweeks = ",week,
          "\ndays = ",days)
     
# Driver Code
number_of_days = 46000
find(number_of_days)