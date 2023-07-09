# exercise 1
#
# Γράψτε ένα πρόγραμμα για να δημιουργήσετε μια κλάση Bank, η οποία να 
# αντιπροσωπεύει μια τράπεζα. Δημιουργήστε μεθόδους όπως, δημιουργία 
# λογαριασμού, κατάθεση ποσού, ανάληψη ποσού, έλεγχος του balance. 
# Χρησιμοποιήστε if - else, σε περιπτώσεις όπως, σε περίπτωση ανάληψης,
# το ποσό είναι μικρότερο από το διαθέσιμο. Ζητήστε εκτυπώσεις.


class Bank:
    def __init__(self):
        self.customers = {}
        
    def create_account(self, account_number, initial_balance = 0):
        if account_number in self.customers:
            print("Ο λογαριασμός υπάρχει ήδη")
        else:
            self.cutomers[account_number] = initial_balance
            print("Ο λογαριασμός μας δημιουργήθηκε επιτυχώς")
    
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Η κατάθεση πραγματοποιήθηκε επιτυχώς.")
        else:
            print("Ο αριθμός λογαριασμού δεν υπάρχει.")
    
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Η ανάληψη ήταν επιτυχής")
            else:
                print("Μη επαρκές διαθέσιμο υπόλοιπο.")
        else:
            print("Ο αριθμός λογαριασμού δεν υπάρχει.")
            
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f'Διαθέσιμο κεφάλαιο: {balance}')
        else:
            print("Ο αριθμός λογαριασμού δεν υπάρχει.")



bank = Bank()
acno1 = 'SB-123'
dep_amt_1 = 1000
print('Νέος αριθμός λογαριασμού: ', acno1, ' - Ποσό κατάθεσης: ', dep_amt_1)
bank.create_account(acno1, dep_amt_1)

acno2 = 'SB-124'
dep_amt_2 = 1500
print('Νέος αριθμός λογαριασμού: ', acno2, ' - Ποσό κατάθεσης: ', dep_amt_2)
bank.create_account(acno2, dep_amt_2)

wamt1 = 600
print('\nΚατάθεση €: ', wamt1, ' σε αριθμό λογαριασμού ', acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print('Ανάληψη €: ', wamt2, ' από αριθμό λογαριασμού: ', acno2)
bank.make_withdrawal(acno2, wamt2)

print('Αριθμός λογαριασμού: ', acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Ανάληψη €: ", wamt3, " από αρθμό λογαριασμού: ", acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = 'SB-134'
print('Αριθμός λογαριασμού: ', acno3)
bank.check_balance(acno3)