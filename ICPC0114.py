import math

def isPrime(n):     
    if n < 2:          
        return False     
    for i in range(2,int(math.sqrt(n)+1)):         
        if n % i == 0:              
            return False     
    return True  

def pefectPrime(str):     
    for i in str:         
        if not isPrime(int(i)):             
            return 'No'     
    num1, num2 = str, str[::-1]     
    if not isPrime(int(num1)) or not isPrime(int(num2)):         
        return 'No'     
    return 'Yes'  
    
for case in range(int(input())):
    print(pefectPrime(input()))