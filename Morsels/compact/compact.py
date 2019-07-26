def compact(seq):
    
    itera = []
    y = None
    for x in seq:
        if x != y:
            itera.append(x)
        y = x
    
    return iter(itera)
    

