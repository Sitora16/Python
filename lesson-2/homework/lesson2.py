##1
name=input('enter your name: ')
Birthday=int(input('enter your birth year: '))
from datetime import datetime
year=datetime.now().year
age=year-Birthday
print(f"My name is {name} I am {age} years old")

#2
txt = 'LMaasleitbtui'
txt1=txt[::2]
txt2=txt[1::2]
print(txt1)
print(txt2)


#3
txt = 'MsaatmiazD'
txt1=txt[::2]
txt2=txt[-1::-2]
print(txt1)
print(txt2)

#4
txt = "I'am John. I am from London"
if "from" in txt:
    qism = txt.split("from")[1].strip()
    area= qism.split()[0]
    print("Live in:", area)
else:
    print("Yashash joyi topilmadi.")


#5
'Sitora'[::-1]

#6
name='Sitora'
vovels='aouie'
cnt =0
for i in name:
    if i.lower() in vovels:
        cnt+=1
print('vowels:',cnt)

#7
numbers=input('Enter the numbers:')
numbers_list = [int(number.strip()) for number in numbers.split(",")]
maxson=max(numbers_list)
print('katta son',maxson)

#8
if 'kiyik'=='kiyik'[::-1]:
     print(True)
else:
    print(False)


#9
email = input('Enter your email: ')
domain = email.split("@")[1]
print(domain)


#10
name1='Sitora1605'
name2='Sitora_1605'
name3='Sitora 1605'
name1.isalnum()
name2.isalnum()
name3.isalnum()
print(name1.isalnum())
print(name2.isalnum())
print(name3.isalnum())

