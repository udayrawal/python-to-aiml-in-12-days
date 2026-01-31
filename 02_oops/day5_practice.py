"""
📘 Day 5 – Abstraction & Interfaces using Abstract Base Classes (ABC)

What I learned today:
1️⃣ Abstraction
   - Defined abstract base classes to act as contracts
   - Enforced method implementation in child classes
   - Prevented incomplete class instantiation

2️⃣ Interfaces (Python-style)
   - Used abstract methods to define required behavior
   - Achieved interface-like design using ABC
   - Ensured consistent method names across implementations

3️⃣ ML & System Design Patterns
   - Designed ML-style model interfaces (train / predict)
   - Built interchangeable components using polymorphism
   - Understood how real ML frameworks enforce contracts

OOP Systems Built Today:
✔ ML Model Interface (Linear & Tree Models)
✔ Payment Processing Interface
✔ Dataset Loader Interface
✔ Trainer Interface

Focus:
→ Writing scalable, enforceable OOP designs  
→ Thinking in contracts, not implementations  
→ Preparing foundations for ML/AI frameworks
"""


# --------------------------------------------------
# 1. Abstract ML Model Interface
# --------------------------------------------------

from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, x):
        pass


class LinearModel(Model):
    def train(self, data):
        return "Training linear model"

    def predict(self, x):
        return f"Predicting {x} using linear model"


class TreeModel(Model):
    def train(self, data):
        return "Training tree model"

    def predict(self, x):
        return f"Predicting {x} using Tree Model"


print("\n---------------------- ML Model Interface -----------------------------\n")

models = [LinearModel(), TreeModel()]

for model in models:
    print(model.train("dataset"))
    print(model.predict(5))

print("\n---------------------------------------------------\n")


# --------------------------------------------------
# 2. Abstract Payment System
# --------------------------------------------------

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class UPI(Payment):
    def process_payment(self, amount):
        return f"Paid ₹{amount} via UPI"


class Card(Payment):
    def process_payment(self, amount):
        return f"Paid ₹{amount} via Card"


print("\n---------------------- Payment System -----------------------------\n")

upi_payment = UPI()
card_payment = Card()

print(upi_payment.process_payment(500))
print(card_payment.process_payment(1200))

print("\n---------------------------------------------------\n")


# --------------------------------------------------
# 3. Abstract Dataset Loader Interface
# --------------------------------------------------

class Dataset(ABC):
    @abstractmethod
    def load_data(self):
        pass


class APIDataset(Dataset):
    def load_data(self):
        return "Loading data from API"


print("\n---------------------- Dataset Loader -----------------------------\n")

dataset = APIDataset()
print(dataset.load_data())

print("\n---------------------------------------------------\n")


# --------------------------------------------------
# 4. Trainer Interface
# --------------------------------------------------

class Trainer(ABC):
    @abstractmethod
    def run(self):
        pass


class SimpleTrainer(Trainer):
    def run(self):
        return "Running simple training loop"


print("\n---------------------- Trainer Interface -----------------------------\n")

trainer = SimpleTrainer()
print(trainer.run())

print("\n---------------------- Thank You -----------------------------\n")

# -----------------------------------------------------------------------------------------
# End of File: 02_oops/day5_practice.py