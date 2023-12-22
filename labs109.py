# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

import tester109

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False  
    return True  

def only_odd_digits(n):
    if n // 10 == 0 and (n % 10) % 2 == 1:
        return True 
    if n % 2 == 0:
        return False 
    elif n % 2 == 1:
        return only_odd_digits(n // 10)
    




