
def factorial(n):
    p=1
    for i in range(1,n+1):
        p=p*i
        return p
def combination(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def probability(n,k):
    c=2**k
    prob=0
    for i in range(n,c+1):
        prob+= combination(c,i) *  ((1/4)**(i)) * ((3/4)**(c - i))
        return prob

print(probability(1,2))

