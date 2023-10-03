#create a function to sum two numbers
def sum(a, b):
    return a + b


#create a recursive fibonaci function
def fib(n):
    '''
    Input: n
    This function returns the nth number in the fibonacci sequence
    '''
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

# 
def fib2(n):
    #create a docstring for the fib2 function
    '''
    Input: n
    This function returns the nth number in the fibonacci sequence
    '''
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
    

#create a function that multiplies two numbers and add a docstring
def multiply(a, b):
    '''
    This function multiplies two numbers
    '''
    return a * b
    
#create a comment that has the top 10 web frameworks
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

#create a class to represent a programming language
# This class represents a programming language
class Language:
    # constructor for Language class
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # create a string representation of the Language class
    def __str__(self):
        return f'{self.name} was created in {self.year}'
    
#
def main():
    # print the result of sum(10, 20)
    print(sum(10, 20))

    # print the result of fib(10)
    print(fib(10))

    # print the result of fib2(10)
    print(fib2(10))

    # create a new instance of the Language class
    python = Language('Python', 1991)

    # print the result of calling the __str__ method
    print(python)


if __name__ == '__main__':
    main()