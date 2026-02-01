"""
📘 Day 3 – Object-Oriented Programming (OOP) Basics

What I learned today:
1️⃣ Classes & Objects
   - Created custom classes using the `class` keyword
   - Instantiated objects from classes
   - Used `__init__` constructor to initialize object data

2️⃣ Object Behavior (Methods)
   - Defined instance methods to represent real-world behavior
   - Used `self` to access and modify object state
   - Implemented logic inside methods (pass/fail check, deposit/withdraw)

3️⃣ Stateful Objects & Encapsulation Thinking
   - Maintained internal state using instance variables
   - Updated state across method calls (BankAccount balance, Counter value)

OOP Programs Built Today:
✔ Student Information System
✔ Bank Account System
✔ Counter Object

Focus:
→ Learning OOP deeply for long-term mastery and AI/ML foundations
"""


# --------------------------------------------------
# 1. Student Information System (OOP)
# --------------------------------------------------

class Student:
    def __init__(self, name, age, marks, student_id, gender):
        self.name = name
        self.age = age
        self.marks = marks
        self.student_id = student_id
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Student ID: {self.student_id}")
        print(f"Gender: {self.gender}")

    def is_passed(self, passing_marks=40):
        return self.marks >= passing_marks


print("\n---------------------- Student Information System -----------------------------\n")

student1 = Student("Alice", 20, 85, "S123", "Female")
student1.display_info()
print(f"Is passed: {student1.is_passed()}")

print("\n---------------------------------------------------\n")

student2 = Student("Bob", 22, 35, "S124", "Male")
student2.display_info()
print(f"Is passed: {student2.is_passed()}")

print("\n---------------------------------------------------\n")

student3 = Student("Charlie", 19, 50, "S125", "Non-binary")
student3.display_info()
print(f"Is passed: {student3.is_passed()}")

print("\n---------------------- Thank You -----------------------------\n")


# --------------------------------------------------
# 2. Bank Account System (OOP)
# --------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Balance: ₹{self.balance}")


print("\n---------------------- Bank Account System -----------------------------\n")

account1 = BankAccount("John Doe", 1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)
account1.display_balance()

print("\n---------------------------------------------------\n")

account2 = BankAccount("Jane Smith")
account2.display_balance()
account2.deposit(300)
account2.withdraw(100)
account2.display_balance()

print("\n---------------------------------------------------\n")

account3 = BankAccount("Alice Johnson", 1500)
account3.display_balance()
account3.deposit(700)
account3.withdraw(400)
account3.display_balance()

print("\n---------------------------------------------------\n")

account4 = BankAccount("Bob Brown", 200)
account4.display_balance()
account4.deposit(800)
account4.withdraw(500)
account4.display_balance()

print("\n---------------------- Thank You -----------------------------\n")


# --------------------------------------------------
# 3. Counter Object (Stateful Thinking)
# --------------------------------------------------

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
print("\n---------------------- Counter Object -----------------------------\n")

counter = Counter()
print("Initial Count:", counter.get_count())
counter.increment()
counter.increment()
print("Count after 2 increments:", counter.get_count())
counter.decrement()
print("Count after 1 decrement:", counter.get_count())
counter.reset()
print("Count after reset:", counter.get_count())
print("\n---------------------- Thank You -----------------------------\n")

# ----------------------------------------------------------------------------
# # End of the File: 02_oops/day3_practice.py