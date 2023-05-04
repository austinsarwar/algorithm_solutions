'''
Algorithm E (Euclids algorithm). Given two positive integers m and n, find
their greatest common divisor, that is, the largest positive integer that evenly
divides both m and n.

'''
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
        euclid_algo(m,n)
print(euclid_algo(4,2))
