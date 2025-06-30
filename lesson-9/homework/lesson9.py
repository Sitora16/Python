#Homework
#1
import math  
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def yuzasi(self):
        return math.pi * (self.radius ** 2)
    def perimetri(self):
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    r = float(input("Doira radiusini kiriting: "))
    doira = Circle(r)
    print(f"Doiraning yuzasi: {doira.yuzasi():.2f}")
    print(f"Doiraning perimetri: {doira.perimetri():.2f}")

#2
from datetime import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=datetime.strptime(date_of_birth, "%Y-%m-%d")
    def age(self):
        today=datetime.today()
        age=today.year-self.date_of_birth.year
        if(today.month,today.day)<(self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
if __name__=='__main__':
        name=input("Name: ")
        country=input("country: ")
        dob=input("dob: ")
        person=Person(name,country, dob)
        print(person.name, person.country, person.age())
#3
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b
if __name__ == "__main__":
    calc = Calculator()

    x = 10
    y = 5

    print("Addition:", calc.add(x, y))
    print("Subtraction:", calc.subtract(x, y))
    print("Multiplication:", calc.multiply(x, y))
    print("Division:", calc.divide(x, y))

#4
import math
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented.")

    def perimeter(self):
        raise NotImplementedError("Perimeter method not implemented.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

if __name__ == "__main__":
    shapes = [
        Circle(5),
        Square(4),
        Triangle(3, 4, 5)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
        print(f"{shape.__class__.__name__} Perimeter: {shape.perimeter():.2f}")
        print()

#5
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            print(f"Value {value} already exists in the tree.")

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    for val in values:
        bst.insert(val)

    print("Inorder Traversal:", bst.inorder())

    print("Search 60:", bst.search(60))  
    print("Search 25:", bst.search(25))  

#6
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo‘sh!"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack holati:", stack.display())

    print("Pop qilingan element:", stack.pop())
    print("Yangi stack holati:", stack.display())

#7
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head
        previous = None

        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            print(f"{data} ro‘yxatda topilmadi.")
            return

        if previous is None:
            self.head = current.next  
        else:
            previous.next = current.next 

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print("Linked List:", ll.display())

    ll.delete(20)
    print("20 o‘chirilgandan keyin:", ll.display())

    ll.delete(50)  

#8
class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            current_price, current_qty = self.items[name]
            self.items[name] = (price, current_qty + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatchada topilmadi.")

    def calculate_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def display_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
            return
        print("Savatchadagi mahsulotlar:")
        for name, (price, quantity) in self.items.items():
            print(f"- {name}: {quantity} dona x {price} so‘m = {price * quantity} so‘m")
        print(f"Umumiy narx: {self.calculate_total()} so‘m")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Olma", 5000, 3)
    cart.add_item("Banan", 7000, 2)
    cart.add_item("Olma", 5000, 1)  

    cart.display_cart()

    cart.remove_item("Banan")
    print("\nBanan olib tashlangandan so‘ng:")
    cart.display_cart()

#9
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} stack'ga qo‘shildi.")

    def pop(self):
        if self.is_empty():
            print("Stack bo‘sh! Element olib tashlab bo‘lmaydi.")
            return None
        removed_item = self.items.pop()
        print(f"{removed_item} stack'dan olib tashlandi.")
        return removed_item

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack bo‘sh.")
        else:
            print("Stack elementlari (yuqoridan pastga):")
            for item in reversed(self.items):
                print(item)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.display()
    
    stack.pop()
    stack.display()

#10
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} navbatga qo‘shildi.")

    def dequeue(self):
        if self.is_empty():
            print("Navbat bo‘sh! Element olib tashlab bo‘lmaydi.")
            return None
        removed_item = self.items.pop(0)
        print(f"{removed_item} navbatdan olib tashlandi.")
        return removed_item

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Navbatdagi elementlar:")
            for item in self.items:
                print(item)

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.display()

    queue.dequeue()
    queue.display()

#11
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so‘m muvaffaqiyatli qo‘shildi. Yangi balans: {self.balance} so‘m.")
        else:
            print("Iltimos, musbat summa kiriting.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Iltimos, musbat summa kiriting.")
        elif amount > self.balance:
            print("Hisobda yetarli mablag‘ yo‘q.")
        else:
            self.balance -= amount
            print(f"{amount} so‘m muvaffaqiyatli yechildi. Qolgan balans: {self.balance} so‘m.")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, initial_deposit=0):
        if owner in self.accounts:
            print(f"{owner} nomidagi hisob allaqachon mavjud.")
        else:
            self.accounts[owner] = Account(owner, initial_deposit)
            print(f"{owner} uchun yangi hisob yaratildi. Dastlabki balans: {initial_deposit} so‘m.")

    def deposit(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].deposit(amount)
        else:
            print(f"{owner} nomidagi hisob topilmadi.")

    def withdraw(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].withdraw(amount)
        else:
            print(f"{owner} nomidagi hisob topilmadi.")

    def check_balance(self, owner):
        if owner in self.accounts:
            balance = self.accounts[owner].get_balance()
            print(f"{owner} hisobidagi balans: {balance} so‘m.")
        else:
            print(f"{owner} nomidagi hisob topilmadi.")

    def list_accounts(self):
        if not self.accounts:
            print("Bankda hech qanday hisob mavjud emas.")
        else:
            print("Bankdagi hisoblar:")
            for owner, account in self.accounts.items():
                print(f"- {owner}: {account.get_balance()} so‘m")

if __name__ == "__main__":
    bank = Bank()
    bank.create_account("Ali", 10000)
    bank.create_account("Vali")
    bank.list_accounts()

    bank.deposit("Ali", 5000)
    bank.withdraw("Ali", 3000)
    bank.check_balance("Ali")

    bank.withdraw("Vali", 1000) 
    bank.check_balance("Vali")
