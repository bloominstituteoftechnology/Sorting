

arrayofitems = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

def arr(elements ):
    if type(elements) == type([]):  
        for i in elements:
        
            print(f"\n{i}")
    
arr("string")