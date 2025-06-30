#1
#!/bin/bash

python3 -m venv myenv

source myenv/bin/activate

pip install --upgrade pip
pip install requests numpy

pip list

echo "Virtual muhit yaratildi va paketlar o'rnatildi."

#2.1
# math_operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0 ga bo'lish mumkin emas")
    return a / b

#2.2
# string_utils

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
#3

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))

write_file("test.txt", "Salom, dunyo!")
content = read_file("test.txt")
print(content)
