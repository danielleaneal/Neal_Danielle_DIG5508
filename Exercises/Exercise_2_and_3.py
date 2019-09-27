
# Week 2 Exercise, performed along with Chapter 5
#%%
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
        return result




#%%
double ([1,10,5])

#%%
double([24])

#%%
double([])

#%%
double([2+2])

# My hypothesis about what double() does is that it doubles the value of whatever expression is inside the parentheses

#%%
x = [1,2,3]
double(x)


#Exercise 3, Performed along with Chapter 6

#%%
1500 * 0.08875


#%%
995.50 * 0.08875

#%%
def tax(subtotal):
        return subtotal * 0.08875


#%%
#making functions for order of operations testing
def add_numbers(x,y):
    return x+y

def subtract_numbers(x,y):
    return x-y

def multiply_numbers(x,y):
    return x*y

def divide_numbers(x,y):
    return x/y

def exponent_numbers(x,y):
    return x**y

