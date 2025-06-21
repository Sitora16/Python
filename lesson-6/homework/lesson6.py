#homework
#1
txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]
#2
n=5
for i in range(n): 
    print(i*i)
#2 davomi
n=int(input('Enter the numbers: '))
for i in range(n): 
    print(i*i)
#3.1
i = 1          
while i <= 10: 
    print(i)   
    i += 1     

#3.2
i = 1
while i <= 5:           
    j = 1
    while j <= i:      
        print(j, end=' ')
        j += 1
    print()            
    i += 1

#3.3
n=int(input('enter the number: '))
sum=0
for i in range(1, n + 1):
    sum += i
print("Sum is: ",sum)
#3.4
n=2

for i in range(1,11):
    print(n*i)
    
#3.5
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i>50 and i<=150:
        print(i)
#3.6
numbers=75869
count =0
for i in str(numbers):
    count+=1
print(count)
#3.7
i = 5
while i >= 1:           
    j = i
    while j >= 1:      
        print(j, end=' ')
        j -= 1 
    print()         
    i-= 1
#3.8
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1,-1,-1):
    print(list1[i])
#3.9
for i in range(-10,0):
    print(i)
#3.10
for i in range(5):
    print(i)
print("Done!")
#3.11
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#3.12
n_terms = 10
a, b = 0, 1
count = 0

print("Fibonacci sequence:")

while count < n_terms:
    print(a, end='  ')
    a, b = b, a + b
    count += 1

3.13
num = 5  
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"{num}! = {factorial}")

#3.14.1
list1 = [1, 1, 2]
list2 = [2, 3, 4]

list1_sorted = sorted(list1)
part1 = list1_sorted[:2]  

list2_sorted = sorted(list2, reverse=True)
part2 = list2_sorted[:2] 

part2.reverse()

result = part1 + part2
print(result)

#3.14.2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
lists=list1+list2
print(lists)
#3.14.3
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

result = []

for item in list1:
    if item not in list2:
        result.append(item)

for item in list2:
    if item not in list1:
        result.append(item)

print(result)
