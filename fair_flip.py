import random

def coin_flip():
    p = random.random()
    heads = .817
    tails = .183
    
    if p < heads:
        return 'H'
    else:
        return 'T'
        
def fair_flip():
 
        flip1 = coin_flip()
        flip2 = coin_flip()
       
	print(flip1, flip2) 
        
        if flip1 != flip2:
            return flip1 
        else:
            return None
        
sum = 0 

for i in range(0,1000):
    x = None 
	    
    while x == None:
	x = fair_flip()

    if x == 'H':
        sum += 1

print sum 
