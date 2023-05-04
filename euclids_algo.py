'''
Algorithm E (Euclids algorithm). Given two positive integers m and n, find
their greatest common divisor, that is, the largest positive integer that evenly
divides both m and n.

'''
m = 12345678901234567890
n = 98765432109876543210


import time
# Euclids algorithm using recursion
def euclid_algo(m,n):
    #E1. [Find remainder.] Divide m by n and let r be the remainder. (We will have 0 ≤ r < n.)
    remainder = m%n
    #[Is it zero?] If r = 0, the algorithm terminates; n is the answer.
    if (remainder == 0):
        return n
    #. [Reduce.] Set m ← n, n ← r, and go back to step E1
    else:
        m = n
        n = remainder
        return euclid_algo(m,n)
    
start_time = time.time()
recur = euclid_algo(m,n)
end_time = time.time()
algo_time = end_time - start_time
print("GCD:", recur, "Recursive Time:", algo_time )


#print(euclid_algo(1024,645))
def euclid_algo_iter(m,n):
    
    while(n > 1):
        remainder = m % n
        if remainder == 0:
            break
        m = n
        n = remainder
    return n
start_time = time.time()
iter = euclid_algo_iter(m,n)
stop_time = time.time()
algo_time = stop_time - start_time
print("GCD:", iter,"Iterative Time:", algo_time)

