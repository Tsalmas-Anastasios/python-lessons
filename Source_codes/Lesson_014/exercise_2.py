# exercise 2
#
#
# Φτιάξτε μια κλάση Calculator η οποία να έχει σαν μεθόδους τις βασικές
# αριθμητικές πράξεις (πρόσθεση, αφαίρεση, πολλαπλασιασμό, διαίρεση).
# Δημιουργήστε τα αντίστοιχα αντικείμενα και ζητήστε την εκτύπωση για κάθε
# μέθοδο. Σε περίπτωση διαίρεσης με το μηδέν, πρέπει το προγραμματάκι σας να
# προβλέπει την εκτύπωση ενός error.

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return('Δεν μπορεί να γίνει διαίρεση με το \'0\'')


calculator = Calculator()

print('7 + 5 = ', calculator.add(7, 5))                         # add
print('34 - 21 = ', calculator.subtract(34, 21))                # subtract
print('54 * 2 = ', calculator.multiply(54, 2))                  # multiply
print('144 / 2 = ', calculator.divide(144, 2))                  # divide
print('45 / 0 = ', calculator.divide(45, 0))                    # divide