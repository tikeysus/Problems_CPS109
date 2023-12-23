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
        
    
    
    
print(riffle([0,1], out = False))