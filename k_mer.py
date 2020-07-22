
import sys

l1 = ['A', 'T', 'G', 'C']
l2 = ['A', 'T', 'G', 'C']

def mer(l1, l2, n) :
    l_tmp = []
    if n == 1 :
        return l2                    # l2 and l_tmp - jal ssu nun gae hak-sim.
    else :
        for b1 in l1 :
            for b2 in l2 :
                l_tmp.append(b1+b2)

    return mer(l1, l_tmp, n-1)

n = sys.argv[1]
n = int(n)
print(mer(l1,l2,n))
print(len(mer(l1, l2, n)))
