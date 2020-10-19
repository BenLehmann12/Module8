from datetime import datetime,timedelta
'''
Author: Ben Lehmann
Date: 10/18/20 but modified 10/19/20
Function: Return the Half Birthday of user
'''
def half_birthday(birthday_time):
    half = birthday_time + timedelta(days=182.5)   #Half: 365/2 = 182.5
    return half

