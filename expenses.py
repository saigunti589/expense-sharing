class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)


class Expense:
    def __init__(self, description, amount, paid_by, split_with):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_with = split_with


class ExpenseTracker:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)

    def add_expense(self, description, amount, paid_by, split_with):
        expense = Expense(description, amount, paid_by, split_with)
        self.users[paid_by].add_expense(expense)
        for user in split_with:
            self.users[user].add_expense(expense)

    def show_balance(self, user):
        balance = 0
        for expense in self.users[user].expenses:
            if expense.paid_by == user:
                balance -= expense.amount
            else:
                balance += expense.amount / len(expense.split_with)
        return balance


# Example usage:
tracker = ExpenseTracker()
tracker.add_user("Alice")
tracker.add_user("Bob")
tracker.add_expense("Dinner", 50, "Alice", ["Alice", "Bob"])
tracker.add_expense("Groceries", 30, "Bob", ["Alice", "Bob"])

print("Alice's balance:", tracker.show_balance("Alice"))
print("Bob's balance:", tracker.show_balance("Bob"))