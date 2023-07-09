'''
Έχετε προσληφθεί για να δημιουργήσετε ένα απλό σύστημα τραπεζικού λογαριασμού.
Το σύστημα πρέπει να υποστηρίζει δύο τύπους λογαριασμών: `SavingsAccount`
και `CheckingAccount`. Και οι δύο τύποι λογαριασμών πρέπει να έχουν κοινές
λειτουργίες όπως `deposit()`, `withdraw()` και `get_balance()`, αλλά κάθε
τύπος λογαριασμού έχει κάποια μοναδικά χαρακτηριστικά.

1. Ορίστε μια βασική κλάση με το όνομα `BankAccount` με τις ακόλουθες μεθόδους:
   - `__init__(self, account_number, initial_balance)`: Αρχικοποιεί τον
   λογαριασμό με έναν αριθμό λογαριασμού και έναν αρχικό υπόλοιπο.
   - `deposit(self, amount)`: Προσθέτει το καθορισμένο ποσό στο υπόλοιπο
   του λογαριασμού.
   - `withdraw(self, amount)`: Αφαιρεί το καθορισμένο ποσό από το υπόλοιπο
   του λογαριασμού.
   - `get_balance(self)`: Επιστρέφει το τρέχον υπόλοιπο του λογαριασμού.

2. Δημιουργήστε μια υποκλάση με το όνομα `SavingsAccount` που κληρονομεί
από την `BankAccount`. Προσθέστε τα ακόλουθα χαρακτηριστικά:
   - Μια μεταβλητή κλάσης με το όνομα `interest_rate` που είναι ίση με 0.05 (5%).
   - Αντικαταστήστε τη μέθοδο `get_balance()` για να υπολογίζει και να
   επιστρέφει το υπόλοιπο συν το επιτόκιο που έχει αποκτηθεί βάσει του επιτοκίου.

3. Δημιουργήστε μια άλλη υποκλάση με το όνομα `CheckingAccount` που κληρονομεί
από την `BankAccount`. Προσθέστε τα ακόλουθα χαρακτηριστικά:
   - Μια μεταβλητή κλάσης με το όνομα `transaction_fee` που είναι ίση με 1.0.
   - Αντικαταστήστε τη μέθοδο `withdraw()` για να αφαιρεί το τέλος συναλλαγής
   από το υπόλοιπο του λογαριασμού.

4. Δοκιμάστε τον κώδικά σας δημιουργώντας παραδείγματα και `SavingsAccount` και
`CheckingAccount`. Πραγματοποιήστε διάφορες λειτουργίες όπως καταθέσεις,
αναλήψεις και ερωτήσεις υπολοίπου και παρατηρήστε τα αποτελέσματα.
'''

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def get_balance(self):
        interest = self.balance * self.interest_rate
        return self.balance + interest


class CheckingAccount(BankAccount):
    transaction_fee = 1.0

    def withdraw(self, amount):
        self.balance -= amount + self.transaction_fee


# Δοκιμή του κώδικα
savings = SavingsAccount("SAV001", 1000)
savings.deposit(500)
savings.withdraw(200)
print("Υπόλοιπο Λογαριασμού Αποταμίευσης:", savings.get_balance())

checking = CheckingAccount("CHK001", 2000)
checking.deposit(100)
checking.withdraw(50)
print("Υπόλοιπο Λογαριασμού Ελέγχου:", checking.get_balance())
