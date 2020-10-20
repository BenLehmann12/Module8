'''
Author: Ben Lehmann
Function: The first function returns the value if user puts in A or "a", the second function goes from A-D but does not accept
not numeric values, the third function accpets non-numeric values
'''

def a_function(key):
    a_key = {"A":90, "a":95}.get(key)
    return a_key

def average(key):
    user_average =  {"A": 100, "B":80, "C": 70, "D":60}.get(key)
    return user_average

def switch_average(key):
    user_value = {"A": 100, "B":80, "C": 70, "D":60}.get(key, KeyError)
    return user_value

if __name__ == "__main__":
    print(average(key="C"))