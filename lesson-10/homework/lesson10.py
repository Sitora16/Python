#1
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")  # e.g., "2025-07-01"
        self.status = False  # False = Incomplete, True = Complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Complete" if self.status else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue: {self.due_date.date()}\nStatus: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Invalid task index.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks):
            print(f"\nTask {i + 1}:\n{task}")

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.status]
        if not incomplete_tasks:
            print("All tasks are complete!")
        for i, task in enumerate(incomplete_tasks):
            print(f"\nIncomplete Task {i + 1}:\n{task}")

def main():
    todo = ToDoList()
    
    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            todo.list_all_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo.mark_task_complete(index)

        elif choice == '3':
            todo.list_all_tasks()

        elif choice == '4':
            todo.list_incomplete_tasks()

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
todo.py
#2
from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content: {self.content}")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No blog posts yet.")
            return
        for i, post in enumerate(self.posts):
            print(f"\nPost {i + 1}:\n{post}\n{'-'*40}")

    def posts_by_author(self, author_name):
        filtered = [post for post in self.posts if post.author.lower() == author_name.lower()]
        if not filtered:
            print(f"No posts found by author: {author_name}")
        for post in filtered:
            print(f"\n{post}\n{'-'*40}")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            print("Post deleted successfully.")
        else:
            print("Invalid post index.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit(new_title, new_content)
            print("Post updated successfully.")
        else:
            print("Invalid post index.")

    def latest_posts(self, count=3):
        sorted_posts = sorted(self.posts, key=lambda p: p.timestamp, reverse=True)
        latest = sorted_posts[:count]
        for post in latest:
            print(f"\n{post}\n{'-'*40}")

def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author's name: ")
            blog.add_post(Post(title, content, author))
            print("Post added successfully.")

        elif choice == '2':
            blog.list_all_posts()

        elif choice == '3':
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == '4':
            blog.list_all_posts()
            index = int(input("Enter post number to delete: ")) - 1
            blog.delete_post(index)

        elif choice == '5':
            blog.list_all_posts()
            index = int(input("Enter post number to edit: ")) - 1
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == '6':
            count = int(input("How many latest posts to show? "))
            blog.latest_posts(count)

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1–7.")
python blog.py

#3
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds. Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.account_number}")

    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Transfer failed: insufficient funds.")
        else:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount:.2f} to {target_account.account_number}")

    def display_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: ${self.balance:.2f}")
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.holder_name} added successfully.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balance for {account.account_number}: ${account.balance:.2f}")
        else:
            print("Account not found.")
def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.add_account(Account(acc_num, name, initial_balance))

        elif choice == '2':
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == '3':
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            from_acc = input("Enter your account number: ")
            to_acc = input("Enter recipient's account number: ")
            amount = float(input("Enter transfer amount: "))

            sender = bank.find_account(from_acc)
            receiver = bank.find_account(to_acc)

            if sender and receiver:
                sender.transfer(receiver, amount)
            else:
                print("One or both accounts not found.")

        elif choice == '6':
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                account.display_details()
            else:
                print("Account not found.")

        elif choice == '7':
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Enter a number between 1 and 7.")
python banking.py
