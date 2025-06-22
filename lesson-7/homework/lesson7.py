#Homework
#1
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return true
n = int(input())
print(is_prime(4))
print(is_prime(7))

#2
def digit_sum(k):
    cnt=0
    for i in str(k):
      cnt+=int(i)
    return cnt

k=int(input())
print(digit_sum(k))
#3
def daraja(n):
    k=2
    while k<=n:
        print(k,end=' ')
        k*=2

n=int(input())
print(daraja(n))
