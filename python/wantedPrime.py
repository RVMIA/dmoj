import math
import sys
sys.set_int_max_str_digits(0)

def numForN(n):
    list = []
    for i in range(n):
        list.append(str(i+1))
    for i in range(n-1):
        list.append(str(n-(i+1)))
    o = list[0]
    for i in range(len(list)-1):
        o += list[i+1]
    output = int(o)
    return output

def prime(n):
    m = math.sqrt(n)
    count = 0
    if ((n == 2 or n == 3 or n == 5 or n == 7)):
        print("count: Prime Unconventional way", count)
        return True
    
    if (n == 1 or ((n > 7) and (n % 5 == 0 or n % 7 == 0 or n % 2 == 0 or n % 3 == 0))):
        print("count: Prime Unconventional way", count)
        return False
    
    if (((n - 1) / 6).is_integer()) or (((n + 1) / 6).is_integer()):
        for i in range(1, n):
            #if i % 10000000 == 0:
             #   print(i/10000000, i)
            # Counting Iterations
            count += 1
            five = 5 + (i * 6)
            seven = 7 + (i * 6)
            if ((((n / five) > 1) and (n / five).is_integer()) or (((n / seven) > 1) and ((n / seven).is_integer()))):
                print("count: Prime Unconventional way", count)
                return False;
            
            if ((i * 6) > n):
                # Max iterations 16666 for n == 100000 instead of 100000
                break;
            
        print("count: Prime Unconventional way", count)
        return True
    
    print("count: Prime Unconventional way", count)
    return False

n = int(input())

#o = numForN(n)
#print(o)
print(prime(n))
