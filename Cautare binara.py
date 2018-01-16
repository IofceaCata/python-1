import random
 


anum = 9          

size = 6          

array = random.sample(list(range(1, 20)), size)

array = sorted(array)  

#array.sort()           

print(anum, array)      



def binary_search(num, array, lo, hi):
 
    
	if hi < lo: return -1 
    
	mid = (lo + hi) // 2  
    
	if num == array[mid]:
        
		return mid          
    
	elif num < array[mid]:
        
		return binary_search(num, array, lo, mid - 1)
    
	else:
        
		return binary_search(num, array, mid + 1, hi)    
 



def my_search(anum, array): 
    
	return binary_search(anum, array, 0, len(array) - 1)
 
 


pos = my_search(anum, array)

if pos < 0:
    
	print("not found")

else:
    
	print("found at position", pos)