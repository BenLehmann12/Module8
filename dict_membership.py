'''
Author: Ben Lehmann
Function: in_dict(a_dict, a_value), this returns a boolean value if value in dictionary
Date Modified: 10/18/2020
'''

def in_dict(a_dict, a_value):
    if a_value in a_dict:
        return True
    else:
        return False

if __name__ == "__main__":
    print(in_dict({3,6,9,12},3))

