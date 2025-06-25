#homework
#1
try:
    1 / 0
except ZeroDivisionError:
    print("Xatolik: 0 ga bo‘lish mumkin emas.")

#2
try:
    int('Sitora')
except ValueError:
    print("Xatolik: Faqat butun son kiriting.")
#3
try:
    with open('file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

#4
try:
    result = 'Sitora' + 100
except TypeError:
    print("Xatolik: Matn bilan sonni qo‘shib bo‘lmaydi.")
#5
try:
    with open('/root/secret.txt', 'r') as f:
        print(f.read())
except PermissionError:
    print("Xatolik: Ruxsat yo‘q.")
#6
l = [1, 2, 3]
try:
    print(l[34])
except IndexError:
    print("Xatolik: Indeks ro'yxatdan tashqarida.")
#7
a = 3
while a > 0:
    print("Hello F25")
    a -= 1
#8
def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"Result: {result}")
    except ArithmeticError as e:
        print(f"An arithmetic error occurred: {e}")

# Run the function
divide_numbers()

#9
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except UnicodeDecodeError as e:
        print(f"Encoding issue: {e}")
    except FileNotFoundError:
        print("File not found. Please check the filename and path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = input("Enter the path to the file: ")
read_file(file_path)

#10
def list_operation():
    my_list = [1, 2, 3, 4, 5]

    try:
        # Attempting to call a non-existent attribute or method
        result = my_list.non_existent_method()
        print(result)
    except AttributeError as e:
        print(f"AttributeError caught: {e}")

# Run the function
list_operation()

#1
fayl = open("example.txt", "r")
matn = fayl.read()
print(matn)
fayl.close()

#2
n = 1 
fayl = open("example.txt", "r")

for i in range(n):
    satr = fayl.readline()
    if satr == '':
        break  
    print(satr, end='')

fayl.close()

#3
fayl = open("example.txt", "a")
text=fayl.write("Sitora")
fayl.close()
fayl = open("example.txt", "r")
matn = fayl.read()
print(matn)
fayl.close()
#4
n=1
fayl = open("example.txt", "r")
satrlar= fayl.readlines()
fayl.close()
for i in satrlar[-n:]:
    print(satr, end='')
#5
fayl = open("example.txt", "r")
satrlar=[]
for i in fayl:
    satrlar.append(i)
fayl.close() 
print(satrlar)   
#6
fayl = open("example.txt", "r")
matn=""
for i in fayl:
    matn+=satr
fayl.close() 
print(satrlar)   
#7
fayl = open("example.txt", "r")
satrlar = []
for satr in fayl:
    satrlar.append(satr.strip())  
fayl.close()
print(satrlar)
#8
fayl = open("example.txt", "r")
matn = fayl.read()
fayl.close()
soz=matn.split()
maks=max(len(soz)for i in soz)
eng_uzun=[i for i in soz if len(soz)==maks]
print("Eng uzun so'z uzunligi:", maks)
print("Eng uzun so'z(lar):", eng_uzun)
#9
fayl = open("example.txt", "r")
lines = fayl.readlines()
fayl.close()
print(len(lines))
#10
file_name = 'sample.txt'

word_count = {}

with open(file_name, 'r') as file:
    for line in file:
        words = line.strip().lower().split()
        for word in words:
            word = word.strip('.,!?":;()[]')
            if word:
                word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")

#11
import os

file_name = 'sample.txt'

if os.path.isfile(file_name):
    size = os.path.getsize(file_name)
    print("File size:", size, "bytes")
else:
    print("File not found.")
#12
list = ['apple', 'banana', 'cherry']
with open('example.txt', 'w') as file:
    for i in list:
        file.write(i+ '\n')

print("List has been written to example.txt")

#13
s_file='source.txt'
d_file='destination.txt'
with open(s_file,'r') as src:
    content=src.read()
with open(d_file,'w') as dest:
    dest.write(content)
print('File copied successfully')
#14
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
output = open('combined.txt', 'w')

lines1 = file1.readlines()
lines2 = file2.readlines()

for line1, line2 in zip(lines1, lines2):
    combined_line = line1.strip() + " " + line2.strip() + "\n"
    output.write(combined_line)

file1.close()
file2.close()
output.close()

print("Lines combined successfully into 'combined.txt'.")

#15
import random
with open('example.txt','r')as file:
    lines=file.readlines()
    random_lines=random.choice(lines)
    print(random_lines.strip())
#16
file=open('example','r')
print(file.closed)
file.close()
print(file.closed)
#17
with open('example.txt', 'r') as file:
    lines = file.readlines()

with open('example.txt', 'w') as file:
    for line in lines:
        file.write(line.strip())
#18
file_name = input("Fayl nomini kiriting (masalan, sample.txt): ")

try:
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        print("So‘zlar soni:", len(words))
except FileNotFoundError:
    print("Fayl topilmadi. Iltimos, to‘g‘ri fayl nomini kiriting.")
#19
import os
file_names = ['file1.txt', 'file2.txt', 'file3.txt']
characters = []
for file_name in file_names:
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            for char in content:
                characters.append(char)
    else:
        print(f"{file_name} topilmadi.")

print("Belgilar ro'yxati:")
print(characters)
#20
import string
for letter in string.ascii_uppercase:  # A dan Z gacha harflar
    file_name = f"{letter}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is file {file_name}\n")

print("26 ta fayl yaratildi: A.txt dan Z.txt gacha.")
#21
import string
n = int(input("Har bir qatorda nechta harf bo‘lsin? "))
with open('alphabet.txt', 'w') as file:
    letters = string.ascii_lowercase  # kichik harflar: a,b,c,...z
    for i in range(0, len(letters), n):
        line = letters[i:i+n]
        file.write(line + '\n')
print("alphabet.txt fayliga alifbo yozildi.")
