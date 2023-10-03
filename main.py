#import the random module
import random

#create a function to sum two numbers
def sum(a, b):
    return a + b

#create a recursive fibonaci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# create a comment that has the top 10 web frameworks
'''
Django
React
Vue
Angular
Spring
Express
Flask
Laravel
Ruby on Rails
ASP.NET
'''


# create a comment that has the top 10 programming languages
'''
JavaScript
Python
Java
C#
C++
PHP
Ruby
Swift
Kotlin
Go (Golang)
'''

#create a class to represent a programming language
class Language:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    #create a string representation of the object
    def __str__(self):
        return f"El programa {self.name} se creó en el año ({self.year})"
    
def print_languages():
    #create a list of languages
    languages = [
        Language("JavaScript", 1995),
        Language("Python", 1991),
        Language("Java", 1995),
        Language("C#", 2000),
        Language("C++", 1985),
        Language("PHP", 1995),
        Language("Ruby", 1995),
        Language("Swift", 2014),
        Language("Kotlin", 2011),
        Language("Go (Golang)", 2009)
    ]


    #print the list of languages
    for language in languages:
        print(language)

    #print the first 5 languages
    for language in languages[:5]:
        print(language)

    #print the last 5 languages
    for language in languages[-5:]:
        print(language)

    #print a random language
    print(random.choice(languages))


# create a main function that prints a hello world message, calls the sum function, calls the fib function, and calls the print_languages function
def main():
    print("Hello World!")
    print("The sum of 2 and 3 is: ", sum(2,3))
    print("The 10th fibonaci number is: ", fib(10))
    print_languages()


if __name__ == "__main__":
    main()
