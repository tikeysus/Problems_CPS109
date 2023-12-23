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
    
def domino_cycle(tiles):
    if not tiles:
        return True 
    for i in range(len(tiles) - 1):
        if tiles[i][1] != tiles[i + 1][0]:
            return False  
    return tiles[0][0] == tiles[-1][1] 

def is_cyclops(n):
    n = str(n)
    if len(n) % 2 == 0: 
        return False 
    for i in range(len(n) // 2):
        if n[i] == '0':
            return False
        continue 
    for j in range(len(n) // 2 + 1, len(n)):
        if n[j] == '0':
            return False 
    return n[len(n) // 2] == '0' 

def riffle(items, out = True):
    if not items:
        return []
    empty = [] 
    if out:
        for i in range(len(items) // 2):
            empty.append(items[:len(items) // 2][i])
            empty.append(items[len(items) // 2:][i])
    elif not out:
        for i in range(len(items) // 2):    
            empty.append(items[len(items) // 2:][i])
            empty.append(items[:len(items) // 2][i])
    return empty 