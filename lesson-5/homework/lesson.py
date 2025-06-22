#Homework
#1
def is_leap_year(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2020))  
print(is_leap_year(1900))  
print(is_leap_year(2000))  
print(is_leap_year(2023))  

#2
n=int(input("Enter the number: "))
if n%2!=0:
    print ('Weird')
elif 2<=n<=5:
    print ('Not weird')
elif 6<=n<=20:
    print ('Weird')
elif n>20:
    print ('Not weird')
else:
    print('20 dan katta emas')
#3
a=16
b=24
if a>b:
    print(b-a)
else:
    print('Topilmadi')
a = 16
b = 24

if a > b:
    a, b = b, a  

if a % 2 != 0:
    a += 1 

evens = list(range(a, b + 1, 2)) 
print(evens)
