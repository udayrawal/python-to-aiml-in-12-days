"""
📘 Day 4 – Inheritance & Polymorphism in Object-Oriented Programming (OOP)

What I learned today:
1️⃣ Inheritance
   - Created child classes using parent classes
   - Reused common attributes and methods using inheritance
   - Used `super()` to initialize parent class properties

2️⃣ Polymorphism
   - Overridden methods to change behavior in child classes
   - Same method name, different implementations
   - Achieved dynamic behavior at runtime

3️⃣ Real-World & ML-Style Design
   - Designed role-based systems (Employee → Manager)
   - Built extensible notification systems
   - Understood base-model architecture used in ML frameworks

OOP Programs Built Today:
✔ Employee & Manager System
✔ Notification System (Email & SMS)
✔ ML-style Base Model System

Focus:
→ Thinking in hierarchies and behaviors  
→ Writing extensible and reusable code  
→ Building foundations for ML/AI system design
"""


# --------------------------------------------------
# 1. Employee System (Inheritance + Polymorphism)
# --------------------------------------------------

class Employee:
    def __init__(self, name, position, salary, employee_id, department):
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₹{self.salary}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

    def get_salary(self):
        return self.salary if self.salary is not None else 0


class Manager(Employee):
    def get_salary(self):
        return self.salary + 10000 if self.salary is not None else 10000

    def apply_raise(self, amount):
        if self.salary is not None:
            self.salary += amount
            print(f"New salary after raise: ₹{self.salary}")
        else:
            print("Salary information is not available.")


print("\n---------------------- Employee System -----------------------------\n")

employee1 = Manager("John Doe", "Software Engineer", 60000, "E101", "IT")
employee1.display_info()
employee1.apply_raise(5000)

print("\n---------------------------------------------------\n")

employee2 = Manager("Jane Smith", "Data Analyst", 55000, "E102", "Analytics")
employee2.display_info()
employee2.apply_raise(4000)

print("\n---------------------------------------------------\n")

employee3 = Manager(None, None, None, None, None)
employee3.display_info()
employee3.apply_raise(150)

print("\n---------------------- Thank You -----------------------------\n")


# --------------------------------------------------
# 2. Notification System (Polymorphism)
# --------------------------------------------------

class Notification:
    def __init__(self, message, recipient, notification_type):
        self.message = message
        self.recipient = recipient
        self.notification_type = notification_type

    def send_notification(self):
        print(
            f"Sending {self.notification_type} notification "
            f"to {self.recipient}: {self.message}"
        )


class EmailNotification(Notification):
    def __init__(self, message, recipient, subject):
        super().__init__(message, recipient, "Email")
        self.subject = subject

    def send_notification(self):
        print(f"Sending Email to {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Message: {self.message}")


class SMSNotification(Notification):
    def __init__(self, message, recipient, phone_number):
        super().__init__(message, recipient, "SMS")
        self.phone_number = phone_number

    def send_notification(self):
        print(
            f"Sending SMS to {self.phone_number} "
            f"({self.recipient}): {self.message}"
        )


print("\n---------------------- Notification System -----------------------------\n")

email_notif = EmailNotification(
    "Your order has been shipped.", "Alice", "Order Update"
)
email_notif.send_notification()

print("\n---------------------------------------------------\n")

sms_notif = SMSNotification(
    "Your OTP is 123456.", "Bob", "+1234567890"
)
sms_notif.send_notification()

print("\n---------------------------------------------------\n")

email_notif2 = EmailNotification(
    "Meeting at 10 AM tomorrow.", "Charlie", "Meeting Reminder"
)
email_notif2.send_notification()

print("\n---------------------- Thank You -----------------------------\n")


# --------------------------------------------------
# 3. ML-Style Base Model System (Polymorphism)
# --------------------------------------------------

class BaseModel:
    def train(self, data):
        print("Training the model with data.")

    def predict(self, input_data):
        print("Predicting output for the given input data.")


class LinearRegressionModel(BaseModel):
    def train(self, data):
        print("Training Linear Regression Model with data.")

    def predict(self, input_data):
        print("Predicting output using Linear Regression Model.")


print("\n---------------------- ML Model System -----------------------------\n")

linear_model = LinearRegressionModel()
linear_model.train("Sample Training Data")
linear_model.predict("Sample Input Data")

print("\n---------------------- Thank You -----------------------------\n")

# ----------------------------------------------------------------------------
# # End of the File: 02_oops/day4_practice.py